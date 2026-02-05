import os
import pickle
import random
from collections import Counter
from tqdm import tqdm
from kiwipiepy import Kiwi
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# ===============================
# 1. 키워드 추출 함수 (기존 로직 유지)
# ===============================
def extract_keywords_from_data(text_list, kiwi):
    words = []
    bigrams = []
    
    print(f"📊 총 {len(text_list)}개의 제품군 데이터를 분석합니다.")

    for text in tqdm(text_list, desc="토크나이징 중"):
        if not text or len(text.strip()) == 0:
            continue
            
        result = kiwi.analyze(text)
        if not result: continue
        tokens = result[0][0]
        
        extracted = [t.form for t in tokens if t.tag in ['NNG', 'NNP', 'XR', 'VA', 'VV']]
        words.extend(extracted)
        
        for i in range(len(tokens) - 1):
            if tokens[i].tag.startswith('N') and tokens[i+1].tag in ['NNG', 'VA', 'VV', 'MAG', 'XSA']:
                bigrams.append(f"{tokens[i].form}{tokens[i+1].form}")
                    
    return words + bigrams

# ===============================
# 2. 메인 실행 함수
# ===============================
def main():
    pickle_file = "class_type_product_data.pkl" 
    font_path = 'C:/Windows/Fonts/malgunbd.ttf' 
    mask_path = 'bonobono.jpg' 
    output_img = 'lg_qna_full_wordcloud.png'

    if not os.path.exists(pickle_file):
        print(f"❌ 에러: '{pickle_file}' 파일이 없습니다.")
        return
    
    with open(pickle_file, "rb") as f:
        raw_data = pickle.load(f)
    
    all_texts = []
    for class_name in raw_data:
        for type_name in raw_data[class_name]:
            all_texts.append(raw_data[class_name][type_name][1])

    kiwi = Kiwi()
    all_tokens = extract_keywords_from_data(all_texts, kiwi)

    # --- [수정 포인트: 필터 해제 및 제외 단어 강화] ---
    # 1. 감정 키워드로 제한하지 않고 모든 단어를 후보로 둡니다.
    # 2. 대신 의미 없는 불용어를 꼼꼼하게 추가하여 노이즈를 줄입니다.
    exclude_words = [
        '하다', '있다', '되다', '보기', '사용', 'LG', '제품', '확인', '문의', '드립니다',
        '궁금', '관련', '내용', '질문', '방법', '알려', '주세요', '가능', '어떻게', '해서',
        '문의글', '제목', '현상', '때문', '경우', '대한', '문의드려요', '이거', '저거', '어디'
    ]
    
    word_counts = Counter(all_tokens)
    final_counts = {}

    for word, count in tqdm(word_counts.items(), desc="키워드 정제 중"):
        # 2글자 이상이고 제외 리스트에 없는 모든 단어를 수용
        if len(word) >= 2 and word not in exclude_words:
            final_counts[word] = count
    # --------------------------------------------------

    if not final_counts:
        print("⚠️ 데이터가 없습니다.")
        return

    print("🎨 워드클라우드 생성 중 (전체 데이터 모드)...")
    try:
        mask = np.array(Image.open(mask_path))
    except:
        mask = None

    lg_colors = ["#A50034", "#2B2B2B", "#4A4A4A", "#7A7A7A", "#E60000"]
    def lg_color_func(*args, **kwargs):
        return random.choice(lg_colors)

    wordcloud = WordCloud(
        font_path=font_path,
        background_color='white',
        mask=mask,
        width=1500, height=1500,
        max_words=250,              # 필터를 풀었으므로 단어 수를 조금 더 늘림
        min_font_size=5,            # 빈 공간을 채우기 위해 최소 폰트 낮춤
        max_font_size=250,
        relative_scaling=0.2,       # 빈도 차이를 줄여 밀도를 높임
        color_func=lg_color_func,
        contour_width=2,
        contour_color='steelblue'
    ).generate_from_frequencies(final_counts)

    plt.figure(figsize=(12, 12))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    
    plt.savefig(output_img, dpi=300)
    print(f"✅ 시각화 완료! 파일 저장됨: {output_img}")
    plt.show()

if __name__ == "__main__":
    main()