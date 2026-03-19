## blind_ver3.py - 스크롤 + 본문 정제 완성본

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
# ⚙️  설정값 (여기만 바꾸면 됩니다)
# ════════════════════════════════════════════════
TARGET_KEYWORD = "렌탈"   # 검색 키워드
LIMIT_COUNT    = 1500       # 수집할 게시글 수 (스크롤로 더 모을 수 있음)
MAX_SCROLL     = 100       # 검색결과 페이지 최대 스크롤 횟수
SCROLL_PAUSE   = 2.5      # 스크롤 후 대기 시간(초) - 너무 짧으면 차단 위험


# ════════════════════════════════════════════════
# 광고/잡음 라인 제거 패턴
# ════════════════════════════════════════════════
AD_LINE_PATTERNS = [
    r'^쿠팡에서', r'^공식 APPLE 브랜드관에서', r'^가연 이상형',
    r'^와우회원', r'^매일 아침 7시', r'^직장인 맞춤 DB',
    r'^오늘 주문하면', r'^공기청정살균기', r'^와우 멤버십',
    r'^가장 빠르게 만나는', r'^블라인드 타로', r'셀소해봅니다',
    r'by 블라인드가 만든', r'^직장인끼리 소개팅', r'렌탈0원',
    r'\(광고\)', r'^tag [가-힣A-Za-z]', r'^매일 오전 7시',
    r'특가를 살펴보세요', r'쿠팡 특가로', r'로켓프레시',
    r'골드박스', r'블릿 셀소', r'이달의 신상호텔',
]

def is_ad_line(line: str) -> bool:
    return any(re.search(p, line.strip()) for p in AD_LINE_PATTERNS)

def extract_body_only(raw_text: str) -> str:
    """
    전체 페이지 텍스트에서 실제 본문만 추출
    구조: [채널·메타] → 메뉴 더보기 → [본문] → [광고] → 좋아요/댓글 → [추천글]
    """
    if not raw_text or str(raw_text) in ['본문 수집 실패', 'nan']:
        return raw_text

    # 1단계: '메뉴 더보기' 앞 메타 영역 제거
    if '메뉴 더보기' in raw_text:
        raw_text = raw_text.split('메뉴 더보기', 1)[1].strip()

    # 2단계: 인터랙션 버튼 영역(좋아요/공유/댓글) 이후 제거
    for p in [r'\n좋아요\n좋아요', r'\n좋아요\n\d+', r'\n공유하기', r'\n댓글을 남겨주세요']:
        m = re.search(p, raw_text)
        if m:
            raw_text = raw_text[:m.start()].strip()

    # 3단계: 끝에서부터 광고 라인 제거
    lines = raw_text.split('\n')
    while lines and (is_ad_line(lines[-1]) or lines[-1].strip() == ''):
        lines.pop()

    return '\n'.join(lines).strip()


# ════════════════════════════════════════════════
# JS: DOM에서 본문 영역만 추출
# ════════════════════════════════════════════════
CONTENT_SCRIPT = """
    var article = document.querySelector('.article-view-content');
    if (!article) return null;
    var clone = article.cloneNode(true);
    var removeSelectors = [
        '[class*="channel"]', '[class*="article-info"]', '[class*="wrap-info"]',
        '[class*="meta"]', '[class*="tag-list"]', '[class*="tags"]',
        '[class*="ads"]', '[class*="ad-"]', '[class*="banner"]', '[class*="promo"]',
        '[class*="like"]', '[class*="comment"]', '[class*="share"]', '[class*="action"]',
        '[class*="recommend"]', '[class*="related"]', '[class*="topic"]',
        'button', 'iframe', 'script', 'style', 'nav'
    ];
    removeSelectors.forEach(function(sel) {
        try { clone.querySelectorAll(sel).forEach(function(el) { el.remove(); }); }
        catch(e) {}
    });
    return clone.innerText.trim() || null;
"""


# ════════════════════════════════════════════════
# 브라우저 초기화
# ════════════════════════════════════════════════
def init_driver():
    options = Options()
    # options.add_argument("--headless")  # 백그라운드 실행 원하면 주석 해제
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
# 핵심 함수 ① : 검색결과 페이지 스크롤하며 URL 수집
# ════════════════════════════════════════════════
def collect_urls(driver, keyword: str, limit: int, max_scroll: int) -> list:
    """
    검색결과 페이지를 스크롤하면서 limit 개수만큼 URL 수집.
    Blind는 무한스크롤 방식이라 스크롤해야 추가 게시글이 로드됨.
    """
    url = f"https://www.teamblind.com/kr/search/{keyword}"
    driver.get(url)
    print(f"▶ '{keyword}' 검색 페이지 접속...")
    time.sleep(5)

    collected = []
    last_height = driver.execute_script("return document.body.scrollHeight")

    for scroll_num in range(1, max_scroll + 1):
        # JS로 href를 한번에 문자열 리스트로 추출
        # → 스크롤 후 DOM 리렌더링으로 인한 StaleElementReferenceException 방지
        hrefs = driver.execute_script(
            "return Array.from(document.querySelectorAll('.tit a'))"
            ".map(a => a.href).filter(h => h);"
        )
        for href in hrefs:
            if href not in collected:
                collected.append(href)

        # 목표 개수 달성 시 조기 종료
        if len(collected) >= limit:
            print(f"  └ 목표 {limit}개 달성 → 스크롤 종료")
            break

        # 페이지 맨 아래로 스크롤
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE)

        # 새 콘텐츠가 로드됐는지 확인
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print(f"  └ 스크롤 {scroll_num}회: 더 이상 새 게시글 없음 → 종료")
            break
        last_height = new_height
        print(f"  └ 스크롤 {scroll_num}회 완료 | 수집된 URL: {len(collected)}개")

    unique_urls = list(dict.fromkeys(collected))[:limit]
    print(f"\n✅ 총 {len(unique_urls)}개 URL 확보\n")
    return unique_urls


# ════════════════════════════════════════════════
# 핵심 함수 ② : 개별 게시글에서 본문 수집
# ════════════════════════════════════════════════
def scrape_post(driver, url: str) -> dict:
    """게시글 페이지에서 제목 + 본문만 추출"""
    driver.get(url)
    wait = WebDriverWait(driver, 12)

    # 제목 로딩 대기
    title_el = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".article-view-head h2"))
    )
    title = title_el.text.strip()
    time.sleep(2)

    # JS로 본문 DOM 추출
    content = "본문 수집 실패"
    js_raw = driver.execute_script(CONTENT_SCRIPT)

    if js_raw and len(js_raw.strip()) > 10:
        content = extract_body_only(js_raw)
    else:
        # 폴백: CSS 셀렉터 직접 탐색
        for sel in [".article-view-content", "section", ".content-area"]:
            els = driver.find_elements(By.CSS_SELECTOR, sel)
            for el in els:
                if len(el.text) > 20:
                    content = extract_body_only(el.text)
                    break
            if content != "본문 수집 실패":
                break

    return {"제목": title, "내용": content, "링크": url}


# ════════════════════════════════════════════════
# 메인 크롤러
# ════════════════════════════════════════════════
def crawl_blind(keyword: str, limit_count: int, max_scroll: int) -> list:
    driver = init_driver()
    data_list = []

    try:
        # 1단계: URL 수집 (스크롤 포함)
        urls = collect_urls(driver, keyword, limit_count, max_scroll)

        # 2단계: 각 게시글 본문 수집
        for idx, url in enumerate(urls, 1):
            try:
                post = scrape_post(driver, url)
                data_list.append(post)
                status = "✅" if post["내용"] != "본문 수집 실패" else "❌"
                print(f"[{idx:2d}/{len(urls)}] {status} {post['제목'][:35]}...")
                time.sleep(2)   # 서버 부하 방지
            except Exception as e:
                print(f"[{idx:2d}/{len(urls)}] ❌ 실패: {url}  ({e})")
                continue

    finally:
        driver.quit()

    return data_list


# ════════════════════════════════════════════════
# 실행 & 저장
# ════════════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 55)
    print(f"  블라인드 크롤러 시작 | 키워드: '{TARGET_KEYWORD}'")
    print(f"  목표: {LIMIT_COUNT}개 | 최대 스크롤: {MAX_SCROLL}회")
    print("=" * 55 + "\n")

    results = crawl_blind(TARGET_KEYWORD, LIMIT_COUNT, MAX_SCROLL)

    if results:
        df = pd.DataFrame(results)
        success = sum(1 for r in results if r["내용"] != "본문 수집 실패")

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"blind_{TARGET_KEYWORD}_{timestamp}.csv"
        df.to_csv(filename, index=False, encoding="utf-8-sig")

        print(f"\n{'=' * 55}")
        print(f"  🎉 크롤링 완료!")
        print(f"  수집: {len(results)}개 | 본문 성공: {success}개 | 실패: {len(results)-success}개")
        print(f"  저장 파일: {filename}")
        print(f"{'=' * 55}")
    else:
        print("수집된 데이터가 없습니다.")