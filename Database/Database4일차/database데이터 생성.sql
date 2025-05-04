-- use mydatabase;
-- customers 테이블 생성: 고객 정보를 저장
CREATE TABLE customers (
    id INT PRIMARY KEY,          -- 고객 ID (고유값)
    name VARCHAR(50),            -- 고객 이름 (최대 50자)
    country VARCHAR(50)          -- 고객 국가 (최대 50자)
);

-- products 테이블 생성: 제품 정보를 저장
CREATE TABLE products (
    id INT PRIMARY KEY,          -- 제품 ID (고유값)
    name VARCHAR(50),            -- 제품 이름
    category VARCHAR(50)         -- 제품 카테고리
);

-- employees 테이블 생성: 직원 정보를 저장
CREATE TABLE employees (
    id INT PRIMARY KEY,          -- 직원 ID
    name VARCHAR(50),            -- 직원 이름
    title VARCHAR(50)            -- 직책 (예: 영업사원, 관리자)
);

-- offices 테이블 생성: 사무실 정보를 저장
CREATE TABLE offices (
    id INT PRIMARY KEY,          -- 사무실 ID
    city VARCHAR(50)             -- 도시명
);

-- orders 테이블 생성: 주문 정보를 저장
CREATE TABLE orders (
    id INT PRIMARY KEY,          -- 주문 ID
    customer_id INT,             -- 주문한 고객 ID (customers 테이블 참조 가능)
    order_date DATE              -- 주문 날짜
);

-- orderdetails 테이블 생성: 주문의 상세 항목을 저장
CREATE TABLE orderdetails (
    order_id INT,                -- 주문 ID
    product_id INT,              -- 주문된 제품 ID
    quantity INT                 -- 주문 수량
);

-- payments 테이블 생성: 결제 정보를 저장
CREATE TABLE payments (
    id INT PRIMARY KEY,          -- 결제 ID
    customer_id INT,             -- 고객 ID
    amount DECIMAL(10,2)         -- 결제 금액 (소수 둘째 자리까지)
);

-- productlines 테이블 생성: 제품 라인(분류)을 저장
CREATE TABLE productlines (
    id INT PRIMARY KEY,          -- 제품 라인 ID
    name VARCHAR(50)             -- 제품 라인 이름
);


