## cook82_crawler.py - 최종본 v5
## Selenium 단일 방식 + urlencode로 URL 안전하게 조립

import pandas as pd
import time
import datetime
import re
from urllib.parse import urlencode
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ════════════════════════════════════════════
# 설정값
# ════════════════════════════════════════════
KEYWORDS   = ["가전 구독", "렌탈"]
MAX_PAGES  = 20
DELAY      = 1.5

NOTICE_NUMS = {"4060855", "3414957", "1945163", "1156646"}
BASE        = "https://www.82cook.com/entiz"


def build_url(php: str, params: dict) -> str:
    """urlencode로 URL 조립 - 한글/특수문자 안전 처리"""
    return f"{BASE}/{php}?" + urlencode(params, encoding="utf-8")


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
    # Chrome 146 + ChromeDriver 버그 workaround
    # missing or invalid columnNumber 에러 방지
    options.page_load_strategy = 'eager'
    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )


# ════════════════════════════════════════════
# 1단계: 목록 수집
# ════════════════════════════════════════════
def get_post_nums(driver, keyword: str, max_pages: int) -> list:
    collected = []
    seen = set()
    print(f"\n>> '{keyword}' 목록 수집 중...")

    for page in range(1, max_pages + 1):
        url = build_url("enti.php", {
            "bn": 15, "searchType": "search",
            "search1": 2, "keys": keyword, "page": page
        })

        try:
            driver.get(url)
            time.sleep(2)

            items = driver.execute_script("""
                var out = [];
                var links = document.querySelectorAll('a[href*="read.php"][href*="searchType"]');
                links.forEach(function(a) {
                    var m = a.href.match(/num=(\\d+)/);
                    var title = a.innerText.trim();
                    if (!m || !title || /^\\d+$/.test(title)) return;
                    out.push({num: m[1], title: title});
                });
                return out;
            """)

            if not items:
                print(f"  {page}p: 없음 -> 종료")
                break

            cnt = 0
            for it in items:
                num   = it["num"]
                title = re.sub(r'\s*\d+\s*$', '', it["title"]).strip()
                if num in NOTICE_NUMS or num in seen or not title:
                    continue
                seen.add(num)
                collected.append((num, title))
                cnt += 1

            print(f"  {page}p: {cnt}개 (누계 {len(collected)})")
            time.sleep(DELAY)

        except Exception as e:
            print(f"  {page}p 오류: {e}")
            continue

    print(f"✅ '{keyword}' {len(collected)}개 확보")
    return collected


# ════════════════════════════════════════════
# 2단계: 본문 수집
# ════════════════════════════════════════════
def scrape_post(driver, num: str, title: str, keyword: str) -> dict:
    url = build_url("read.php", {
        "bn": 15, "num": num,
        "searchType": "search", "search1": 2, "keys": keyword
    })
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        el = wait.until(EC.presence_of_element_located((By.ID, "articleBody")))
        time.sleep(0.8)

        body = el.text.strip()
        if len(body) < 10:
            body = "본문 수집 실패"
        else:
            body = re.sub(r'\n{3,}', '\n\n', body).strip()

        try:
            t = driver.find_element(By.CSS_SELECTOR, "h4.bbstitle").text.strip()
            if t:
                title = t
        except:
            pass

        return {"제목": title, "내용": body, "URL": url}

    except Exception as e:
        return {"제목": title, "내용": f"오류: {str(e)[:60]}", "URL": url}


# ════════════════════════════════════════════
# 메인
# ════════════════════════════════════════════
def crawl_82cook(keywords, max_pages):
    results = []
    driver = init_driver()
    try:
        for kw in keywords:
            posts = get_post_nums(driver, kw, max_pages)
            print(f"\n📄 '{kw}' 본문 수집 ({len(posts)}개)")
            print("-" * 55)
            for i, (num, title) in enumerate(posts, 1):
                r = scrape_post(driver, num, title, kw)
                r["키워드"] = kw
                results.append(r)
                ok = r["내용"] != "본문 수집 실패" and "오류:" not in r["내용"]
                preview = r["내용"][:35].replace("\n", " ")
                print(f"  [{i:3d}/{len(posts)}] {'✅' if ok else '❌'} {title[:22]:<22} | {preview}")
                time.sleep(DELAY)
    finally:
        driver.quit()
    return results


if __name__ == "__main__":
    print("=" * 55)
    print(f"  82cook 크롤러  키워드: {KEYWORDS}")
    print("=" * 55)

    results = crawl_82cook(KEYWORDS, MAX_PAGES)

    if results:
        df = pd.DataFrame(results)[["키워드", "제목", "내용", "URL"]]
        ok_cnt = sum(1 for r in results
                     if r["내용"] != "본문 수집 실패" and "오류:" not in r["내용"])
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        fname = f"82cook_{ts}.csv"
        df.to_csv(fname, index=False, encoding="utf-8-sig")
        print(f"\n🎉 완료! 성공 {ok_cnt}/{len(results)}개  파일: {fname}")
    else:
        print("수집된 데이터가 없습니다.")