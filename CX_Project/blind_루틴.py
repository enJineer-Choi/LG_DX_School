## 완성은 됐지만, 데이터가 모두 긁어와짐

import pandas as pd
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# 1. 브라우저 및 옵션 설정
chrome_options = Options()
# chrome_options.add_argument("--headless") # 화면 없이 실행하려면 주석 해제
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
# 차단 방지를 위한 User-Agent 설정
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def crawl_blind_final(keyword, limit_count=20):
    search_url = f"https://www.teamblind.com/kr/search/{keyword}"
    data_list = []
    
    try:
        # 1단계: 검색 페이지에서 게시글 링크 수집
        driver.get(search_url)
        print(f"▶ '{keyword}' 검색 결과 페이지 접속 중...")
        time.sleep(5) # 검색 결과가 뜰 때까지 충분히 대기

        # 모든 링크를 가져온 후 중복 제거 (순서 유지)
        raw_links = driver.find_elements(By.CSS_SELECTOR, ".tit a")
        all_urls = [link.get_attribute("href") for link in raw_links]
        unique_urls = list(dict.fromkeys(all_urls))[:limit_count]
        
        print(f"✅ 중복 제거 완료. 총 {len(unique_urls)}개의 본문을 수집합니다.")

        # 2단계: 개별 게시글 접속 및 데이터 추출
        for idx, url in enumerate(unique_urls, 1):
            try:
                driver.get(url)
                wait = WebDriverWait(driver, 12) # 대기 시간을 12초로 조금 더 늘림
                
                # 1. 제목 수집
                title_el = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".article-view-head h2")))
                title = title_el.text.strip()

                # 2. 본문 수집 (강화된 로직)
                content = "본문 수집 실패"
                
                # 본문이 나타날 때까지 기다릴 후보군들 (Blind 실제 구조 반영)
                try:
                    # 후보 1: 클래스 기반 (가장 표준)
                    # 후보 2: data-v 속성을 가진 h2의 형제 요소인 div (캡처 기반)
                    # 후보 3: 모든 article 내 p 태그 수집
                    
                    # 먼저 본문 영역이 로딩될 때까지 기다림
                    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                    time.sleep(2) # 동적 렌더링을 위해 2초 완전 대기

                    # 💡 방법 A: JS를 사용해 '루틴' 제목 바로 아래에 있는 본문 상자를 직접 찾아 텍스트 추출
                    # (클래스명이 바뀌어도 구조가 유지되면 작동함)
                    # 수정된 content_script 부분
                    content_script = """
                        var article = document.querySelector('.article-view-content');
                        if (!article) return null;

                        // 1. 불필요한 요소(광고 상자, 추천 태그, 버튼 등)를 미리 제거
                        var unwanted = article.querySelectorAll('.wrap-info, .tag-list, .ads, button, .article-info');
                        unwanted.forEach(el => el.remove());

                        // 2. 본문 텍스트만 추출
                        // 만약 p 태그들로 나누어져 있다면 그것들만 합치고, 아니면 전체 텍스트를 가져옴
                        var pTags = article.querySelectorAll('p');
                        if (pTags.length > 0) {
                            return Array.from(pTags).map(p => p.innerText).join('\\n').trim();
                        } else {
                            return article.innerText.trim();
                        }
                    """
                    js_content = driver.execute_script(content_script)
                    
                    if js_content and len(js_content.strip()) > 10:
                        content = js_content.strip()
                    else:
                        # 💡 방법 B: 일반적인 태그 탐색
                        for sel in [".article-view-content", "section", ".content-area"]:
                            elements = driver.find_elements(By.CSS_SELECTOR, sel)
                            for el in elements:
                                if len(el.text) > 20: # 최소 20자 이상인 것만 본문으로 인정
                                    content = el.text
                                    break
                            if content != "본문 수집 실패": break

                except Exception as inner_e:
                    pass

                data_list.append({"제목": title, "내용": content, "링크": url})
                status = "✅ 성공" if content != "본문 수집 실패" else "❌ 실패"
                print(f"[{idx}/{len(unique_urls)}] {status}: {title[:15]}...")
                
                time.sleep(2)

            except Exception as e:
                print(f"[{idx}/{len(unique_urls)}] 완전 실패 (URL 확인): {url}")
                continue

        return data_list

    finally:
        driver.quit()

# --- 실행 및 파일 저장 ---
target_keyword = "루틴"
final_results = crawl_blind_final(target_keyword, limit_count=30) # 30개 수집

if final_results:
    df = pd.DataFrame(final_results)
    
    # PermissionError 방지를 위한 타임스탬프 파일명
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"blind_{target_keyword}_{timestamp}.csv"
    
    # 한글 깨짐 방지를 위한 utf-8-sig
    df.to_csv(filename, index=False, encoding="utf-8-sig")
    print("\n" + "="*50)
    print(f"🎉 크롤링 완료! 파일이 생성되었습니다: {filename}")
    print("="*50)
else:
    print("수집된 데이터가 없습니다.")