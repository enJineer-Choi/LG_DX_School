## blind_ver3.py - 중복 제거 기능 추가본
## EXISTING_CSV에 기존 데이터 파일 경로를 지정하면 이미 수집된 URL은 자동으로 건너뜀

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
TARGET_KEYWORD = "렌탈"
LIMIT_COUNT    = 10000      # 새로 수집할 목표 개수
MAX_SCROLL     = 1000       # 최대 스크롤 횟수
SCROLL_PAUSE   = 2.5

# ★ 핵심: 기존 CSV 파일 경로 지정 → 중복 자동 제거
# 여러 파일을 합치고 싶으면 리스트에 추가
EXISTING_CSVS = [
    "blind_렌탈_최종데이터_1500.csv",   # ← 기존 파일명으로 변경하세요
    # "blind_렌탈_20260301_1200.csv",  # 파일 여러 개도 가능
]


# ════════════════════════════════════════════════
# 기존 URL 로딩
# ════════════════════════════════════════════════
def load_existing_urls(csv_paths: list) -> set:
    """기존 CSV에서 링크 컬럼을 읽어 이미 수집된 URL 집합 반환"""
    seen = set()
    for path in csv_paths:
        try:
            df = pd.read_csv(path, encoding="utf-8-sig")
            if "링크" in df.columns:
                seen.update(df["링크"].dropna().tolist())
                print(f"  ✅ '{path}' 에서 {len(df)}개 URL 로드")
            else:
                print(f"  ⚠️  '{path}' 에 '링크' 컬럼 없음 → 건너뜀")
        except FileNotFoundError:
            print(f"  ⚠️  '{path}' 파일 없음 → 건너뜀")
    print(f"  → 중복 제거 대상: 총 {len(seen)}개 URL\n")
    return seen


# ════════════════════════════════════════════════
# 광고/잡음 라인 제거
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
    if not raw_text or str(raw_text) in ['본문 수집 실패', 'nan']:
        return raw_text
    if '메뉴 더보기' in raw_text:
        raw_text = raw_text.split('메뉴 더보기', 1)[1].strip()
    for p in [r'\n좋아요\n좋아요', r'\n좋아요\n\d+', r'\n공유하기', r'\n댓글을 남겨주세요']:
        m = re.search(p, raw_text)
        if m:
            raw_text = raw_text[:m.start()].strip()
    lines = raw_text.split('\n')
    while lines and (is_ad_line(lines[-1]) or lines[-1].strip() == ''):
        lines.pop()
    return '\n'.join(lines).strip()


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
    options.page_load_strategy = 'eager'
    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )


# ════════════════════════════════════════════════
# URL 수집 - 기존 URL은 건너뜀
# ════════════════════════════════════════════════
def collect_urls(driver, keyword: str, limit: int, max_scroll: int,
                 existing_urls: set) -> list:
    """
    스크롤하며 URL 수집.
    existing_urls에 있는 URL은 이미 수집된 것으로 간주하고 건너뜀.
    limit개의 새로운 URL을 목표로 수집.
    """
    search_url = f"https://www.teamblind.com/kr/search/{keyword}"
    driver.get(search_url)
    print(f"▶ '{keyword}' 검색 페이지 접속...")
    time.sleep(5)

    new_urls   = []   # 새로 수집된 URL (기존에 없는 것)
    seen_urls  = set(existing_urls)  # 중복 체크용 (기존 + 이번 수집분)
    skipped    = 0
    last_height = driver.execute_script("return document.body.scrollHeight")

    for scroll_num in range(1, max_scroll + 1):
        hrefs = driver.execute_script(
            "return Array.from(document.querySelectorAll('.tit a'))"
            ".map(a => a.href).filter(h => h);"
        )
        for href in hrefs:
            if href in seen_urls:
                if href in existing_urls:
                    skipped += 1   # 기존 데이터와 중복
                continue
            seen_urls.add(href)
            new_urls.append(href)

        print(f"  └ 스크롤 {scroll_num}회 | 신규: {len(new_urls)}개 | 중복 건너뜀: {skipped}개")

        if len(new_urls) >= limit:
            print(f"  └ 목표 {limit}개 달성 → 종료")
            break

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print(f"  └ 더 이상 새 게시글 없음 → 종료")
            break
        last_height = new_height

    result = new_urls[:limit]
    print(f"\n✅ 신규 URL {len(result)}개 확보 (중복 {skipped}개 제외)\n")
    return result


# ════════════════════════════════════════════════
# 본문 수집
# ════════════════════════════════════════════════
def scrape_post(driver, url: str) -> dict:
    driver.get(url)
    wait = WebDriverWait(driver, 12)
    title_el = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".article-view-head h2"))
    )
    title = title_el.text.strip()
    time.sleep(2)

    content = "본문 수집 실패"
    js_raw = driver.execute_script(CONTENT_SCRIPT)
    if js_raw and len(js_raw.strip()) > 10:
        content = extract_body_only(js_raw)
    else:
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
# 메인
# ════════════════════════════════════════════════
def crawl_blind(keyword: str, limit_count: int, max_scroll: int,
                existing_csvs: list) -> list:
    # 기존 URL 로드
    print("📂 기존 데이터 로드 중...")
    existing_urls = load_existing_urls(existing_csvs)

    driver = init_driver()
    data_list = []

    try:
        urls = collect_urls(driver, keyword, limit_count, max_scroll, existing_urls)

        for idx, url in enumerate(urls, 1):
            try:
                post = scrape_post(driver, url)
                data_list.append(post)
                status = "✅" if post["내용"] != "본문 수집 실패" else "❌"
                print(f"[{idx:3d}/{len(urls)}] {status} {post['제목'][:35]}...")
                time.sleep(2)
            except Exception as e:
                print(f"[{idx:3d}/{len(urls)}] ❌ 실패: {url}  ({e})")
                continue

    finally:
        driver.quit()

    return data_list


# ════════════════════════════════════════════════
# 실행 & 저장
# ════════════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 55)
    print(f"  블라인드 크롤러 | 키워드: '{TARGET_KEYWORD}'")
    print(f"  신규 목표: {LIMIT_COUNT}개 | 최대 스크롤: {MAX_SCROLL}회")
    print("=" * 55 + "\n")

    results = crawl_blind(TARGET_KEYWORD, LIMIT_COUNT, MAX_SCROLL, EXISTING_CSVS)

    if results:
        df = pd.DataFrame(results)
        success = sum(1 for r in results if r["내용"] != "본문 수집 실패")

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"blind_{TARGET_KEYWORD}_추가수집.csv"
        df.to_csv(filename, index=False, encoding="utf-8-sig")

        print(f"\n{'=' * 55}")
        print(f"  🎉 완료!")
        print(f"  신규 수집: {len(results)}개 | 성공: {success}개 | 실패: {len(results)-success}개")
        print(f"  저장 파일: {filename}")
        print(f"{'=' * 55}")
    else:
        print("수집된 데이터가 없습니다.")