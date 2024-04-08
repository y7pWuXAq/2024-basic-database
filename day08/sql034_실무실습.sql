-- HR 데이터베이스 연습

-- SAMPLE 사원정보 테이블 사번, 이름, 급여, 입사일, 상사의 사원번호를 출력하세요.(107행)
SELECT employee_id
     , first_name + ' ' + last_name AS [name]
     , salary
     , hire_date
     , manager_id
  FROM Employees;


/* 사원정보에서 사원의 성과 이름을 name으로, 업무는 job, 급여는 salary,
    연봉에 $100 보너스를 추가해서 계산한 연봉은 Increased Ann Salary,
    월급에 $100 추가해서 Increased Salary의 별칭으로 출력 */
SELECT first_name + ' ' + last_name AS 'name'
     , job_id AS 'job'
     , salary
     , (salary * 12) + 100 AS 'Increased Ann Salary'
     , (salary + 100) * 12 AS 'Increased Salary'
  FROM Employees;

/* 2. 사원정보의 모든 사원에 Last name에 Last name : 1 Year Salary = $연봉 양식으로
      컬럼에 1 Year Salary 별칭을 붙이시오 */
SELECT last_name + ' : 1 Year Salary = $' + CONVERT(VARCHAR,(salary * 12)) AS '1 Year Salary'
  FROM employees;

/* 3. 부서별 담당하는 업무를 한 번씩 출력하세요 (20행) */
SELECT DISTINCT department_id
     , job_id
  FROM employees;

-- WHERE, ORDER BY
/* SAMPLE : hr 부서에서 예산 문제로 급여 정보 보고서를 작성.
사원 정보에서 급여가 7000 ~ 10000이외의 사람과 성과 이름 급여를 급여가 작은 순으로 출력(75행) */
SELECT first_name + ' ' + last_name AS 'name'
     , salary
  FROM employees
 WHERE salary NOT BETWEEN 7000 AND 10000
 ORDER BY salary ASC;


/* 4. last name에 e나 o로 시작하는 사원을 출력 (10행) */
SELECT last_name AS 'e and o Name'
  FROM employees
 WHERE last_name LIKE '%e%' AND last_name LIKE '%o%'

/* 5. 현재의 날짜 타입을 날자 함수를 통해 확인 2006년 5월 20일부터 2007년 5월 20일 사이에
고용된 사원의 이름(First + Last), 사원번호, 고용일자 단, 입사일 빠른 순으로 (18행) */
SELECT GETDATE()