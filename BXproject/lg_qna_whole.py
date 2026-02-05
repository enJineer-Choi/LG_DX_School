# 라이브러리 불러오기

import selenium.webdriver as wb

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains # 복잡한 상호작용 자동화 도구

import time

from tqdm import tqdm

import pandas as pd

import re # 정규표현식 도구

from urllib.parse import quote # URL에서 사용할 수 없는 문자를 16진수로 포맷하는 도구

from kiwipiepy import Kiwi # 키위 형태소 분석 도구

from wordcloud import WordCloud # 워드 클라우드 생성 도구

from collections import Counter # 단어가 나온 횟수 세는 도구

import matplotlib.pyplot as plt # 시각화 도구

from PIL import Image # mask 이미지 생성 도구

import numpy as np

# 문자열 전처리 함수 -> 숫자, 문자, (?.!,¿) 제외하고 공백으로 대체

def preprocess_sentence_kr(w):

  w = w.strip()

  w = re.sub(r"[^0-9가-힣?.!,¿]+", " ", w) 

  w = w.strip()

  return w



# url 설정

url = "https://www.lge.co.kr/home"

# 브라우저 열기

driver = wb.Chrome()

# 페이지 요청

driver.get(url)

# 로딩 기다리기

time.sleep(1)

actions = ActionChains(driver)

# [제품/소모품] 탭 호버
product_tab = driver.find_element(By.CLASS_NAME, "CommonPcGnb_item__ooPqg")
actions.move_to_element(product_tab).perform()

# 제품 분류 탭에서 모든 제품 분류의 이름('TV/오디오' ~ '에어컨/에어케어') 가져오기
product_classes = driver.find_elements(By.CLASS_NAME, "CommonPcGnb_scroll_item__bXHY9")[:5]
product_class_names = [pt.text for pt in product_classes]
print(product_class_names)

# 제품 분류별 메뉴 아이디
product_class_ids = ["#NV0001140"+str(i) for i in range(3, 8)] # id = #NV00011403 ~ #NV00011407
# 분류별 제품 url: {"TV/오디오": ["TV": url], ...}
class_product_urls = {}

for i in range(len(product_class_ids)):
    # i번째 제품 분류 탭으로 호버
    actions.move_to_element(product_classes[i]).perform()
    # i번째 제품 분류 메뉴의 제품 종류 객체 가져오기
    product_types = driver.find_elements(By.CSS_SELECTOR, product_class_ids[i]+" .CommonPcGnb_sub_cate_tit__hJBJn>a")
    # i번째 제품 분류 메뉴의 제품 종류 이름 및 url 수집
    name_url = []
    for j in range(len(product_types)):
        product_type_name = product_types[j].text
        product_type_url = product_types[j].get_attribute("href")
        name_url.append([product_type_name, product_type_url])
    class_product_urls[product_class_names[i]] = name_url

# 분류별 제품 url 확인
class_product_urls

# 분류별 제품 url: {"TV/오디오": {"TV": [best1_url, best2_url, best3_url], ...}, ...}
class_type_product_urls = {}
for product_class in product_class_names:
    print(product_class, "제품별 링크 접속 중...")
    type_product_urls = {}
    for type_url in class_product_urls[product_class]:
        driver.get(type_url[1])
        print(type_url[0], "링크 접속 완료!")
        time.sleep(1)
        # 베스트랭킹 1~3 상품 url 수집
        best = driver.find_elements(By.CSS_SELECTOR, ".PlpPcBestranking_unit_item__lnMdk>a")[:3]
        if best == []: # 만약 베스트랭킹이 없을 경우 수집 x (제품 수 또는 리뷰와 Q&A 데이터가 많이 없기 때문)
            print("베스트랭킹 없음 ㅠ.ㅠ")
            continue
        product_urls = []
        for b in best:
            # 리스트에 베스트랭킹 1~3 상품 url 수집
            product_urls.append(b.get_attribute("href"))
        # 딕셔너리에 제품별로 베스트랭킹 1~3 상품 url 담기
        type_product_urls[type_url[0]] = product_urls
    class_type_product_urls[product_class] = type_product_urls
    print()
class_type_product_urls

import time
import re
import pickle
from selenium.webdriver.common.by import By

# 결과를 담을 최종 데이터 구조
class_type_product_data = {}

for class_name, type_dict in class_type_product_urls.items():
    print(f"\n>>> 대분류 수집 시작: {class_name}")
    class_type_product_data[class_name] = {}
    
    for type_name, urls in type_dict.items():
        print(f"  > 중분류 수집 중: {type_name}")
        
        total_qna_count = 0    
        usage_qna_count = 0    
        all_use_qna_titles = [] 
        
        for url in urls:
            driver.get(url)
            time.sleep(3) 
            
            try:
                # 1. Q&A 탭 클릭 (JS 클릭으로 안전하게)
                qna_tab = driver.find_elements(By.CSS_SELECTOR, ".tab-menu>.linker")[3]
                driver.execute_script("arguments[0].click();", qna_tab)
                time.sleep(2)
                
                # 2. 전체 문의글 수 수집
                qna_total_text = driver.find_element(By.CSS_SELECTOR, ".title .count").text
                total_qna_count += int(re.sub(r'[^0-9]', '', qna_total_text))
                
                # 3. 문의 유형 드롭다운 클릭
                inquiry_buttons = driver.find_elements(By.CSS_SELECTOR, ".ui-select-button>.ui-select-text")
                driver.execute_script("arguments[0].click();", inquiry_buttons[1])
                time.sleep(1)
                
                # 4. '제품 사용 문의' 필터 선택
                inquiry_type_menu = driver.find_elements(By.CSS_SELECTOR, ".ui-select-scrollarea a")
                target_found = False
                for menu in inquiry_type_menu:
                    if "제품 사용 문의" in menu.text:
                        driver.execute_script("arguments[0].click();", menu)
                        target_found = True
                        break
                if not target_found:
                    driver.execute_script("arguments[0].click();", inquiry_type_menu[4])
                
                time.sleep(2)

                # 5. 페이지 순회 (최대 페이지까지 동적으로)
                page_idx = 1
                while True:
                    # 현재 페이지 제목 수집
                    titles = driver.find_elements(By.CSS_SELECTOR, "div.title-box>h4.title")
                    for qna in titles:
                        txt = qna.text
                        if "제품 사용 문의" in txt:
                            clean_title = txt.replace("문의글 제목\n[제품 사용 문의] ", "").strip()
                            all_use_qna_titles.append(clean_title)
                    
                    # 다음 페이지 버튼 찾기
                    try:
                        # 페이지 번호 링크들 가져옴
                        pages = driver.find_elements(By.CSS_SELECTOR, ".page_num>a")
                        
                        # 다음 페이지 번호(page_idx + 1) 찾기
                        next_page_btn = None
                        for p in pages:
                            if p.text.strip() == str(page_idx + 1):
                                next_page_btn = p
                                break
                        
                        if next_page_btn:
                            driver.execute_script("arguments[0].click();", next_page_btn)
                            time.sleep(2)
                            page_idx += 1
                            continue  # 다음 페이지로 진행
                        
                        # 다음 번호 없으면 '다음' 버튼 찾기 (클래스: .next 또는 유사, 사이트 확인 후 조정)
                        next_group_btn = driver.find_elements(By.CSS_SELECTOR, ".next>a")  # '다음' 버튼 셀렉터 (필요시 .page_next 등으로 변경)
                        if next_group_btn and next_group_btn[0].is_enabled():
                            driver.execute_script("arguments[0].click();", next_group_btn[0])
                            time.sleep(2)
                            page_idx += 1  # 페이지 그룹이 넘어갔으므로 인덱스 증가 (실제로는 리셋될 수 있음, 로그로 확인)
                        else:
                            break  # 더 이상 페이지 없음
                    except:
                        break  # 에러 시 종료
                        
            except Exception as e:
                print(f"      수집 실패 ({url}): {e}")

        # 한 상품군(베스트 1~3위) 수집 완료 후 저장
        usage_qna_count = len(all_use_qna_titles) # 실제 수집된 타이틀 개수 반영
        combined_titles = " ".join(all_use_qna_titles)
        class_type_product_data[class_name][type_name] = [
            (total_qna_count, usage_qna_count), 
            combined_titles
        ]

# 6. 파일 저장 로직 (이전과 동일)
with open("lg_qna_raw_backup_whole.txt", "w", encoding="utf-8") as f:
    for c_name, t_dict in class_type_product_data.items():
        f.write(f"\n[대분류: {c_name}]\n")
        for t_name, data in t_dict.items():
            f.write(f"  - {t_name}: 전체{data[0][0]}건/사용수집{data[0][1]}건\n")
            f.write(f"    텍스트: {data[1][:200]}...\n")

with open("class_type_product_data_whole.pkl", "wb") as f:
    pickle.dump(class_type_product_data, f)

print("\n✅ 최대 페이지 수집 및 원본 저장이 완료되었습니다!")