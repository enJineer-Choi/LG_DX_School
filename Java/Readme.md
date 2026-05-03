# ☕ Java 학습 정리

> 자바 기초 문법부터 OOP, JDBC, 멀티스레드까지 단계별 실습 내용 정리

---

## 📚 학습 목차

1. [자바 기초 및 제어문](#1-자바-기초-및-제어문)
2. [객체 지향 프로그래밍 (OOP)](#2-객체-지향-프로그래밍-oop)
3. [심화 주제 및 응용](#3-심화-주제-및-응용)

---

## 1. 자바 기초 및 제어문

### 📌 변수 및 연산자

| 개념 | 주요 내용 | 실습 파일 |
|------|----------|----------|
| 변수 & 자료형 | 기본 자료형, 상수(`final`), 형 변환 | `Ex01variable.java` |
| 연산자 | 산술, 논리, 삼항 연산자 | `Ex02operator.java`, `Ex03and.java`, `Ex04tripleoperator.java` |
| 응용 | 큰 수 처리, 농구 점수 계산 | `Ex06bignumber.java`, `Ex07basketball.java` |

### 📌 조건문

| 개념 | 주요 내용 | 실습 파일 |
|------|----------|----------|
| if / else | 기본 조건 분기 | `Ex01conditional.java`, `Ex02else.java` |
| else if | 다중 조건 처리 | `Ex03elseif.java` |
| switch | 다중 분기, 계절 판별 실습 | `Ex04switch.java`, `Ex05season.java` |

### 📌 반복문

| 개념 | 주요 내용 | 실습 파일 |
|------|----------|----------|
| while | 기본 반복 | `Ex07while.java` |
| do-while | 최소 1회 실행 보장 | `Ex01dowhile.java` |
| for | 구구단, 숫자 나누기, 다중 for문 | `Ex03for.java`, `Ex04for.java`, `Ex05googoodan.java`, `Ex07divide.java`, `Ex09multi.java` |

### 📌 배열 및 정렬/탐색 알고리즘

| 개념 | 주요 내용 | 실습 파일 |
|------|----------|----------|
| 배열 기초 | 선언, 초기화, 최댓값/최솟값 | `Ex04array.java` ~ `Ex07Array.java` |
| 정렬 | 버블 정렬, 선택 정렬 | `Ex08bubblesort.java`, `Ex09Selectsort.java` |
| 탐색 | 순차 탐색, 이진 탐색 | `Ex10Sequentialsearching.java`, `Ex11binarysearch.java` |

---

## 2. 객체 지향 프로그래밍 (OOP)

> Java OOP의 4대 핵심 개념: **캡슐화 · 상속 · 다형성 · 추상화**

### 📌 클래스 & 객체

- 클래스 정의, 필드(속성), 메소드(기능), 생성자 개념 학습
- 객체 생성 및 활용 실습

```
실습 파일: Ex05Car.java / Ex05Car_main.java
          PiggyBank.java / PiggyBank_main.java
          Person.java / Person_main.java
```

### 📌 캡슐화 & 접근 제한자

- `private` → 정보 은닉 (외부 직접 접근 차단)
- 접근 제한자 범위: `public` > `protected` > `default` > `private`

```
실습 파일: Ex01Access.java / Ex01Access_main.java / Ex01Another.java
```

### 📌 상속 & 다형성

| 개념 | 설명 |
|------|------|
| `extends` | 부모 클래스의 필드/메소드 상속 |
| 메소드 오버라이딩 | 자식 클래스에서 부모 메소드 재정의 |
| 업캐스팅 / 다운캐스팅 | 부모↔자식 타입 변환 |
| 추상 클래스 / 추상 메소드 | 구현 강제화, 설계 틀 제공 |

```
실습 파일: ParentsStore.java / ChildStore.java / Store_main.java
          Mouse.java / WheelMouse.java / SpeedMouse.java
          Doll.java / Ryan.java / Jjangu.java / Ditto.java
```

### 📌 인터페이스

- 인터페이스 정의 및 `implements` 구현
- **다중 상속** 지원 (Java는 클래스 다중 상속 불가, 인터페이스는 가능)
- 인터페이스 간 상속

```
실습 파일: Ex01Interface.java
          Phone.java / Camera.java / SmartPhone.java / Phone_class.java
```

> 💡 **클래스 vs 인터페이스**
> - 추상 클래스: `is-a` 관계 (예: 고양이 **is a** 동물)
> - 인터페이스: `can-do` 관계 (예: 스마트폰 **can** 카메라 기능)

### 📌 객체 배열 & 컬렉션

| 개념 | 설명 | 실습 파일 |
|------|------|----------|
| 객체 배열 | 클래스 타입의 배열 선언 및 사용 | `Student_main.java`, `BookData_main.java` |
| ArrayList | 동적 크기 리스트, 데이터 추가/삭제/조회 | `Ex01ArrayList.java`, `Address_main.java`, `MusicPlayList.java` |

---

## 3. 심화 주제 및 응용

### 📌 JDBC (Java Database Connectivity)

> Java에서 Oracle DB에 직접 연결하여 SQL을 실행하는 방법

```
연결 흐름:
Java 코드 → JDBC 드라이버 → Oracle DB
```

| 단계 | 내용 | 실습 파일 |
|------|------|----------|
| DB 연결 | Oracle 드라이버 로딩, Connection 객체 생성 | `Ex01Connection.java` |
| INSERT | 데이터 삽입 | `Ex02Insert.java` |
| DELETE | 데이터 삭제 | `Ex03Delete.java` |
| UPDATE | 데이터 수정 | `Ex04Update.java` |
| SELECT | 데이터 조회 | `Ex05Select.java` |
| DAO 패턴 | DB 로직 분리 (Data Access Object) | `DAO.java`, `Dao_main.java`, `MemberVO.java` |

> 💡 **DAO 패턴이란?**
> DB 접근 로직을 별도 클래스(DAO)로 분리해서 관리하는 디자인 패턴.
> 나중에 배우는 MyBatis / JPA가 이 역할을 자동화해줌.

### 📌 스레드 (Thread)

> 여러 작업을 동시에 실행하는 **멀티스레드** 프로그래밍

| 방법 | 설명 | 실습 파일 |
|------|------|----------|
| `Thread` 클래스 상속 | `extends Thread` → `run()` 오버라이딩 | `Mythread.java` |
| `Runnable` 인터페이스 | `implements Runnable` → 더 유연한 구조 | `MyRunnable.java` |
| 실행 | `start()` 메소드로 새 스레드 시작 | `Mythread_main.java` |

### 📌 미니 프로젝트: 콘솔 음악 플레이어 🎵

> `jlap` 외부 라이브러리를 활용한 콘솔 기반 음악 플레이어 구현

**사용 기술**
- `javazoom.jl.player.Player` (MP3 재생)
- ArrayList로 플레이리스트 관리
- Thread로 백그라운드 재생 구현

```
구성 파일: Music.java          ← 음악 데이터 클래스 (제목, 경로 등)
          Musicplayercon.java  ← 플레이어 컨트롤 로직
          Music_main.java      ← 실행 진입점
```

---

## 🗺️ 전체 학습 흐름 요약

```
기초 문법
  └── 변수/자료형 → 연산자 → 조건문 → 반복문 → 배열
         ↓
객체 지향 (OOP)
  └── 클래스/객체 → 캡슐화 → 상속/다형성 → 인터페이스 → 컬렉션
         ↓
심화 & 응용
  └── JDBC (DB 연동) → 스레드 (멀티태스킹) → 미니 프로젝트
```
