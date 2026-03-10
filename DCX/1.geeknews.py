from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from urllib.parse import quote
from tqdm import tqdm

# ==============================
# 검색 키워드
# ==============================

keywords = [

    # 기본 AI
    "AI",
    "인공지능",
    "생성형 AI",
    "Generative AI",
    "LLM",
    "GPT",
    "ChatGPT",
    "AI agent",

    # 개발 관련
    "AI 개발",
    "AI 코딩",
    "AI coding",
    "AI programming",
    "AI developer tools",
    "AI coding assistant",
    "AI Copilot",
    "Github Copilot",
    "Cursor AI",

    # 자동화
    "AI 자동화",
    "AI automation",
    "workflow automation",
    "AI workflow",
    "AI agents automation",

    # 생산성
    "AI 생산성",
    "AI productivity",
    "developer productivity",
    "engineering productivity",
    "AI efficiency",
    "AI 효율",

    # 비용 절감
    "AI 비용 절감",
    "AI cost reduction",
    "AI cost saving",
    "AI 인건비 절감",
    "AI cost efficiency",

    # 대체
    "AI 대체",
    "AI replacing jobs",
    "AI replacing developers",
    "AI replacing engineers",

    # 스타트업
    "AI startup",
    "AI 스타트업",
    "AI small team",
    "AI lean startup",
    "AI small company",

    # 소규모 팀
    "small team with AI",
    "AI solo founder",
    "AI one person startup",
    "AI indie hacker",

    # 개발 생산성 사례
    "build startup with AI",
    "vibe coding",
    "AI powered development",
    "AI dev workflow",
    "AI engineering workflow",

    "AI Saas",
    "AI micro startup"

]

driver = wb.Chrome()

all_results = []

# ==============================
# 키워드 반복
# ==============================

for keyword in keywords:

    print(f"\n===== 🔍 키워드: {keyword} =====")

    encoded = quote(keyword)

    search_url = f"https://news.hada.io/search?q={encoded}"

    driver.get(search_url)

    time.sleep(3)

    url_list = []

    # ==========================
    # 페이지 반복 (1~5)
    # ==========================

    for page in range(1,6):

        print(f"   🔎 {page} 페이지")

        time.sleep(2)

        # 스크롤 한번
        scroll = driver.find_element(By.TAG_NAME,"body")
        scroll.send_keys(Keys.END)

        time.sleep(2)

        # URL 수집
        links = driver.find_elements(By.CSS_SELECTOR,"a.gs-title")

        for l in links:

            href = l.get_attribute("href")

            if href:
                url_list.append(href)

        # 마지막 페이지면 종료
        if page == 5:
            break

        # ==========================
        # 다음 페이지 클릭
        # ==========================

        try:

            pages = driver.find_elements(By.CSS_SELECTOR,".gsc-cursor-page")

            pages[page].click()

            time.sleep(3)

        except:
            print("페이지 이동 실패")
            break

    url_list = list(set(url_list))

    print(f"   ✔ URL 수집 완료: {len(url_list)}개")


    # ==============================
    # 기사 내용 수집
    # ==============================

    for link in tqdm(url_list):

        try:

            driver.get(link)

            time.sleep(2)

            title = driver.find_element(By.CSS_SELECTOR,"h1").text

            content = driver.find_element(By.ID,'topic_contents').text

            all_results.append({
                "keyword": keyword,
                "title": title,
                "content": content,
                "url": link
            })

        except:
            continue


driver.quit()

# ==============================
# 저장
# ==============================

df = pd.DataFrame(all_results)

df.to_csv(
    "geeknews_AI_articles.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\n✅ 크롤링 완료")
print("총 기사 수 :", len(df))