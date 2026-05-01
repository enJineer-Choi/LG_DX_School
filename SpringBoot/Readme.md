# Spring Boot 기반 웹 서비스 설계
- Spring Boot
- Thymeleaf
- MyBatis
---
[ 브라우저 ]
    ↕ HTTP 요청/응답
[ Spring Boot ] ← 전체를 감싸는 프레임워크
    ├── FrontController (DispatcherServlet)
    │       모든 요청을 여기서 받아서 각 Controller로 분배
    ├── Controller → 어떤 요청인지 판단
    ├── Service    → 비즈니스 로직 처리
    ├── MyBatis    → SQL 실행해서 DB와 소통
    │
    ├── Thymeleaf  → 결과를 HTML로 변환해서 응답
    └── Oracle DB  → 실제 데이터 저장
