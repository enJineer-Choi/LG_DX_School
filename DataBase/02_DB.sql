-- 0225 --



-- GROUP BY : 그룹으로 묶어서 (집계)데이터를 조회할 때 사용.
-- 전 직원이 근무하고있는 그룹별로 묶어서 출력
SELECT DEPARTMENT_ID FROM EMPLOYEES
GROUP BY DEPARTMENT_ID;
-- DEPARTMENT_ID 별로 묶인 결과값이 출력

-- 집계함수
-- 전체직원의 급여 총합
SELECT SUM(SALARY) FROM EMPLOYEES;

-- 전체직원 중 급여 최대값
SELECT MAX(SALARY) FROM EMPLOYEES;

--
SELECT COUNT(EMPLOYEE_ID) FROM EMPLOYEES;

--부서별 급여의 최소값을 출력
SELECT DEPARTMENT_ID,MIN(SALARY) FROM EMPLOYEES
GROUP BY DEPARTMENT_ID;

--부서별 급여의 평균값을 출력
SELECT DEPARTMENT_ID,AVG(SALARY) FROM EMPLOYEES
GROUP BY DEPARTMENT_ID;

-- 불가능 > GROUP BY가 우선실행되므로, GROUP BY 로 묶이면 누구의 이름을 가져와야할지 모름
SELECT MIN(SALARY),FIRST_NAME FROM EMPLOYEES
GROUP BY DEPARTMENT_ID;

-- 가능 > GROUP BY가 우선실행되도, DEPARTMENT_ID는 하나밖에 없으므로 가능
SELECT MIN(SALARY),DEPARTMENT_ID FROM EMPLOYEES
GROUP BY DEPARTMENT_ID;

-- 실습

--  성적표 테이블에서 학생별로 평균 점수를 출력해주세요!
SELECT 학생ID, ROUND(AVG(성적),2) FROM 성적표
GROUP BY 학생ID;
-- 소수점 자리 수 설정 : ROUND함수

-- 단, 성적이 NULL이 아닐때만
-- IS NULL / IS NOT NULL 
-- VER.1
SELECT 학생ID, ROUND(AVG(성적),2) FROM 성적표
WHERE 성적 IS NOT NULL
GROUP BY 학생ID;
-- 그룹으로 묶기 전에 NULL인 성적을 미리제외한 후, 학생ID로 GROUP BY

-- VER.2
SELECT 학생ID, ROUND(AVG(성적)) FROM 성적표
GROUP BY 학생ID
HAVING AVG(성적) IS NOT NULL;



-- 과목별로 최고성적과 최저성적을 출력해주세요!
SELECT MIN(성적),MAX(성적),과목 FROM 성적표
GROUP BY 과목;


-- 교육생 정보 테이블에서 각 팀에 몇명이 있는지 출력해주세요
SELECT 팀,COUNT(학생id) FROM 교육생정보
GROUP BY 팀;

-- 성적표 테이블에서 학생별로 파이썬을 제외한 나머지 과목의 평균을 출력
SELECT 학생ID,AVG(성적) FROM 성적표
WHERE 과목 NOT IN ('PYTHON')
GROUP BY 학생ID;

SELECT 학생ID,AVG(성적) FROM 성적표
WHERE 과목 IN ('JAVA','DATABASE')
GROUP BY 학생ID;

SELECT AVG(성적) FROM 성적표
WHERE  과목 != 'PYTHON'
GROUP BY 학생ID;

-- HAVING : GROUP BY로 묶여진 그룹에 조건을 걸어준다!(무조건 GROUP BY와 같이 쓰임)
-- 평균성적이 80점 이상인 학생들만 출력
SELECT 학생ID FROM 성적표
GROUP BY 학생ID
HAVING AVG(성적) >= 80;

-- 평균성적이 80점 이상인 학생들만 출력
SELECT 학생ID FROM 성적표
WHERE AVG(성적)>=80;
--에러 발생 ㅣ WHERE절에서는 집계함수 사용이 불가! > 왜냐하면 WHERE절은 행별로 조건을 걸어주는 방식이기 때문에...

-- 교육생 정보에서 소속된 팀원의 수가 3명이상인 팀만 출력
SELECT 팀 FROM 교육생정보
GROUP BY 팀
HAVING COUNT(팀)>=3;
--내가 짰던 코드

SELECT 팀 FROM 교육생정보
GROUP BY 팀
HAVING COUNT(학생ID)>=3;
-- 로직상 학생ID로 카운팅 하는게 맞다...


-- 부서별 최고연봉이 100,000이상인 부서번호를 출력
SELECT DEPARTMENT_ID FROM EMPLOYEES
GROUP BY DEPARTMENT_ID
HAVING MAX(SALARY)>=100000;
-- 에러가 계속 발생했던 이유... 100,000 중간에 콤마써서....
-- 로직은 맞게 하고 있었다... 

-- 연봉임!!
SELECT DEPARTMENT_ID,MAX(SALARY*12) FROM EMPLOYEES
GROUP BY DEPARTMENT_ID
HAVING MAX(SALARY*12)>=100000;
