import time
import json
import pandas as pd
import random
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# 키워드/분석 사전
KEYWORDS_CARE = {
    "핵심_행위": ["부양", "돌봄", "간호", "부모 돌봄", "부모 부양", "노인 돌봄", "치매 돌봄", "부모님 챙기기"],
    "부정_감정": ["부양 불안", "돌봄 걱정", "부모님 걱정", "부모님 혼자", "아이 걱정", "부담스럽다", "힘들다 부양", "스트레스 부양"],
    "행동_상황": ["부모님 상태 확인", "부모님 전화", "아이 챙기기", "부모님 챙기기", "신경 쓰는다 부모", "혼자 두기 불안"],
    "가족_관계": ["샌드위치 세대", "부모와 자녀", "다세대 가정", "조부모 돌봄", "시어머니 돌봄", "장모님 돌봄"],
    "긍정_기대": ["알아서 돌봄", "자동으로 관리", "안심 가족", "편하게 부양"]
}

KEYWORDS_APPLIANCE = {
    "사용법_일반": ["가전 사용법", "사용법 모르겠다", "가전 설명", "사용법 헷갈린다"],
    "제품별_사용법": ["세탁기 사용법", "냉장고 사용법", "에어컨 사용법", "식기세척기 사용법", "건조기 사용법"],
    "질문_표현": ["어떻게 쓰나요 가전", "순서 가전", "설명서 가전", "가전 사용 순서", "가전 조작법"]
}

ANALYSIS_KEYWORDS = {
    "불안": ["불안", "불안한", "불안해", "불안하다"],
    "걱정": ["걱정", "걱정된", "걱정되다", "걱정스럽"],
    "번거로움": ["번거롭", "번거로운"],
    "귀찮음": ["귀찮", "귀찮은", "귀찮다"],
    "힘들음": ["힘들", "힘든", "힘들다", "힘들어"],
    "부담": ["부담", "부담스럽", "부담되"],
    "스트레스": ["스트레스", "스트레스받"],
    "확인": ["확인", "확인했", "확인하다", "확인해"],
    "전화": ["전화했", "전화하다", "전화해"],
    "챙기기": ["챙기", "챙기다", "챙겼"],
    "알아서": ["알아서"],
    "자동": ["자동으로", "자동", "자동 관리"],
    "안심": ["안심", "안심한", "안심되"],
    "사용법_혼란": ["사용법", "모르겠다", "헷갈린다", "이해안됨", "복잡하다"],
    "도움_요청": ["어떻게 쓰나요", "알려주세요", "설명해주세요", "순서가"]
}

def get_driver():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(options=options)
    return driver

def crawl_naver_content(driver, keyword, where="blog", max_posts=15):
    encoded_keyword = quote(keyword)
    where_param = "blog" if where == "blog" else "article"
    url = f"https://search.naver.com/search.naver?where={where_param}&query={encoded_keyword}"
    results = []
    
    try:
        driver.get(url)
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, 2500);")
        time.sleep(1)
        
        soup = BeautifulSoup(driver.page_source, "html.parser")
        items = soup.find_all(["li", "div"], class_=lambda x: x and ("bx" in x or "view_wrap" in x or "item" in x))
        
        for item in items:
            a_tags = item.find_all("a")
            for a in a_tags:
                title = a.get_text(strip=True)
                link = a.get("href", "")
                if len(title) > 10 and ("blog.naver.com" in link or "cafe.naver.com" in link):
                    results.append({
                        "title": title,
                        "url": link,
                        "snippet": item.get_text(" ", strip=True)[:100],
                        "keyword": keyword
                    })
                    break
            if len(results) >= max_posts:
                break
    except Exception as e:
        print(f" ⚠️ 오류: {e}")
    return results

def run_all_crawling(driver):
    all_results = []
    tasks = [("부양/돌봄", KEYWORDS_CARE), ("가전 사용법", KEYWORDS_APPLIANCE)]
    
    for axis_name, axis_keywords in tasks:
        print(f"\n📌 {axis_name} 시작")
        for category, keywords in axis_keywords.items():
            for kw in keywords:
                # 블로그 크롤링
                b_res = crawl_naver_content(driver, kw, "blog")
                for r in b_res:
                    r.update({"축": axis_name, "카테고리": category, "플랫폼": "블로그"})
                all_results.extend(b_res)
                
                # 카페 크롤링
                c_res = crawl_naver_content(driver, kw, "cafe")
                for r in c_res:
                    r.update({"축": axis_name, "카테고리": category, "플랫폼": "카페"})
                all_results.extend(c_res)
                print(f" 🔍 {kw} -> {len(b_res) + len(c_res)}건")
    return all_results

def analyze_keywords(results):
    texts = [str(r.get("title", "")) + " " + str(r.get("snippet", "")) for r in results]
    full_text = " ".join(texts)
    keyword_counts = {}
    for label, variants in ANALYSIS_KEYWORDS.items():
        count = sum(full_text.count(v) for v in variants)
        keyword_counts[label] = count
    return sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    driver = get_driver()
    try:
        final_results = run_all_crawling(driver)
        if final_results:
            df = pd.DataFrame(final_results)
            df.to_csv("bx_crawling_results.csv", index=False, encoding="utf-8-sig")
            
            care_res = [r for r in final_results if r["축"] == "부양/돌봄"]
            print("\n📊 분석 결과:", analyze_keywords(care_res)[:10])
            print(f"✅ 총 {len(df)}건 저장 완료!")
        else:
            print("\n❌ 여전히 0건입니다. 브라우저 창에서 검색 결과가 보이는지 확인해주세요.")
    finally:
        driver.quit()