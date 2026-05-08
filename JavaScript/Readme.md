# 🟨 JavaScript 학습 정리

> JS 기본 문법부터 DOM 조작, 이벤트 처리, 외부 API 연동까지 학습 내용 정리

---

## 1. 기본 문법

- 변수 선언 : `var`, `let`, `const` 차이점 및 스코프(Scope)
- 자료형 : 숫자, 문자, boolean, 배열, 객체(JSON)
- 연산자 : 산술 연산, `==` vs `===` (값 비교 vs 값+타입 비교)
- 대화 상자 : `alert`, `confirm`, `prompt`
- 형 변환 : `parseInt`, 삼항 연산자
- 실습 : 사칙연산 계산기, 두 수 중 큰 값 출력

---

## 2. 제어문

- 반복문 : `while`, `for` 기본 구조 및 활용
- 실습 : 1~10 합계, 보스 몬스터 딜 계산기, 30의 약수 출력, 1~1000 완전수 탐색
- 응용 : `Math.random()`으로 숫자 추측 게임 구현

---

## 3. 배열 / 객체 / 함수

- 배열 : 생성, `length`, 추가/삭제 메서드 (`push`, `pop`, `shift`, `unshift`)
- 함수 : 선언 방식 vs 표현 방식, 지역 함수, `return` 값 반환
- 화살표 함수(Arrow Function) 문법
- 객체(Object) : `{key: value}` 구조, 속성 접근 및 수정
- `this` 키워드 : 객체 내 함수에서 사용, Arrow Function에서는 사용 불가
- JSON 배열로 회원 리스트 구성 후 HTML 테이블로 출력

---

## 4. DOM 조작 및 이벤트 처리

- 요소 선택 : `getElementById`, `getElementsByTagName`, `getElementsByClassName`, `querySelector`, `querySelectorAll`
- 내용 변경 : `innerText` (텍스트) vs `innerHTML` (HTML 구조)
- 스타일 변경 : `요소.style.속성`, `setAttribute`
- 동적 요소 생성/삭제 : `createElement`, `createTextNode`, `appendChild`
- 페이지 이동 : `location.href`
- 타이머 : `setInterval`, `clearInterval`
- 실습 : 버튼 클릭 시 색상/크기 변경, 10초 카운트다운 후 페이지 이동, 분식집 메뉴 동적 추가

---

## 5. API 연동 및 응용 실습

- 비동기 통신 : `fetch`, `async/await`
- **KOBIS 영화진흥위원회 API** : 일별 박스오피스 데이터 조회 후 테이블 출력
- **OpenWeatherMap API** : 도시별 현재 날씨(온도, 상태) 조회 및 화면 표시
- 이미지 슬라이드 : 배열로 이미지 관리, 버튼으로 이전/다음 전환
- 키보드 이벤트(`keydown`) + `setInterval`로 말 이동 게임 구현
