-- (0303)
-- DDL : 테이블과 같이 데이터 저장소 객체를 만들거나 수정하거나 삭제할 때 사용

-- CREATE : 테이블(객체) 생성시 사용
-- 직원테이블 한글버전
CREATE TABLE 직원정보 (
    직원번호 NUMBER(10), -- 중복되선 안되고, 값을 무조건 가지고 있어야함 (특성)
    이름 VARCHAR2(100),
    급여 NUMBER(10) NOT NULL, --조건을 걸어줌 (절대 NULL값이 들어가지 않도록)
    부서번호 NUMBER(10),  -- 이미있는 데이터를 참조해서 넣어줘야함!
    입사일 DATE
);

-- DROP : 테이블(객체) 삭제 명령
DROP TABLE 직원정보;

-- 제약조건 사용법1
-- 테이블 생성 시 추가하기
CREATE TABLE 직원정보 (
    직원번호 NUMBER(10) PRIMARY KEY, -- 중복되선 안되고, 값을 무조건 가지고 있어야함 (특성)
    이름 VARCHAR2(100),
    급여 NUMBER(10) NOT NULL, --조건을 걸어줌 (절대 NULL값이 들어가지 않도록)
    부서번호 NUMBER(10),
    입사일 DATE
);

-- 제약조건 사용법2
-- 테이블 먼저 만든 다음에, 조건 추가를 통한 테이블 수정
CREATE TABLE 직원정보 (
    직원번호 NUMBER(10), -- 중복되선 안되고, 값을 무조건 가지고 있어야함 (특성)
    이름 VARCHAR2(100),
    급여 NUMBER(10) NOT NULL, --조건을 걸어줌 (절대 NULL값이 들어가지 않도록)
    부서번호 NUMBER(10),
    입사일 DATE
);

-- 수정 명령어
ALTER TABLE 직원정보 ADD CONSTRAINT PRIMARY KEY(직원번호);
-- 이대로 하면 에러 발생


ALTER TABLE 직원정보 ADD CONSTRAINT 직원정보_PK PRIMARY KEY(직원번호);



-- 부서정보 테이블을 한글버전으로 만들기
CREATE TABLE 부서정보 (
    부서번호 NUMBER(10),
    부서이름 VARCHAR2(100),
    매니저번호 NUMBER(10),
    지역번호 NUMBER(10)
);


ALTER TABLE 직원정보 ADD CONSTRAINT 직원정보_FK FOREIGN KEY(부서번호) REFERENCES 부서정보(부서번호);
-- 에러남 > 즉, 부서번호에 다른 제약조건이 없음. 
-- ALTER TABLE 부서정보 ADD CONSTRAINT PRIMARY KEY(부서번호); > 이 코드 실행전임. 
-- 즉, 현재 중복에 대한 특별한 조건이 없음. > 참조를 하려면 중복에 대한 제약조건이 필요함.
-- 



-- 부서 정보 테이블에 부서번호 컬럼에 PK 제약조건 추가. 
ALTER TABLE 부서정보 ADD CONSTRAINT 부서정보_PK PRIMARY KEY(부서번호);


-- 위 코드 실행시킨 후에 실행하면 제약조건이 잘 들어갔기때문에, 코드 OK
ALTER TABLE 직원정보 ADD CONSTRAINT 직원정보_FK FOREIGN KEY(부서번호) REFERENCES 부서정보(부서번호);



-- 실습: 네이버 회원 테이블, 네이버 블로그 테이블


CREATE TABLE 네이버회원(
    ID VARCHAR2(15),
    이름 VARCHAR2(12) NOT NULL,
    비밀번호 VARCHAR2(16),
    생년월일 DATE,
    성별 VARCHAR2(3)
);


CREATE TABLE 네이버블로그(
    블로그번호 NUMBER ,
    블로그제목 VARCHAR2(100) NOT NULL,
    블로그내용 VARCHAR2(4000),
    ID VARCHAR2(15) 
);


ALTER TABLE 네이버회원 ADD CONSTRAINT 회원_ID_PK PRIMARY KEY(ID);
ALTER TABLE 네이버회원 ADD CONSTRAINT 회원_성별_CK CHECK (성별 IN ('남','여'));
ALTER TABLE 네이버블로그 ADD CONSTRAINT 블로그_번호_PK PRIMARY KEY(블로그번호);
ALTER TABLE 네이버회원 ADD CONSTRAINT 블로그_회원ID_FK FOREIGN KEY(ID) REFERENCES 네이버블로그(ID);
-- 이렇게 적으면 네이버 회원이 블로그 테이블을 참조하고 싶다는 의미..

ALTER TABLE 네이버블로그 ADD CONSTRAINT 블로그_회원ID_FK FOREIGN KEY(ID) REFERENCES 네이버회원(ID);
-- 블로그가 -> 회원을 참조하고 싶음.
-- 네이버 블로그 테이블에 ID를 FOREIGN KEY로 참조하고 싶음. 근데 어떤 테이블 ? > 네이버회원 테이블


-- 정답 코드
-- 네이버회원
CREATE TABLE 네이버회원(
    ID VARCHAR2(15) ,
    이름 VARCHAR2(12) NOT NULL,
    비밀번호 VARCHAR2(16),
    생년월일 DATE,
    성별 VARCHAR2(3)
);

-- 네이버블로그
-- NUMBER : 38자리까지로 임의로 정해짐
CREATE TABLE 네이버블로그(
    블로그번호 NUMBER,
    블로그제목 VARCHAR2(100) NOT NULL,
    블로그내용 VARCHAR2(4000),
    ID VARCHAR2(15)
);

ALTER TABLE 네이버회원 ADD CONSTRAINT 회원_ID_PK PRIMARY KEY(ID);
ALTER TABLE 네이버회원 ADD CONSTRAINT 회원_성별_CK CHECK (성별 IN ('남','여'));
ALTER TABLE 네이버블로그 ADD CONSTRAINT 블로그_번호_PK PRIMARY KEY(블로그번호);
ALTER TABLE 네이버블로그 ADD CONSTRAINT 블로그_회원ID_FK FOREIGN KEY(ID) REFERENCES 네이버회원(ID);



-- 제약조건은 지우는 방식으로 사용.
ALTER TABLE 네이버회원 DROP CONSTRAINT 회원_성별_CK; 


DROP TABLE 네이버회원; 
-- 불가능 : 참조키가 걸려있어서 안됨.

-- 이런 방식으로 지울 수 있음.
DROP TABLE 네이버블로그;
-- 블로그 먼저 지우고














































































