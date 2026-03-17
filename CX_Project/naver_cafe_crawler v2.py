"""
똑똑(Knock) 푸드 매니저 - CX 프로젝트
네이버 카페 전용 다중 페이지 크롤러 v2
"""

import time
import random
import json
import csv
from datetime import datetime
from dataclasses import dataclass, field, asdict

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager


# ──────────────────────────────────────────────
# 1. 키워드 설정 (Pain Point 3축)
# ──────────────────────────────────────────────

KEYWORDS = {
    "과잉구매": [
        "냉장고 중복구매",
        "장보기 실패",
        "마트 또 샀다",
        "냉장고 같은거 두개",
        "냉장고 확인 장보기",
    ],
    "반복폐기": [
        "냉장고 또 버렸다",
        "식재료 유통기한",
        "냉장고 파먹기",
        "음식 아깝다 버렸다",
        "식재료 썩었다",
    ],
    "소비패턴인지실패": [
        "냉장고 재고 파악",
        "1인가구 식재료 관리",
        "자취 냉장고 정리",
        "냉장고 뭐있는지",
        "소량 식재료 구매",
    ],
}

# ──────────────────────────────────────────────
# 2. 설정값
# ──────────────────────────────────────────────

MAX_PAGES = 5          # 키워드당 크롤링할 페이지 수 (1페이지 = 약 10건)
HEADLESS = False       # True: 브라우저 숨김 / False: 브라우저 직접 확인
DELAY_MIN = 1.5        # 요청 간 최소 딜레이 (초)
DELAY_MAX = 2.5        # 요청 간 최대 딜레이 (초)


# ──────────────────────────────────────────────
# 3. 데이터 구조
# ──────────────────────────────────────────────

@dataclass
class CrawledPost:
    source: str           # cafe
    keyword_axis: str     # 과잉구매 / 반복폐기 / 소비패턴인지실패
    keyword: str          # 실제 검색 키워드
    title: str
    content_preview: str  # 본문 미리보기
    cafe_name: str        # 카페 이름
    url: str
    crawled_at: str = field(
        default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )


# ──────────────────────────────────────────────
# 4. 드라이버 초기화
# ──────────────────────────────────────────────

def init_driver() -> webdriver.Chrome:
    options = Options()
    if HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,900")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver


# ──────────────────────────────────────────────
# 5. 네이버 카페 다중 페이지 크롤러
# ──────────────────────────────────────────────

def crawl_naver_cafe_multipage(
    driver, keyword: str, axis: str, max_pages: int = MAX_PAGES
) -> list[CrawledPost]:

    results = []
    seen_urls = set()  # 중복 URL 방지

    for page in range(1, max_pages + 1):
        start = (page - 1) * 10 + 1
        url = (
            f"https://search.naver.com/search.naver?"
            f"where=cafeblog&query={keyword}"
            f"&sm=tab_opt&nso=so%3Add%2Cp%3A1y"  # 최신순, 1년 이내
            f"&start={start}"
        )

        print(f"  [{axis}] '{keyword}' - {page}페이지 수집 중...")
        driver.get(url)
        time.sleep(random.uniform(DELAY_MIN, DELAY_MAX))

        # 카페 탭 클릭 (검색 결과가 블로그로 넘어가는 경우 방지)
        try:
            cafe_tab = driver.find_elements(By.CSS_SELECTOR, "a.tab")
            for tab in cafe_tab:
                if "카페" in tab.text:
                    tab.click()
                    time.sleep(1)
                    break
        except Exception:
            pass

        # 게시글 수집
        posts = driver.find_elements(By.CSS_SELECTOR, "li.bx")

        if not posts:
            print(f"    → {page}페이지 결과 없음, 종료")
            break

        page_count = 0
        for post in posts:
            try:
                title_el = post.find_element(By.CSS_SELECTOR, "a.title_link")
                title = title_el.text.strip()
                post_url = title_el.get_attribute("href")

                # 중복 제거
                if not title or not post_url or post_url in seen_urls:
                    continue
                seen_urls.add(post_url)

                # 본문 미리보기
                try:
                    desc_el = post.find_element(By.CSS_SELECTOR, "a.dsc_link")
                    content_preview = desc_el.text.strip()[:300]
                except NoSuchElementException:
                    content_preview = ""

                # 카페 이름
                try:
                    cafe_el = post.find_element(By.CSS_SELECTOR, "a.sub_txt.cafe_name")
                    cafe_name = cafe_el.text.strip()
                except NoSuchElementException:
                    cafe_name = "알 수 없음"

                results.append(CrawledPost(
                    source="cafe",
                    keyword_axis=axis,
                    keyword=keyword,
                    title=title,
                    content_preview=content_preview,
                    cafe_name=cafe_name,
                    url=post_url,
                ))
                page_count += 1

            except NoSuchElementException:
                continue

        print(f"    → {page}페이지: {page_count}건 수집 (누적 {len(results)}건)")

    return results


# ──────────────────────────────────────────────
# 6. 저장 함수
# ──────────────────────────────────────────────

def save_results(results: list[CrawledPost]):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    prefix = f"knock_cafe_{timestamp}"

    # JSON
    json_path = f"{prefix}.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump([asdict(r) for r in results], f, ensure_ascii=False, indent=2)

    # CSV (클러스터링용)
    csv_path = f"{prefix}.csv"
    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=asdict(results[0]).keys())
        writer.writeheader()
        writer.writerows([asdict(r) for r in results])

    print(f"\n✅ 저장 완료")
    print(f"   JSON → {json_path}")
    print(f"   CSV  → {csv_path}")
    print(f"   총 {len(results)}건")

    # 축별 통계 출력
    print("\n📊 축별 수집 현황:")
    axis_counts = {}
    for r in results:
        axis_counts[r.keyword_axis] = axis_counts.get(r.keyword_axis, 0) + 1
    for axis, count in axis_counts.items():
        print(f"   {axis}: {count}건")


# ──────────────────────────────────────────────
# 7. 메인 실행
# ──────────────────────────────────────────────

def main():
    print("=" * 55)
    print("  똑똑 푸드 매니저 - 네이버 카페 크롤러 v2")
    print(f"  키워드당 최대 {MAX_PAGES}페이지 수집")
    print("=" * 55)

    driver = init_driver()
    all_results: list[CrawledPost] = []

    try:
        for axis, keywords in KEYWORDS.items():
            print(f"\n{'='*40}")
            print(f"📌 [{axis}] 축 시작")
            print(f"{'='*40}")

            for kw in keywords:
                posts = crawl_naver_cafe_multipage(driver, kw, axis)
                all_results.extend(posts)
                time.sleep(random.uniform(DELAY_MIN, DELAY_MAX))

    finally:
        driver.quit()

    print(f"\n{'='*55}")
    print(f"  크롤링 완료 - 총 {len(all_results)}건 수집")
    print(f"{'='*55}")

    if all_results:
        save_results(all_results)
    else:
        print("⚠ 수집된 데이터가 없습니다.")


if __name__ == "__main__":
    main()
