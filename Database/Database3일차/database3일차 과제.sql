-- use mydatabase;
-- 테이블 만들기 
-- CREATE TABLE employees(
	-- id INT auto_increment primary key,
	-- name VARCHAR (100),
    -- position VARCHAR (100),
    -- salary DECIMAL (10,2)
   -- );

-- use mydatabase; 직원 데이터 추가 
-- insert into employees (name,position,salary) values('해린','PM',90000);
-- INSERT INTO employees (name,position,salary) values('은우','Frontend',80000);
-- insert into employees (name,position,salary) values('가을','Backend',92000);
-- INSERT INTO employees (name, position, salary) VALUES ('지수', 'Frontend', 78000);
-- INSERT INTO employees (name, position, salary) VALUES ('민혁', 'Frontend', 96000);
-- INSERT INTO employees (name, position, salary) VALUES ('하온', 'Backend', 130000);
    
-- select * from employees 연봉이 90000 이하인 직원 조회
-- SELECT name, salary FROM employees WHERE position = 'Frontend' AND salary <= 90000;
-- UPDATE employees SET salary = salary * 1.10 WHERE position = 'PM';
-- UPDATE employees SET salary = salary * 1.05 WHERE position = 'Backend';
-- DELETE FROM employees WHERE name = '민혁';
SELECT position, AVG(salary) AS average_salary FROM employees GROUP BY position;
DROP TABLE employees;