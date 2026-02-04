import os
import random
from collections import Counter
from tqdm import tqdm
from kiwipiepy import Kiwi
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image  # 마스크 로드를 위해 추가
import numpy as np     # 마스크 배열 변환 위해 추가

# ===============================
# 1. 형태소 분석 및 N-gram 처리 함수 (기존 유지)
# ===============================
def extract_keywords_streaming(file_path, kiwi):
    words = []
    bigrams = []
    
    print("📊 파일 읽기 중...")
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    line_count = len(lines)
    print(f"📄 총 {line_count}행의 데이터를 분석합니다. (호환 모드)")

    for line in tqdm(lines, total=line_count, desc="토크나이징 중"):
        result = kiwi.analyze(line)
        if not result:
            continue
            
        tokens = result[0][0]
        
        # 1. 단어 추출
        extracted = [t.form for t in tokens if t.tag in ['NNG', 'NNP', 'XR', 'VA', 'VV']]
        words.extend(extracted)
        
        # 2. 2-grams 생성
        for i in range(len(tokens) - 1):
            if tokens[i].tag.startswith('N') and tokens[i+1].tag in ['NNG', 'VA', 'VV', 'MAG']:
                bigrams.append(f"{tokens[i].form} {tokens[i+1].form}")
                    
    return words + bigrams

# ===============================
# 2. 메인 실행 함수 (마스크 & 투명 배경 추가)
# ===============================
def main():
    input_file = "merged_reviews1.txt"  # ThinQ 리뷰 파일
    font_path = 'C:/Windows/Fonts/malgun.ttf'
    mask_path = 'bonobono.jpg'  # 사용자가 원하는 이미지 파일 (예: 업로드된 첫 이미지 저장)
    output_img = 'thinq_sentiment_wordcloud_transparent.png'  # 출력 파일명 (투명 PNG)

    if not os.path.exists(input_file):
        print(f"❌ 에러: '{input_file}' 파일을 찾을 수 없습니다.")
        return
    if not os.path.exists(mask_path):
        print(f"❌ 에러: 마스크 이미지 '{mask_path}'를 찾을 수 없습니다. 이미지를 다운로드해 저장하세요.")
        return

    # Kiwi 초기화
    kiwi = Kiwi()

    # 키워드 추출
    all_tokens = extract_keywords_streaming(input_file, kiwi)

    # 부정 감정 키워드 설정 (BX: ThinQ Pain Points 중심)
    sentiment_keywords = [
        '불편', '어렵', '복잡', '귀찮', '번거로움', '실망', '짜증', '화남', '답답', '짜증나',
        '안됨', '실패', '오류', '버그', '멈춤', '튕김', '느림', '렉', '지연', '무거움',
        '거부', '포기', '이탈', '삭제', '재설치', '싫', '최악', '별로', '후회', '아쉽',
        # 1. 편리함 및 효율성
        '편리', '편해', '간편', '유용', '도움', '효율', '똑똑', '스마트', '혁신', 
        '자동', '세상편함', '삶의질', '꿀템', '필수', '빠름', '신속',
        
        # 2. 만족도 및 감정
        '좋음', '좋아', '만족', '추천', '최고', '훌륭', '감동', '행복', '감사', 
        '신기', '재밌', '즐거움', '뿌듯', '애용', '대만족',
        
        # 3. 디자인 및 UI/UX
        '깔끔', '예쁨', '세련', '직관적', '보기편함', '심플', '디자인', '가독성',
        
        # 4. 기능적 성공 (Pain Point 해결)
        '한번에', '연결잘됨', '성공', '해결', '안정적', '정확', '알아서', '척척'
    ]

    # 제외 단어 (기존 + 확장)
    exclude_words = ['하다', '있다', '되다', '보기', '사용', '로그인', '씽큐', '어플', '앱', 'LG', 'ThinQ']
    exclude_appliances = [
        '오브제', '컬렉션', '일렉트로룩스', '냉장고', '세탁기', '건조기', '에어컨', '청소기', '오븐', '스타일러',
        '와이파이', 'wifi', '연결', '연동', '페어링', '인식', '등록', '업데이트', '설정', '기능', '모드','다이렉트','렉트','일렉트로','일렉트로마트'
    ]

    # 빈도 계산 및 필터링
    word_counts = Counter(all_tokens)
    final_counts = {}

    for word, count in tqdm(word_counts.items(), desc="키워드 필터링 중"):
        if (len(word) > 1 and 
            word not in exclude_words and 
            not any(appliance in word for appliance in exclude_appliances) and 
            any(sentiment in word for sentiment in sentiment_keywords)):
            final_counts[word] = count

    if not final_counts:
        print("⚠️ 필터링된 결과가 없습니다. 감정 키워드를 더 확장해보세요.")
        return

    # 마스크 이미지 로드 (BX: 사용자가 원하는 형태로 워드 배치)
    mask = np.array(Image.open(mask_path))

    # 워드클라우드 생성 (LG 색상, 마스크 적용, 투명 배경)
    lg_colors = ["#A50034", "#2B2B2B", "#4A4A4A", "#6A6A6A"]
    def lg_color_func(*args, **kwargs):
        return random.choice(lg_colors)

    print("🎨 감정 중심 워드클라우드 이미지를 생성 중입니다 (마스크 적용, 투명 배경)...")
    wordcloud = WordCloud(
        font_path=font_path,
        background_color=None,  # 투명 배경 설정
        mode='RGBA',            # 알파 채널 지원 (투명)
        mask=mask,              # 이미지 마스크 적용
        width=1200, height=1200,
        max_words=200,
        relative_scaling=0.2,
        color_func=lg_color_func,
        prefer_horizontal=0.8
    ).generate_from_frequencies(final_counts)

    plt.figure(figsize=(10, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(output_img, dpi=300, transparent=True)  # 투명 PNG 저장
    print(f"✅ 분석 완료! 결과 이미지 저장됨: {output_img} (배경 투명)")
    plt.show()

if __name__ == "__main__":
    main()