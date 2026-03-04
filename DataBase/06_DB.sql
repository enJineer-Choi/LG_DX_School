--(0304)
-- DML : 데이터 조작어
-- 테이블에 원한느 데이터를 입력/수정/삭제
-- INSERT, UPDATE, DELETE


-- INSERT : 테이블에 데이터 입력
-- 부서정보테이블에 IT 부서정보 데이터를 입력

INSERT INTO 부서정보 VALUES (10,'IT',100,1000);
INSERT INTO 부서정보 VALUES (20,'IT',1000,100);
INSERT INTO 부서정보 VALUES (10,'IT',100,1000);
-- 10으로 또 똑같이 하면 안됨 ( PK 키 이므로 중복되서 들어갈 수 없음
-- 또한 순서에 맞춰서 잘 넣어줘야함 

SELECT * FROM 부서정보;


-- 만약 아직 부서장이 결정되지 않음 > 즉 매니저번호가 없음
INSERT INTO 부서정보 (부서번호, 부서이름, 지역번호) VALUES (30,'IT',1000);
-- 컬럼명을 지정해서 데이터를 삽입하면 지정위치에만 데이터를 삽입.


-- DELETE : 테이블에 데이터 삭제
DELETE FROM 부서정보;
-- 이렇게 명령어를 입력하면 부서정보 테이블에 있는 모든 데이터 삭제

-- 2,3 행만 지우고 싶음.
DELETE FROM 부서정보 WHERE 부서번호 = 20 OR 부서번호 = 30;

SELECT * FROM 직원정보;

-- 직원정보 테이블에 팀원들 정보 넣기 
-- 팀원들이 속한 부서는 3개 이상이어야 함.

-- SYSDATE : 현재날짜 현재시간
INSERT INTO 직원정보 VALUES (100,'승환',3000,10,SYSDATE);
-- 위 코드가 동작할 수 ㅣㅇㅆ었던 이유가 부서정보에 10, 'IT' 라는 정보를 미리 넣어줘서 가능함.!


INSERT INTO 부서정보 VALUES (20,'DATA',200,2000);
INSERT INTO 부서정보 VALUES (30,'마케팅',300,3000);

SELECT * FROM 부서정보;

INSERT INTO 직원정보 VALUES (200,'석진',4000,20,'25/04/12');
INSERT INTO 직원정보 VALUES (300,'서영',6000,30,'25/07/22');
INSERT INTO 직원정보 VALUES (201,'준서',5500,20,'25/08/11');
INSERT INTO 직원정보 VALUES (101,'승욱',5000,10,'25/12/30');
INSERT INTO 직원정보 VALUES (301,'은수',5000,30,SYSDATE);


-- 에러 발생했던 이유. 
-- 부서정보에 20,30인 데이터가 없으면 직원정보를 만들어도 삽입이 불가능함 > 참조 무결성의 위배.


-- 서브쿼리문을 사용해서 부서번호를 입력해도 됨
-- EX) 
SELECT 부서번호 FROM 부서정보
WHERE 부서이름 = '마케팅';

INSERT INTO 직원정보 VALUES (302,'영화',5000,
    (SELECT 부서번호 FROM 부서정보
    WHERE 부서이름 = '마케팅'),
    SYSDATE
);

-- UPDATE : 데이터 수정
UPDATE 직원정보 SET 급여 = 7000; -- >모든 급여가 7000으로 변경됨

UPDATE 직원정보 SET 급여 = 7000
WHERE 직원번호 = 100; -- > 조건을 걸어서 직원번호 100일때만 급여 7000으로 수정


--- 입사일에 있는 데이터를 각 팀원의 생일로 바꿔주세요
-- 동시에 한꺼번에 바꾸는 코드 있을까?
UPDATE 직원정보 SET 입사일 = '23/12/01'
WHERE 이름 = '석진';


DELETE FROM 부서정보 WHERE 부서정보 = 10;
-- 부서정보 테이블에서 부서정보를 직;원정보 테이블에서 이미 참조하고 있으므로 삭제되지 않음!
-- 1. 구조를 먼저 파악해야함 2. 데이터 결함이 발생할지 하지 않을지 고려해야함!

COMMIT;
-- TCL : 트랜잭션 제어어
-- COMMIT, ROLLBACK
-- COMMIT : 수행한 작업을 영구히 저장할 때 사용한다



SELECT * FROM 직원정보;
INSERT INTO 직원정보 VALUES (400,'해도',5000,20,SYSDATE);

COMMIT;
-- ROLLBACK : 마지막 COMMIT 시점으로 되돌릴때 사용한다




DELETE FROM 직원정보;
-- 모든 사람의 정보를 지움> 데이터에 대한 접근자. 테이블은 여전히 유지되어 있음.
-- 이런 데이터에 관련된 것들은 중간중간 커밋이 필요함.

ROLLBACK;
-- COMMIT을 DELETE이전에 했으므로 지우기 전으로 되돌아감!


-- DDL 명령은 AUTO COMMIT이기 때문에 주의해야함!
DROP TABLE 직원정보;
-- 이러면 테이블 전체를 날리는 거라 ROLLBACK을 시켜도 테이블을 찾을 수 없음.