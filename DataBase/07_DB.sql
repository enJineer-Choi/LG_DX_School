--(0305)
SELECT EMPLOYEE_ID, SALARY, DEPARTMENT_ID
FROM EMPLOYEES
WHERE (SALARY,DEPARTMENT_ID) IN (SELECT MAX(SALARY),DEPARTMENT_ID
                                    FROM EMPLOYEES
                                    GROUP BY DEPARTMENT_ID);    

-- VIEW : 가상의 테이블
-- 복잡한 SELECT문을 저장하기 위해 사용한다

-- 도시정보를 지금 현재 보여지는 테이블 옆에 보여지게 하고 싶음
-- 1.방법 > 서브쿼리와 조인을 통해서 할 수 있음 > 너무 쿼리문이 길어지고, 코드가 복잡해짐.
--
--SELECT EMPLOYEE_ID, SALARY,DEPARTMENT_ID, CITY
--FROM LOCATIONS,EMPLOYEES, DEPARTMENT
--WHERE 

-- 2. VIEW를 활용

CREATE VIEW 부서별최고급여 AS 
SELECT EMPLOYEE_ID, SALARY, DEPARTMENT_ID
FROM EMPLOYEES
WHERE (SALARY,DEPARTMENT_ID) IN (SELECT MAX(SALARY),DEPARTMENT_ID
                                    FROM EMPLOYEES
                                    GROUP BY DEPARTMENT_ID);    
                                    
-- VIEW를 생성 > 해당 쿼리문에 "부서별최고급여" 별칭을 붙여서 VIEW를 생성

-- 활용법
SELECT * FROM 부서별최고급여;

SELECT EMPLOYEE_ID, SALARY, MS.DEPARTMENT_ID , CITY
FROM LOCATIONS L, 부서별최고급여 MS, DEPARTMENTS D
WHERE MS.DEPARTMENT_ID = D.DEPARTMENT_ID AND D.LOCATION_ID = L.LOCATION_ID;
-- 부서별 최고급여 라는 것을 VIEW로 따로 정의하지 않으면 계속 작성해야하고, 코드의 가독성이 떨어짐.

-- 실습
-- 각 부서별 부서번호, 부서명, 도시명, 나라이름을 가지는 VIEW를 만들어주세요
CREATE VIEW  DEPARTVIEW AS
SELECT D.DEPARTMENT_ID, D.DEPARTMENT_NAME,L.CITY, C.COUNTRY_NAME
FROM DEPARTMENTS D,LOCATIONS L, COUNTRIES C
WHERE D.LOCATION_ID = L.LOCATION_ID AND L.COUNTRY_ID = C.COUNTRY_ID;




-- 각 도시별로 몇명이 근무하는 지 출력

-- 궁금한거 -> 직원수가 궁금함! 
-- 누가 어느도시에 근무하는 지가 연결 되어야함 > JOIN필요 (E.DEPATMENT_ID = DV.DEPARTMENT_ID)

SELECT * FROM DEPARTVIEW;

SELECT COUNT(E.EMPLOYEE_ID)
FROM DEPARTVIEW DV, EMPLOYEES E
WHERE E.DEPARTMENT_ID = DV.DEPARTMENT_ID
GROUP BY DV.DEPARTMENT_ID;
-- 이코드는 부서 아이디별로 묶는 코드임 .. > GROUP BY 를 CITY로 해야 도시별로 몇명 근무하는지를 알수 있음.
-- 일단 VIEW와EMPLOYEE 테이블을 조인 한다음에 DEPARTMENT ID로 GROUPBY 해서 EMPLOYEE_ID를 COUNT한다

SELECT CITY,COUNT(E.EMPLOYEE_ID)
FROM DEPARTVIEW DV, EMPLOYEES E
WHERE E.DEPARTMENT_ID = DV.DEPARTMENT_ID
GROUP BY CITY;


-- 시퀀스 : 연속된 숫자를 생성하는 객체
CREATE SEQUENCE 블로그시퀀스 
INCREMENT BY 1
START WITH 1 ;

ALTER TABLE 네이버블로그 DROP CONSTRAINT 블로그_회원ID_FK;

INSERT INTO 네이버블로그 VALUES (블로그시퀀스.NEXTVAL,'맛집','짜장면','TEST');
INSERT INTO 네이버블로그 VALUES (블로그시퀀스.NEXTVAL,'맛집','짬뽕','TEST');

SELECT * FROM 네이버블로그
WHERE ROWNUM <2;

-- TOP-N : 상위 N개만 출력하기! > 
-- ROWNUM : TOP-N과 함께 사용하는 키워드 
-- SELECT문을 통해 출력되는 행의 개수를 제한

-- 전 직원 중 제일 급여를 많이 받는 직원 상위 5명만 출력
-- 서브쿼리로 미리 정렬된 상태의 데이터에서 5명만 봅기
SELECT SALARY,FIRST_NAME FROM (SELECT SALARY,FIRST_NAME FROM EMPLOYEES ORDER BY SALARY DESC)
WHERE ROWNUM <=5 AND SALARY IS NOT NULL;


-- WHERE 조건이 더 우선순위이므로 밑의 코드처럼 작성하면 안됨.
SELECT SALARY,FIRST_NAME FROM EMPLOYEES
WHERE ROWNUM <=6
ORDER BY SALARY DESC;





