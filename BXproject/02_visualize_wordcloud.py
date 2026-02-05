import pickle
import random
from collections import Counter
from tqdm import tqdm
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def main():
    token_file = "data/tokens.pkl"
    mask_path = "mask/스마트폰 이미지.jpg"
    font_path = "C:/Windows/Fonts/malgun.ttf"
    output_img = "thinq_긍정.png"

    with open(token_file, "rb") as f:
        all_tokens = pickle.load(f)

    print(f"📦 토큰 로드 완료: {len(all_tokens)}개")

    # 감정 키워드
    sentiment_keywords = [
        '편리', '간편', '유용', '도움', '자동', '만족', '추천',
        '최고', '좋아', '깔끔', '직관', '성공', '안정적'
    ]

    exclude_words = ['하다', '있다', '되다', '사용', 'LG', 'ThinQ', '씽큐']
    exclude_appliances = [
        '냉장고', '세탁기', '에어컨', '청소기',
        '연결', '연동', '등록', '설정'
    ]

    word_counts = Counter(all_tokens)
    final_counts = {}

    for word, count in tqdm(word_counts.items(), desc="키워드 필터링"):
        if (
            len(word) > 1
            and word not in exclude_words
            and not any(a in word for a in exclude_appliances)
            and any(s in word for s in sentiment_keywords)
        ):
            final_counts[word] = count

    mask = np.array(Image.open(mask_path).convert("RGB"))

    lg_colors = ["#A50034", "#19CD76", "#B310E5", "#6A6A6A"]
    def lg_color_func(*args, **kwargs):
        return random.choice(lg_colors)

    wc = WordCloud(
        font_path=font_path,
        background_color=None,
        mode="RGBA",
        mask=mask,
        width=mask.shape[1],
        height=mask.shape[0],
        max_words=200,
        color_func=lg_color_func
    ).generate_from_frequencies(final_counts)

    plt.figure(figsize=(10, 10))
    plt.imshow(wc)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(output_img, dpi=300, transparent=True)
    plt.show()

    print(f"✅ 워드클라우드 생성 완료: {output_img}")


if __name__ == "__main__":
    main()
