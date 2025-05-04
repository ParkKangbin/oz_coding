use mydatabase;
SELECT * FROM customers;  
-- customers 테이블의 모든 열(*)을 가져옵니다.
SELECT * FROM products;  
-- products 테이블의 전체 데이터를 조회합니다.
SELECT name, title FROM employees;  
-- employees 테이블에서 name(이름)과 title(직급) 열만 가져옵니다.
SELECT city FROM offices;  
-- offices 테이블에서 city(도시)만 조회합니다.
SELECT * FROM orders  
			
SELECT * FROM orders  
ORDER BY order_date DESC  -- 주문일을 기준으로 최신 순으로 정렬하고
LIMIT 10;                 -- 위에서 10개만 가져옵니다.
            
SELECT * FROM orderdetails  
WHERE order_id = 5001;  
-- order_id가 5001인 주문의 상세 정보를 조회합니다.

SELECT * FROM payments  
WHERE customer_id = 1;  
-- 고객 ID가 1인 사람의 결제 내역을 조회합니다.
SELECT name FROM productlines;  
-- productlines 테이블에서 name(제품 라인 이름)을 조회합니다.
SELECT * FROM customers  
WHERE country = 'Korea';  
-- country가 'Korea'인 고객 정보를 조회합니다.
SELECT * FROM products  
WHERE price BETWEEN 10000 AND 50000;  
-- 가격이 10,000원 이상 50,000원 이하인 제품만 조회합니다.

