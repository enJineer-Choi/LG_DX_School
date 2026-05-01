# 📚 Spring Boot 학습 프로젝트

> LG DX School 부트캠프 병행 개인 학습 환경 정리

---

## 🛠️ 기술 스택 (Tech Stack)

### Backend
| 기술 | 버전 | 설명 |
|------|------|------|
| **Java** | 17 | 메인 언어 |
| **Spring Boot** | 3.3.x | 웹 애플리케이션 프레임워크 |
| **MyBatis** | - | SQL 매퍼 (Java ↔ SQL 연결) |

### Frontend (Server-Side Rendering)
| 기술 | 설명 |
|------|------|
| **Thymeleaf** | 서버사이드 HTML 템플릿 엔진 |
| **HTML / CSS / JS** | 정적 리소스 (`static/` 폴더 관리) |

### Database
| 환경 | DB | 설명 |
|------|-----|------|
| 부트캠프 (Windows) | **Oracle** | SQL Developer로 로컬 접속 |


### 개발 도구
| 환경 | IDE | 빌드 도구 |
|------|-----|----------|
| 부트캠프 (Windows) | Eclipse | Maven |
| 개인 (MacBook) | IntelliJ IDEA | Maven |

---

## 📁 프로젝트 디렉토리 구조

```
src/
├── main/
│   ├── java/com/example/demo/
│   │   ├── DemoApplication.java        ← 애플리케이션 진입점 (main)
│   │   │
│   │   ├── controller/                 ← 요청 처리 (URL 매핑)
│   │   │   └── HomeController.java
│   │   │
│   │   ├── service/                    ← 비즈니스 로직
│   │   │   └── HomeService.java
│   │   │
│   │   ├── mapper/                     ← MyBatis 인터페이스
│   │   │   └── HomeMapper.java
│   │   │
│   │   └── dto/                        ← 데이터 전달 객체
│   │       └── HomeDto.java
│   │
│   └── resources/
│       ├── mapper/                     ← MyBatis SQL XML 파일
│       │   └── HomeMapper.xml
│       │
│       ├── templates/                  ← Thymeleaf HTML 파일 (동적)
│       │   └── index.html
│       │
│       ├── static/                     ← 정적 리소스 (변하지 않는 파일)
│       │   ├── css/
│       │   ├── js/
│       │   └── images/
│       │
│       └── application.properties      ← 환경 설정 (DB 접속 정보 등)
│
└── test/                               ← 테스트 코드
```

---

## 🔄 전체 요청 처리 흐름 (Architecture)

```
[ 브라우저 ]
     │  HTTP 요청 (예: GET /home)
     ▼
[ DispatcherServlet ]  ← FrontController 역할
  Spring Boot가 자동 등록
  모든 요청을 한 곳에서 받아 적절한 Controller로 분배
     │
     ▼
[ Controller ]
  @GetMapping("/home")
  URL 요청을 받아 어떤 작업을 할지 결정
  Service를 호출
     │
     ▼
[ Service ]
  실제 비즈니스 로직 처리
  Mapper(MyBatis)를 호출
     │
     ▼
[ Mapper (MyBatis) ]
  Java 인터페이스 ↔ SQL XML 파일 매핑
  SQL 쿼리 실행
     │
     ▼
[ Database (Oracle / H2) ]
  실제 데이터 저장 및 조회
     │
     ▼ (데이터 반환)
[ Controller ]
  Model에 데이터 담아서 View 이름 반환
     │
     ▼
[ Thymeleaf ]
  templates/ 폴더의 HTML에 데이터를 끼워넣어
  완성된 HTML 생성
     │
     ▼
[ 브라우저 ]
  완성된 HTML 페이지 렌더링
```
