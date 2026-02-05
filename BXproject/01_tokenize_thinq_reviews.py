import os
import pickle
from tqdm import tqdm
from kiwipiepy import Kiwi

def extract_keywords_streaming(file_path, kiwi):
    words = []
    bigrams = []

    print("📊 파일 읽기 중...")
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    print(f"📄 총 {len(lines)}행 분석")

    for line in tqdm(lines, desc="Kiwi 형태소 분석"):
        result = kiwi.analyze(line)
        if not result:
            continue

        tokens = result[0][0]

        # 단어
        extracted = [
            t.form for t in tokens
            if t.tag in ['NNG', 'NNP', 'XR', 'VA', 'VV']
        ]
        words.extend(extracted)

        # 2-gram
        for i in range(len(tokens) - 1):
            if tokens[i].tag.startswith('N') and tokens[i + 1].tag in ['NNG', 'VA', 'VV', 'MAG']:
                bigrams.append(f"{tokens[i].form} {tokens[i + 1].form}")

    return words + bigrams


def main():
    input_file = "LG_ThinQ어플,앱 모든 리뷰 데이터.txt"
    output_file = "tokens.pkl"

    kiwi = Kiwi()

    all_tokens = extract_keywords_streaming(input_file, kiwi)

    with open(output_file, "wb") as f:
        pickle.dump(all_tokens, f)

    print(f"✅ 토크나이즈 완료: {len(all_tokens)} tokens 저장됨")
    print(f"📦 저장 위치: {output_file}")


if __name__ == "__main__":
    main()
