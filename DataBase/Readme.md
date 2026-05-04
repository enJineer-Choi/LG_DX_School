# 🗄️ Database 학습 정리

> Oracle SQL 기초 문법부터 DDL, DML, DCL, TCL 및 고급 조회까지 핵심 개념 정리

---

## 1. DDL (데이터 정의어)

테이블(객체)의 구조를 **생성 · 수정 · 삭제**하는 명령어

- **CREATE** : 테이블 생성 (직원정보, 부서정보, 네이버회원 등 예시)
- **DROP** : 테이블 삭제
- **ALTER TABLE** : 테이블 수정 및 제약조건 추가
  - 제약조건 종류 : `PRIMARY KEY`, `NOT NULL`, `FOREIGN KEY`, `CHECK`

---

## 2. DML (데이터 조작어)

테이블의 **데이터를 삽입 · 수정 · 삭제**하는 명령어

- **INSERT** : 데이터 삽입
- **UPDATE** : 조건(`WHERE`)을 사용한 데이터 수정
- **DELETE** : 데이터 삭제 (조건 없으면 전체 삭제 주의)

---

## 3. DCL (데이터 제어어)

**사용자 권한**을 부여하거나 회수하는 명령어

- **GRANT** : 접속, 테이블 생성 등 권한 부여
- **REVOKE** : 부여했던 권한 회수

---

## 4. TCL (트랜잭션 제어어)

DML 작업을 **확정하거나 되돌리는** 명령어

- **COMMIT** : 변경 내용을 DB에 영구 저장
- **ROLLBACK** : 마지막 COMMIT 시점으로 되돌리기
- ⚠️ DDL은 AUTO COMMIT → ROLLBACK 불가

---

## 5. SELECT (데이터 조회)

- **실행 순서** : `FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY`
- **WHERE** : 조건 필터링 (`AND`, `OR`, `IN`, `BETWEEN`, `LIKE` 등)
- **GROUP BY** : 데이터 그룹화 + 집계 함수 (`SUM`, `AVG`, `MAX`, `MIN`, `COUNT`)
- **HAVING** : 그룹에 조건 적용 (WHERE와 달리 집계 함수 사용 가능)
- **ORDER BY** : 오름차순(`ASC`) / 내림차순(`DESC`) 정렬
- **JOIN** : 두 개 이상의 테이블을 공통 컬럼 기준으로 연결
- **SUB QUERY** : 쿼리 안의 쿼리
  - 단일 행 서브쿼리 : `=`, `<`, `>` 사용
  - 다중 행 서브쿼리 : `IN`, `ANY`, `ALL` 사용

---

## 6. 기타 객체 및 기능

- **VIEW** : 복잡한 SELECT문을 저장해 가상 테이블처럼 재사용
- **SEQUENCE** : 연속된 숫자를 자동 생성 (Oracle의 AUTO INCREMENT 역할)
- **ROWNUM** : 조회 결과에서 상위 N개 행만 추출할 때 사용

---

## 🗺️ SQL 명령어 분류 요약

| 분류 | 이름 | 주요 명령어 |
|------|------|------------|
| **DDL** | 데이터 정의어 | `CREATE`, `DROP`, `ALTER` |
| **DML** | 데이터 조작어 | `INSERT`, `UPDATE`, `DELETE` |
| **DCL** | 데이터 제어어 | `GRANT`, `REVOKE` |
| **TCL** | 트랜잭션 제어어 | `COMMIT`, `ROLLBACK` |
| **DQL** | 데이터 질의어 | `SELECT` |
