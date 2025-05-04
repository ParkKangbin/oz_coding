UPDATE customers SET address = '123 New Street' WHERE customerNumber = 103;
-- 고객 번호가 103인 고객의 주소를 '123 New Street'로 변경합니다.
UPDATE products SET buyPrice = 45.99 WHERE productCode = 'S10_1678';
-- 제품 코드 'S10_1678'의 가격을 45.99로 변경합니다.
UPDATE employees SET jobTitle = 'Sales Manager' WHERE employeeNumber = 1504;
-- 직원 번호 1504의 직급을 'Sales Manager'로 변경합니다.
UPDATE offices SET phone = '+1 123-456-7890' WHERE officeCode = '1';
-- 사무실 코드 '1'의 전화번호를 '+1 123-456-7890'으로 변경합니다.
UPDATE orders SET status = 'Shipped' WHERE orderNumber = 10100;
-- 주문 번호 10100의 상태를 'Shipped'로 변경합니다.
UPDATE orderdetails SET quantityOrdered = 25 WHERE orderNumber = 10100 AND productCode = 'S10_1678';
-- 주문 번호 10100의 제품 'S10_1678'의 수량을 25로 변경합니다.
UPDATE payments SET amount = 1500.00 WHERE customerNumber = 103 AND checkNumber = 'HQ336336';
-- 고객 번호 103의 수표 번호 'HQ336336'에 대한 금액을 1500.00으로 변경합니다.
UPDATE productlines SET textDescription = 'Updated description here' WHERE productLine = 'Classic Cars';
-- 'Classic Cars' 제품 라인의 설명을 'Updated description here'로 변경합니다.
UPDATE customers SET email = 'newemail@example.com' WHERE customerNumber = 103;
-- 고객 번호 103의 이메일을 'newemail@example.com'으로 변경합니다.
UPDATE products 
SET buyPrice = buyPrice * 1.1 
WHERE productLine = 'Motorcycles';
-- 'Motorcycles' 제품 라인의 모든 제품 가격을 10% 인상합니다.
