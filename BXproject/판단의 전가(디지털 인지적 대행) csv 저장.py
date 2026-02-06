import time
import pandas as pd
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# 1. 키워드 대확장 (가족 호칭 + 구체적 상황 + 감정 조합)
# 1. 키워드 무한 확장 (행동 + 대상 + 고충 조합)
KEYWORDS_LABOR = {
    "디지털_대행_노동": [
        "부모님 대신 예매", "엄마 쿠팡 주문 대신", "아빠 뱅킹 대신", "부모님 기차표 예매 대행",
        "부모님 인증번호 확인 전화", "부모님 병원 예약 대신", "부모님 배달 앱 결제 대신", "부모님 회원가입 대행",
        "대신 해드리는 온라인 쇼핑", "시댁 장보기 대행", "항공권 예매 대행 부모님", "부모님 대신 수강신청",
        "정부24 민원 서류 대신", "아이디 찾기 대신 부모님", "비밀번호 재설정 대행", "대신 해주는 디지털",
        "엄마 비행기표 예매", "아빠 대신 송금", "부모님 택시 호출 대신", "시어머니 쇼핑 대신",
        "부모님 공인인증서 갱신 대신", "어르신 앱 설치 대행", "자녀가 대신 결제", "대신 주문 스트레스",
        "부모님 영화표 예매 대신", "부모님 해외직구 대행", "부모님 식당 원격 줄서기", "부모님 호텔 예약 대행"
    ],
    "반복_설명_노동": [
        "부모님 스마트폰 사용법 교육", "엄마 핸드폰 가르쳐주기 스트레스", "아빠 스마트폰 질문 또", "시어머니 가전제품 설명",
        "할머니 카톡 배우기", "어르신 앱 사용법 설명", "기기 사용법 반복 질문", "스마트폰 가르치다 화남",
        "디지털 문맹 부모님 교육", "키오스크 가르쳐드리기 답답", "앱 사용법 설명 반복", "엄마 핸드폰 알려주다 싸움",
        "아빠 핸드폰 또 물어봐", "부모님 유튜브 사용법 반복", "티비 리모컨 작동법 설명", "스마트폰 사용법 메모",
        "부모님 기기 교육 한계", "디지털 소외 부모님", "똑같은 거 또 물어보심", "가전제품 기능 설명 반복",
        "부모님 전용 스마트폰 가이드", "엄마랑 핸드폰 때문에 싸움", "부모님 태블릿 교육", "어르신 정보화 교육 자녀"
    ],
    "인지적_부담_불안": [
        "부모님 가스불 확인 연락", "홈캠 부모님 확인", "안부 전화 반복 강박", "부모님 보이스피싱 걱정",
        "부모님 위치 확인 앱 설치", "외출 후 부모님 걱정", "인덕션 자동 차단기 설치", "부모님 안부 연락 노이로제",
        "엄마 핸드폰 원격제어 설정", "아빠 위치추적 자녀", "혼자 계신 부모님 불안", "부모님 스마트홈 설치 후기",
        "부모님 안부 전화 스트레스", "부모님 외출 확인", "부모님 전기장판 걱정", "어르신 낙상 걱정 홈캠",
        "부모님 스마트워치 위치추적", "부모님 보이스피싱 예방 교육", "부모님 스팸 문자 차단 대신"
    ],
    "물리적_방문_한계": [
        "전화로 안돼서 결국 방문", "결국 직접 가야 해결되는", "부모님 댁 기기 수리 방문", "주말마다 시댁 방문 이유",
        "원격제어 실패 직접 방문", "부모님 가전 AS 대신 접수", "전화 설명의 한계", "디지털 효도 방문기",
        "결국 자식 손이 가야 해결", "부모님 댁 스마트폰 수리 방문", "직접 가야 하는 디지털 문제",
        "부모님 댁 와이파이 고치러", "부모님 댁 셋톱박스 수리", "주말마다 부모님 댁 가전", "디지털 뒤치다꺼리"
    ]
}

def get_driver():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    # options.add_argument("--headless") # 필요시 주석 해제 (창 안뜨게 함)
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

def crawl_naver_heavy(driver, keyword, category, max_posts=100):
    encoded_keyword = quote(keyword)
    # 통합검색에서 스마트블록과 VIEW를 모두 뒤집니다.
    url = f"https://search.naver.com/search.naver?query={encoded_keyword}"
    results = []
    
    try:
        driver.get(url)
        time.sleep(2)
        
        # 1,000건 확보를 위해 스크롤을 충분히 내립니다.
        body = driver.find_element(By.TAG_NAME, "body")
        for _ in range(12): 
            body.send_keys(Keys.END)
            time.sleep(0.7)
        
        soup = BeautifulSoup(driver.page_source, "html.parser")
        
        # 네이버의 모든 콘텐츠 블록 탐색 (bx, view_wrap, n_info 등)
        items = soup.select('div[class*="bx"], div[class*="view_wrap"], div[class*="total_area"]')
        
        for item in items:
            # 제목과 링크 찾기
            title_tag = item.select_one('a[class*="tit"], a[class*="text"], div[class*="tit"]')
            if title_tag:
                title = title_tag.get_text(strip=True)
                
                # 🚫 광고 및 무관한 데이터 필터링 (순도 높이기)
                noise_words = ["보험", "공동구매", "최저가", "발품", "배달대행", "수익", "알바"]
                if any(x in title for x in noise_words) or len(title) < 10:
                    continue
                
                # 🚫 중복 수집 방지
                if any(r['title'] == title for r in results):
                    continue
                
                snippet = item.get_text(" ", strip=True)
                
                results.append({
                    "축": "인지적 부양",
                    "카테고리": category,
                    "keyword": keyword,
                    "title": title,
                    "snippet": snippet[:300] # 분석을 위해 내용을 조금 더 길게 가져옵니다.
                })
            
            if len(results) >= max_posts:
                break
    except Exception as e:
        print(f" ⚠️ {keyword} 수집 중 오류: {e}")
    return results

if __name__ == "__main__":
    driver = get_driver()
    final_data = []
    
    print("="*60)
    print("🚀 [인지적 부양 노동] 1,000건 목표 수집기 가동")
    print("="*60)
    
    try:
        for category, keywords in KEYWORDS_LABOR.items():
            print(f"\n📂 현재 카테고리: {category}")
            for kw in keywords:
                res = crawl_naver_heavy(driver, kw, category)
                final_data.extend(res)
                print(f" ✅ {kw} -> {len(res)}건 (누적: {len(final_data)}건)")
                
        # 2. 결과 저장
        if final_data:
            df = pd.DataFrame(final_data)
            df.drop_duplicates(subset=['title'], inplace=True)
            df.to_csv("bx_crawling_results_v2.csv", index=False, encoding="utf-8-sig")
            print("\n" + "="*60)
            print(f"✨ 수집 완료! 최종 {len(df)}건이 bx_crawling_results_v2.csv에 저장되었습니다.")
            print("="*60)
        else:
            print("\n❌ 수집된 데이터가 없습니다.")
            
    finally:
        driver.quit()