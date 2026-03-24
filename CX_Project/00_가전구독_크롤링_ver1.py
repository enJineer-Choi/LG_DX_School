from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from tqdm import tqdm
import re
import os
from urllib.parse import quote

# ---------------------------------------------------------------
# 전처리 함수
# ---------------------------------------------------------------
def preprocess_sentence_kr(w):
    w = w.strip()
    w = re.sub(r"[^A-Za-z0-9가-힣?.!,]+", " ", w)
    w = w.strip()
    return w

# ---------------------------------------------------------------
# 키워드 사전 (ver1 보강)
# ---------------------------------------------------------------
KEYWORDS_LG_SUBSCRIPTION = {

    "인지_및_탐색": [
        "LG 가전 구독", "엘지 가전 구독", "가전 구독 서비스란", "LG전자 구독 혜택", "LG 구독",
        "가전 구독이란", "가전 구독 처음", "가전제품 구독 서비스", "LG전자 구독 서비스",
        "가전 구독 어떻게", "LG 구독 신청 방법", "가전 월정액 서비스"
    ],

    "비교_및_구매": [
        "가전 구독 vs 구매", "가전 렌탈 구독 차이", "LG 가전 구독 가격",
        "가전 구독 일시불 비교", "가전 구독 사은품",
        "가전 구독 렌탈 차이", "가전 구독 할부 비교", "LG 구독 가격표",
        "가전 구독 총비용", "가전 구독 이득인가", "가전 구독 비용 계산",
        "LG 구독 vs 삼성 렌탈", "코웨이 vs LG 구독",
        # ✅ ver1 추가
        "가전 구독 카드 혜택",
        "가전 구독 실제 후기",
        "LG 구독 베스트샵 상담",
        "가전 구독 계약서",
        "가전 구독 약정 위약금 계산",
    ],

    "제품_특화": [
        "LG 세탁기 구독", "LG 냉장고 구독", "LG 에어컨 구독",
        "LG 스타일러 구독", "LG 슈케이스 구독", "LG 정수기 구독",
        "LG 건조기 구독", "LG TV 구독",
        "LG 식기세척기 구독", "LG 공기청정기 구독", "LG 전자레인지 구독",
        "LG 안마의자 구독", "LG 의류관리기 구독", "LG 드럼세탁기 구독",
        "LG 통돌이 구독", "LG 미니워시 구독"
    ],

    "유지_및_관리": [
        "LG 가전 구독 케어", "가전 구독 필터 교체", "가전 구독 방문 점검", "LG전자 케어십",
        "가전 구독 케어매니저", "가전 구독 자가교체", "가전 구독 AS",
        "LG 구독 방문 주기", "가전 구독 소모품 교체", "LG 구독 정기점검",
        "가전 구독 관리 서비스", "LG 케어솔루션"
    ],

    "페인포인트_및_이탈": [
        "가전 구독 위약금", "가전 구독 단점", "가전 구독 해지", "LG 구독 서비스 불만",
        "가전 구독 비싸다", "가전 구독 후기", "LG 가전 구독 솔직후기",
        "가전 구독 해보니", "가전 구독 실망", "가전 구독 중도해지", "구독 가전 반납",
        "LG 구독 해지 방법", "가전 구독 환불", "가전 구독 이사할때",
        "LG 구독 취소 위약금", "가전 구독 함정"
    ],

    "구독_정보_탐색": [
        "가전 구독 신청 절차", "LG 구독 계약 기간", "가전 구독 등록 방법",
        "LG 구독 약정 기간", "가전 구독 몇 년", "LG 구독 온라인 신청",
        "가전 구독 서류", "LG 구독 오프라인 신청"
    ],

    "라이프스타일_연계": [
        "신혼부부 가전 구독", "1인가구 가전 구독", "원룸 가전 구독",
        "이사할때 가전 구독", "자취 가전 구독", "아이있는집 가전 구독",
        "시니어 가전 구독", "40대 가전 구독", "맞벌이 가전 구독",
        # ✅ ver1 추가
        "혼수 가전 구독",
        "전세 가전 구독",
        "분양 가전 구독",
        "아파트 입주 가전 구독",
        "육아 가전 구독",
    ],

    "경쟁사_비교": [
        "삼성 케어플러스 후기", "코웨이 렌탈 후기", "SK매직 렌탈 후기",
        "가전 렌탈 업체 비교", "LG vs 코웨이 정수기", "가전 구독 브랜드 비교",
        "삼성 렌탈 vs LG 구독"
    ],

    # 🆕 ver1 신규 카테고리: 실사용 고객 목소리 확보용
    "구독_후_경험": [
        "LG 가전 구독 사용 중",
        "가전 구독 케어 방문 후기",
        "가전 구독 필터 교체 경험",
        "LG 구독 만족",
        "가전 구독 갱신",
        "가전 구독 연장",
        "LG 구독 업그레이드",
        "가전 구독 재계약",
    ],
}


# ---------------------------------------------------------------
# 수집량 설정 (ver1 조정)
# ---------------------------------------------------------------
MAX_SCROLL = 30    # ✅ 50 → 30 (30 이후 신규 링크 거의 없음, 속도 개선)
MAX_POSTS  = 150   # ✅ 100 → 150 (수집량 증대)

# ---------------------------------------------------------------
# 플랫폼별 설정
# ---------------------------------------------------------------
PLATFORM_CONFIG = {
    "blog": {
        "url":         lambda kw: f"https://search.naver.com/search.naver?ssc=tab.blog.all&query={kw}&sm=tab_opt&nso=so%3Ar%2Cp%3A1y",
        "title_cls":   "a.fender-ui_228e3bd1.AgQsNgarR3C1k5Frc3VC",
        "title_cls2":  "a.title_link",
        "href_filter": lambda h: "blog.naver.com" in h,
    },
    "cafe": {
        "url":         lambda kw: f"https://search.naver.com/search.naver?cafe_where=&date_option=6&query={kw}&sm=mtb_opt&ssc=tab.cafe.all&st=rel",
        "title_cls":   "a.title_link",
        "title_cls2":  "a.api_txt_lines",
        "href_filter": lambda h: "cafe.naver.com" in h,
    },
    "kin": {
        "url":         lambda kw: f"https://search.naver.com/search.naver?ssc=tab.kin.kqna&where=kin&query={kw}",
        "title_cls":   "a.fender-ui_228e3bd1.TyKgZsBii5WemCXs9JiJ",
        "title_cls2":  "a.question_text",
        "href_filter": lambda h: "kin.naver.com" in h,
    },
}

# ---------------------------------------------------------------
# URL 수집 함수
# ---------------------------------------------------------------
def get_href_list(driver, keyword, platform="blog",
                  max_scroll=MAX_SCROLL, max_posts=MAX_POSTS):
    cfg = PLATFORM_CONFIG[platform]
    encoded = quote(keyword)
    url = cfg["url"](encoded)

    driver.get(url)
    time.sleep(2)

    scroll = driver.find_element(By.TAG_NAME, "body")

    href_set = set()
    href_list = []

    for _ in range(max_scroll):
        scroll.send_keys(Keys.END)
        time.sleep(1)  # ✅ 2초 → 1초 (속도 개선, 네이버 차단 기준 충분)

        links = driver.find_elements(By.CSS_SELECTOR, cfg["title_cls"])
        if not links:
            links = driver.find_elements(By.CSS_SELECTOR, cfg["title_cls2"])

        for l in links:
            href = l.get_attribute("href") or ""
            if cfg["href_filter"](href) and href not in href_set:
                href_set.add(href)
                href_list.append(href)

        if len(href_list) >= max_posts:
            break

    return href_list[:max_posts]

# ---------------------------------------------------------------
# 본문 추출 함수
# ---------------------------------------------------------------
def get_content(driver, url, platform):
    try:
        driver.get(url)
        time.sleep(1)  # ✅ 2초 → 1초

        if platform == "blog":
            try:
                driver.switch_to.frame("mainFrame")
            except Exception:
                pass
            text = driver.find_element(By.CSS_SELECTOR, "div.se-main-container").text

        elif platform == "cafe":
            try:
                driver.switch_to.frame("cafe_main")
            except Exception:
                pass
            text = driver.find_element(By.CSS_SELECTOR, "div.se-main-container, div.article_viewer").text

        elif platform == "kin":
            q_els = driver.find_elements(By.CSS_SELECTOR, ".c-heading__content")
            a_els = driver.find_elements(By.CSS_SELECTOR, "div.se-main-container, div._answer_content")
            q_text = q_els[0].text if q_els else ""
            a_text = " / [답변]: ".join([a.text for a in a_els])
            text = q_text + (" / [답변]: " + a_text if a_text else "")

        driver.switch_to.default_content()
        return preprocess_sentence_kr(text) if text.strip() else "본문 내용 없음"

    except Exception:
        driver.switch_to.default_content()
        return "본문 추출 실패"

# ---------------------------------------------------------------
# 전체 크롤링 실행
# ---------------------------------------------------------------
def run_all_crawling():
    driver = wb.Chrome()
    platforms = [("blog", "블로그"), ("cafe", "카페"), ("kin", "지식iN")]
    all_results = []

    output_path = "./가전 구독"
    os.makedirs(output_path, exist_ok=True)

    try:
        for category, keywords in KEYWORDS_LG_SUBSCRIPTION.items():
            print(f"\n{'='*50}")
            print(f"📂 카테고리: {category}")
            print(f"{'='*50}")

            category_results = []  # ✅ 카테고리별 중간 저장용

            for kw in keywords:
                for p_code, p_name in platforms:
                    print(f"\n  🔍 [{p_name}] '{kw}' 링크 수집 중...")

                    href_list = get_href_list(driver, kw, platform=p_code)
                    print(f"      → 링크 {len(href_list)}건 수집. 본문 수집 시작...")

                    success = 0
                    for url in tqdm(href_list, desc=f"    {p_name} 본문", leave=False):
                        content = get_content(driver, url, p_code)
                        if "실패" not in content and "없음" not in content:
                            success += 1
                        row = {
                            "카테고리":  category,
                            "플랫폼":    p_name,
                            "키워드":    kw,
                            "url":       url,
                            "full_text": content,
                        }
                        all_results.append(row)
                        category_results.append(row)

                    print(f"      ✅ 본문 수집 완료: {success}/{len(href_list)}건")
                    time.sleep(1)

            # ✅ 카테고리 완료 시 중간 저장 (크롤링 중단돼도 데이터 보존)
            if category_results:
                tmp_df = pd.DataFrame(category_results)
                tmp_path = os.path.join(output_path, f"tmp_{category}.csv")
                tmp_df.to_csv(tmp_path, index=False, encoding="utf-8-sig")
                print(f"\n  💾 중간 저장 완료: {tmp_path} ({len(tmp_df)}건)")

    finally:
        driver.quit()

    return all_results

# ---------------------------------------------------------------
# 메인 실행
# ---------------------------------------------------------------
if __name__ == "__main__":
    results = run_all_crawling()

    if results:
        df = pd.DataFrame(results)

        # ✅ ver1: URL + 본문 앞 100자 기준 이중 중복 제거
        df = df.drop_duplicates(subset=["url"])
        df["text_key"] = df["full_text"].str[:100]
        df = df.drop_duplicates(subset=["text_key"])
        df = df.drop("text_key", axis=1)

        output_path = "./가전 구독"
        os.makedirs(output_path, exist_ok=True)

        save_path = os.path.join(output_path, "LG_subscription_ver1.csv")
        df.to_csv(save_path, index=False, encoding="utf-8-sig")

        print(f"\n✅ 저장 완료: {save_path}")
        print(f"📈 총 유니크 데이터: {len(df)}건")

        # ✅ 카테고리별 수집 현황 요약 출력
        print("\n📊 카테고리별 수집 현황:")
        print(df.groupby("카테고리")["url"].count().to_string())

    else:
        print("\n❌ 수집된 데이터가 없습니다.")
