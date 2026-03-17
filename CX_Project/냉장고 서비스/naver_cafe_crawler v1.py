"""
똑똑(Knock) 푸드 매니저 - CX 프로젝트 크롤러
네이버 블로그 / 카페 크롤링
"""

import time
import random
import json
import csv
from datetime import datetime
from dataclasses import dataclass, field, asdict
from typing import Optional

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


# ──────────────────────────────────────────────
# 1. 키워드 설정 (Pain Point 3축 기반)
# ──────────────────────────────────────────────

KEYWORDS = {
    "과잉구매": [
        "냉장고 중복구매",
        "장보기 실패",
        "마트 또 샀다",
        "냉장고 같은거 두개",
    ],
    "반복폐기": [
        "냉장고 또 버렸다",
        "식재료 유통기한",
        "냉장고 파먹기",
        "음식 아깝다 버렸다",
    ],
    "소비패턴인지실패": [
        "냉장고 재고 파악",
        "1인가구 식재료 관리",
        "자취 냉장고 정리",
        "냉장고 뭐있는지",
    ],
}

# ──────────────────────────────────────────────
# 2. 데이터 구조
# ──────────────────────────────────────────────

@dataclass
class CrawledPost:
    source: str           # blog / cafe
    keyword_axis: str     # 과잉구매 / 반복폐기 / 소비패턴인지실패
    keyword: str          # 실제 검색 키워드
    title: str
    content_preview: str  # 본문 앞 300자
    url: str
    crawled_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# ──────────────────────────────────────────────
# 3. 드라이버 초기화
# ──────────────────────────────────────────────

def init_driver(headless: bool = True) -> webdriver.Chrome:
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,900")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
    driver = webdriver.Chrome(options=options)
    return driver


# ──────────────────────────────────────────────
# 4. 네이버 블로그 크롤러
# ──────────────────────────────────────────────

def crawl_naver_blog(driver, keyword: str, axis: str, max_posts: int = 10) -> list[CrawledPost]:
    results = []
    search_url = f"https://search.naver.com/search.naver?where=blog&query={keyword}&sm=tab_opt&nso=so%3Add%2Cp%3A1y"

    print(f"  [블로그] 검색: '{keyword}'")
    driver.get(search_url)
    time.sleep(random.uniform(2, 3))

    try:
        # 검색 결과 카드 목록
        posts = driver.find_elements(By.CSS_SELECTOR, "li.bx")[:max_posts]

        for post in posts:
            try:
                title_el = post.find_element(By.CSS_SELECTOR, "a.title_link")
                desc_el = post.find_element(By.CSS_SELECTOR, "a.dsc_link")

                title = title_el.text.strip()
                content_preview = desc_el.text.strip()[:300]
                url = title_el.get_attribute("href")

                if title and url:
                    results.append(CrawledPost(
                        source="blog",
                        keyword_axis=axis,
                        keyword=keyword,
                        title=title,
                        content_preview=content_preview,
                        url=url,
                    ))
            except NoSuchElementException:
                continue

    except Exception as e:
        print(f"    ⚠ 블로그 크롤링 오류: {e}")

    print(f"    → {len(results)}건 수집")
    return results


# ──────────────────────────────────────────────
# 5. 네이버 카페 크롤러
# ──────────────────────────────────────────────

def crawl_naver_cafe(driver, keyword: str, axis: str, max_posts: int = 10) -> list[CrawledPost]:
    results = []
    search_url = f"https://search.naver.com/search.naver?where=cafeblog&query={keyword}&sm=tab_opt&nso=so%3Add%2Cp%3A1y"

    print(f"  [카페] 검색: '{keyword}'")
    driver.get(search_url)
    time.sleep(random.uniform(2, 3))

    try:
        posts = driver.find_elements(By.CSS_SELECTOR, "li.bx")[:max_posts]

        for post in posts:
            try:
                title_el = post.find_element(By.CSS_SELECTOR, "a.title_link")
                desc_el  = post.find_element(By.CSS_SELECTOR, "a.dsc_link")

                title = title_el.text.strip()
                content_preview = desc_el.text.strip()[:300]
                url = title_el.get_attribute("href")

                if title and url:
                    results.append(CrawledPost(
                        source="cafe",
                        keyword_axis=axis,
                        keyword=keyword,
                        title=title,
                        content_preview=content_preview,
                        url=url,
                    ))
            except NoSuchElementException:
                continue

    except Exception as e:
        print(f"    ⚠ 카페 크롤링 오류: {e}")

    print(f"    → {len(results)}건 수집")
    return results


# ──────────────────────────────────────────────
# 6. 저장 함수
# ──────────────────────────────────────────────

def save_results(results: list[CrawledPost], filename_prefix: str = "knock_cx"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")

    # JSON 저장
    json_path = f"{filename_prefix}_{timestamp}.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump([asdict(r) for r in results], f, ensure_ascii=False, indent=2)

    # CSV 저장 (클러스터링 작업용)
    csv_path = f"{filename_prefix}_{timestamp}.csv"
    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=asdict(results[0]).keys())
        writer.writeheader()
        writer.writerows([asdict(r) for r in results])

    print(f"\n✅ 저장 완료")
    print(f"   JSON → {json_path}")
    print(f"   CSV  → {csv_path}")
    return json_path, csv_path


# ──────────────────────────────────────────────
# 7. 메인 실행
# ──────────────────────────────────────────────

def main():
    MAX_POSTS_PER_KEYWORD = 10   # 키워드당 수집 수 (조절 가능)
    HEADLESS = True              # False로 바꾸면 브라우저 직접 확인 가능

    print("=" * 50)
    print("  똑똑 푸드 매니저 - CX 크롤러 시작")
    print("=" * 50)

    driver = init_driver(headless=HEADLESS)
    all_results: list[CrawledPost] = []

    try:
        for axis, keywords in KEYWORDS.items():
            print(f"\n📌 축: [{axis}]")
            for kw in keywords:
                # 블로그
                blog_results = crawl_naver_blog(driver, kw, axis, MAX_POSTS_PER_KEYWORD)
                all_results.extend(blog_results)
                time.sleep(random.uniform(1.5, 2.5))

                # 카페
                cafe_results = crawl_naver_cafe(driver, kw, axis, MAX_POSTS_PER_KEYWORD)
                all_results.extend(cafe_results)
                time.sleep(random.uniform(1.5, 2.5))

    finally:
        driver.quit()

    print(f"\n총 수집: {len(all_results)}건")

    if all_results:
        save_results(all_results)
    else:
        print("⚠ 수집된 데이터가 없습니다.")


if __name__ == "__main__":
    main()
