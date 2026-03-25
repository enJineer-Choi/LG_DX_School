## diagnose_82cook.py
## 이 파일 실행 후 결과를 Claude에게 보내주세요!

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/119.0.0.0 Safari/537.36",
    "Referer": "https://www.82cook.com/",
    "Accept-Language": "ko-KR,ko;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

# 실제 게시글 URL
URL = "https://www.82cook.com/entiz/read.php?bn=15&num=4159725&page=1&searchType=search&search1=2&keys=%EA%B0%80%EC%A0%84+%EA%B5%AC%EB%8F%85"

res = requests.get(URL, headers=HEADERS, timeout=10)
res.encoding = "utf-8"
html = res.text
soup = BeautifulSoup(html, "html.parser")

print(f"[1] 응답 상태코드: {res.status_code}")
print(f"[2] HTML 총 길이: {len(html)} 글자")
print(f"[3] 'articleBody' 문자열 존재 여부: {'articleBody' in html}")
print(f"[4] 'div#articleBody' 셀렉터 결과: {soup.select_one('div#articleBody')}")
print(f"[5] '#articleBody' 셀렉터 결과: {soup.select_one('#articleBody')}")
print()

# HTML 앞부분 500자 출력 (리다이렉트/로그인 페이지인지 확인)
print("[6] HTML 앞 500자:")
print(html[:500])
print()

# id/class 있는 주요 태그 목록
print("[7] id 있는 태그 목록:")
for tag in soup.find_all(id=True):
    text_len = len(tag.get_text(strip=True))
    if text_len > 20:
        print(f"  <{tag.name} id='{tag['id']}'> 텍스트 길이={text_len}")