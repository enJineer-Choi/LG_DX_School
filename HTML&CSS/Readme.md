# 🌐 WEB 학습 정리

> HTML 구조 설계부터 CSS 스타일링 및 레이아웃 구성까지 학습 내용 정리

---

## 1. HTML 기초

- HTML 기본 구조 및 태그/속성 개념
- 텍스트 태그 : 제목(`h1~h6`), 본문(`p`), 줄바꿈(`br`), 강조(`b`, `strong`)
- 목록 : 순서 없는 리스트(`ul`), 순서 있는 리스트(`ol`)
- 이미지 : `img` 태그, 이미지 경로 (상대/절대 경로, 네트워크/파일 방식)
- 하이퍼링크 : `a` 태그로 페이지 이동 및 이미지 링크 구현
- 표 : `table`, `tr`, `th`, `td`, `caption` 태그
- 폼 : `form` + `input` 태그 (text, password, checkbox, radio, file 등), `select` 태그
- 실습 : 회원가입 양식 페이지 구현 (form + table 조합)

---

## 2. CSS 기초 및 선택자

- CSS 기본 개념 및 `style` 태그로 작성하는 방법
- 폰트 스타일 : `font-family`, `font-size`, `font-weight`, `font-style`
- 폰트 크기 단위 : `px`, `em`, `rem` 차이점
- 선택자 종류 및 우선순위 : 전체(`*`), 태그, 클래스(`.`), 아이디(`#`) — `id` > `class` 순
- 계층 선택자 : 자손(` `), 자식(`>`), 형제(`+`, `~`)
- 그룹 선택자 : `,`로 여러 태그에 동일 스타일 적용
- 반응 선택자 : `:hover`, `:active` + `transition`, `transform`

---

## 3. CSS 박스 모델 및 레이아웃

- `display` 속성 : `inline`, `block` 특징 및 변환
- `display: none` + `:hover` 조합으로 숨김/표시 효과 구현
- `margin` : 요소 바깥 여백 (다른 요소와의 간격)
- `padding` : 요소 안쪽 여백 (콘텐츠와 테두리 사이 간격)
- `box-sizing` : `content-box` vs `border-box` 차이점, 외부 CSS 파일 연결
- `border-radius` : 테두리 둥글게 처리
- `position` : `static`, `relative`, `absolute`, `fixed` 배치 기준
- `overflow` : 콘텐츠 초과 시 처리 방법 (`visible`, `hidden`, `scroll`, `auto`)
- `float` : 이미지 주변 텍스트 배치
- 레이아웃 실습 : `float`으로 `header`, `navigation`, `side`, `section`, `footer` 구성
