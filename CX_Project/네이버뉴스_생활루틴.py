## naver_news_crawler.py
## 네이버 뉴스 크롤러 - "생활루틴", "생활패턴" 키워드
## 전략: 네이버 뷰어 우선 + 언론사 원본 다중 셀렉터 폴백

import pandas as pd
import time
import datetime
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ════════════════════════════════════════════════
# ⚙️  설정값
# ════════════════════════════════════════════════
KEYWORDS    = ["생활루틴", "생활패턴"]   # 검색 키워드 목록
LIMIT_COUNT = 100                         # 키워드당 수집할 기사 수
MAX_SCROLL  = 30                          # 검색결과 최대 스크롤 횟수
SCROLL_PAUSE = 2.0                        # 스크롤 대기 시간(초)


# ════════════════════════════════════════════════
# 네이버 뷰어 기사 본문 셀렉터 (우선순위 순)
# ════════════════════════════════════════════════
NAVER_SELECTORS = [
    "#dic_area",            # 대부분의 네이버 뉴스
    "#newsct_article",      # 일부 네이버 뉴스
    "#articeBody",          # 구형 네이버 뉴스
    ".go_trans",            # 번역 가능 기사
]

# ════════════════════════════════════════════════
# 언론사 원본 기사 본문 셀렉터 (사이트별 패턴 모음)
# ════════════════════════════════════════════════
PUBLISHER_SELECTORS = [
    # 공통 시맨틱 태그
    "article",
    "[role='main']",
    "main",

    # 주요 언론사별
    ".article_body",        # 조선일보, 동아일보 계열
    ".article-body",
    ".article_txt",         # 중앙일보
    ".article-content",
    ".news_content",        # 한국경제
    ".news-article-body",
    "#articleBody",         # 연합뉴스, 머니투데이
    "#article-view-content-div",
    "#articleBodyContents", # 한겨레
    "#content-article",
    ".view_con_tx",         # 이데일리
    ".news_view",
    ".newsct_article",
    "#newsEndContents",     # SBS, MBC 등 방송사
    ".article_view",
    ".reporter_view",
    ".news_body",
    ".post-body",
    ".entry-content",

    # 최후 폴백: p 태그 집합
    "p",
]


# ════════════════════════════════════════════════
# 브라우저 초기화
# ════════════════════════════════════════════════
def init_driver():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,900")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    )
    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )


# ════════════════════════════════════════════════
# URL 수집: 검색결과 스크롤하며 뉴스 링크 모으기
# ════════════════════════════════════════════════
def debug_page_structure(driver):
    """수집이 안 될 때 실제 페이지 구조를 출력해서 셀렉터 확인용"""
    info = driver.execute_script("""
        var allClasses = new Set();
        document.querySelectorAll('[class]').forEach(function(el) {
            el.className.split(' ').forEach(function(c) {
                if (c && (c.includes('news') || c.includes('article')
                    || c.includes('item') || c.includes('list')
                    || c.includes('result') || c.includes('tit'))) {
                    allClasses.add(el.tagName.toLowerCase() + '.' + c);
                }
            });
        });
        return Array.from(allClasses).slice(0, 40);
    """)
    print("\n  [DEBUG] 페이지에서 발견된 뉴스 관련 클래스:")
    for c in info:
        print(f"    {c}")


def collect_news_urls(driver, keyword: str, limit: int, max_scroll: int) -> list:
    """
    네이버 뉴스 검색결과를 스크롤하며 기사 URL 수집.
    - 네이버가 구조를 자주 바꾸므로 다중 셀렉터 전략 사용
    - 네이버 뷰어 URL (news.naver.com) 우선, 없으면 언론사 원본
    """
    search_url = (
        f"https://search.naver.com/search.naver"
        f"?where=news&query={keyword}&sm=tab_opt&sort=0"
    )
    driver.get(search_url)
    print(f"\n▶ '{keyword}' 뉴스 검색 중...")
    time.sleep(3)

    collected = []
    last_height = driver.execute_script("return document.body.scrollHeight")

    # ── 뉴스 카드 탐색 JS: 여러 셀렉터를 순서대로 시도 ──
    # 네이버가 구조를 변경해도 하나는 걸리도록 폭넓게 설정
    EXTRACT_JS = """
        var results = [];
        var seen = new Set();

        // 시도할 (카드 셀렉터, 제목 셀렉터) 조합 목록
        var strategies = [
            // 2024~2025 네이버 구조
            ['.news_area',          'a.news_tit'],
            ['.news_wrap',          'a.news_tit'],
            ['.news_wrap',          'a[class*="tit"]'],
            // 구형 구조
            ['.newsct_item',        'a.news_tit'],
            ['.bx',                 'a.news_tit'],
            // 최신 구조 (클래스명이 해시로 바뀐 경우 대비)
            ['[data-cr-r]',         'a[href*="news"]'],
            // 폴백: 링크만 직접 수집
            [null,                  'a[href*="news.naver.com/article"]'],
            [null,                  'a[href*="n.news.naver.com"]'],
        ];

        for (var s = 0; s < strategies.length; s++) {
            var cardSel = strategies[s][0];
            var titleSel = strategies[s][1];

            if (cardSel) {
                var cards = document.querySelectorAll(cardSel);
                cards.forEach(function(card) {
                    var titleEl = card.querySelector(titleSel);
                    if (!titleEl) return;
                    var title = titleEl.innerText.trim();
                    var origUrl = titleEl.href;
                    var naverLink = card.querySelector('a[href*="news.naver.com"]');
                    var url = naverLink ? naverLink.href : origUrl;
                    if (title && url && !seen.has(url)) {
                        seen.add(url);
                        results.push({title: title, url: url});
                    }
                });
            } else {
                // 카드 없이 링크만 직접 수집
                var links = document.querySelectorAll(titleSel);
                links.forEach(function(a) {
                    var url = a.href;
                    var title = a.innerText.trim() || a.title || '';
                    if (url && !seen.has(url)) {
                        seen.add(url);
                        results.push({title: title, url: url});
                    }
                });
            }

            if (results.length > 0) break;  // 하나라도 찾으면 중단
        }
        return results;
    """

    first_run_debug = True  # 첫 스크롤에서만 디버그 출력

    for scroll_num in range(1, max_scroll + 1):
        items = driver.execute_script(EXTRACT_JS)

        if first_run_debug and len(items) == 0:
            debug_page_structure(driver)
            first_run_debug = False

        for item in items:
            url = item.get("url", "")
            title = item.get("title", "")
            if url and url not in [c[0] for c in collected]:
                collected.append((url, title))

        if len(collected) >= limit:
            print(f"  └ 목표 {limit}개 달성 → 스크롤 종료")
            break

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print(f"  └ 스크롤 {scroll_num}회: 더 이상 기사 없음 → 종료")
            break
        last_height = new_height
        print(f"  └ 스크롤 {scroll_num}회 | 수집 URL: {len(collected)}개")

    result = collected[:limit]
    print(f"✅ '{keyword}' 총 {len(result)}개 URL 확보")
    return result


# ════════════════════════════════════════════════
# 본문 추출: 네이버 뷰어 → 언론사 원본 폴백
# ════════════════════════════════════════════════
def extract_content(driver) -> str:
    """
    현재 페이지에서 본문 추출.
    1순위: 네이버 뷰어 셀렉터
    2순위: 언론사별 셀렉터 목록 순차 시도
    3순위: p 태그 전체 합치기
    """
    current_url = driver.current_url

    # ── 1순위: 네이버 뷰어 ──
    if "news.naver.com" in current_url:
        for sel in NAVER_SELECTORS:
            try:
                el = driver.find_element(By.CSS_SELECTOR, sel)
                text = el.text.strip()
                if len(text) > 50:
                    return clean_text(text)
            except:
                continue

    # ── 2순위: 언론사 원본 셀렉터 ──
    for sel in PUBLISHER_SELECTORS:
        try:
            if sel == "p":
                # p 태그 여러 개를 합쳐서 판단
                els = driver.find_elements(By.CSS_SELECTOR, "p")
                combined = "\n".join(
                    e.text.strip() for e in els if len(e.text.strip()) > 20
                )
                if len(combined) > 100:
                    return clean_text(combined)
            else:
                el = driver.find_element(By.CSS_SELECTOR, sel)
                text = el.text.strip()
                if len(text) > 100:
                    return clean_text(text)
        except:
            continue

    # ── 3순위: body 전체에서 텍스트 추출 (최후 수단) ──
    try:
        body_text = driver.find_element(By.TAG_NAME, "body").text
        if len(body_text) > 200:
            return clean_text(body_text[:3000])  # 너무 길면 앞부분만
    except:
        pass

    return "본문 수집 실패"


def clean_text(text: str) -> str:
    """광고·공백·특수문자 정리"""
    # 연속 개행 정리
    text = re.sub(r'\n{3,}', '\n\n', text)
    # 광고성 문구 제거
    ad_patterns = [
        r'.*구독.*\n?', r'.*뉴스레터.*\n?', r'.*광고.*\n?',
        r'.*저작권.*\n?', r'.*무단.*전재.*\n?', r'.*재배포.*\n?',
        r'\[.*?\]',      # [기자명], [편집자주] 등
    ]
    for p in ad_patterns:
        text = re.sub(p, '', text)
    return text.strip()


# ════════════════════════════════════════════════
# 개별 기사 크롤링
# ════════════════════════════════════════════════
def scrape_article(driver, url: str, title: str) -> dict:
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(1.5)

        # 실제 기사 제목 재추출 시도 (검색결과보다 정확)
        for sel in ["h2.media_end_head_headline", "h3#articleTitle",
                    "h1.tit", "h1", ".article_head .title", ".news_headline"]:
            try:
                t = driver.find_element(By.CSS_SELECTOR, sel).text.strip()
                if t:
                    title = t
                    break
            except:
                continue

        content = extract_content(driver)
        return {
            "제목": title,
            "내용": content,
            "URL": url,
            "도메인": re.sub(r'https?://(www\.)?', '', url).split('/')[0],
        }
    except Exception as e:
        return {"제목": title, "내용": "본문 수집 실패", "URL": url, "도메인": ""}


# ════════════════════════════════════════════════
# 메인
# ════════════════════════════════════════════════
def crawl_naver_news(keywords: list, limit: int, max_scroll: int) -> list:
    driver = init_driver()
    all_results = []

    try:
        for keyword in keywords:
            url_list = collect_news_urls(driver, keyword, limit, max_scroll)
            print(f"\n📰 '{keyword}' 기사 본문 수집 시작...\n")

            for idx, (url, title) in enumerate(url_list, 1):
                result = scrape_article(driver, url, title)
                result["키워드"] = keyword
                all_results.append(result)

                status = "✅" if result["내용"] != "본문 수집 실패" else "❌"
                domain = result.get("도메인", "")
                print(f"  [{idx:3d}/{len(url_list)}] {status} [{domain}] {result['제목'][:30]}...")
                time.sleep(1.5)

    finally:
        driver.quit()

    return all_results


# ════════════════════════════════════════════════
# 실행 & 저장
# ════════════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 60)
    print(f"  네이버 뉴스 크롤러 시작")
    print(f"  키워드: {KEYWORDS}")
    print(f"  키워드당 목표: {LIMIT_COUNT}개 | 최대 스크롤: {MAX_SCROLL}회")
    print("=" * 60)

    results = crawl_naver_news(KEYWORDS, LIMIT_COUNT, MAX_SCROLL)

    if results:
        df = pd.DataFrame(results)[["키워드", "제목", "내용", "도메인", "URL"]]
        success = sum(1 for r in results if r["내용"] != "본문 수집 실패")

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"naver_news_생활루틴패턴_{timestamp}.csv"
        df.to_csv(filename, index=False, encoding="utf-8-sig")

        print(f"\n{'=' * 60}")
        print(f"  🎉 완료!")
        print(f"  총 수집: {len(results)}개")
        print(f"  본문 성공: {success}개 / 실패: {len(results) - success}개")
        print(f"  저장 파일: {filename}")
        print(f"{'=' * 60}")
    else:
        print("수집된 데이터가 없습니다.")