DELETE FROM customers WHERE customerNumber = 103;
-- 고객 번호가 103인 고객을 삭제합니다.
DELETE FROM products WHERE productCode = 'S10_1678';
-- 제품 코드가 'S10_1678'인 제품을 삭제합니다.
DELETE FROM employees WHERE employeeNumber = 1504;
-- 직원 번호가 1504인 직원을 삭제합니다.
DELETE FROM offices WHERE officeCode = '1';
-- 사무실 코드가 '1'인 사무실을 삭제합니다.
DELETE FROM orders WHERE orderNumber = 10100;
-- 주문 번호가 10100인 주문을 삭제합니다.
DELETE FROM orderdetails WHERE orderNumber = 10100 AND productCode = 'S10_1678';
-- 주문 번호 10100에서 제품 'S10_1678'에 대한 주문 상세를 삭제합니다.
DELETE FROM payments WHERE customerNumber = 103 AND checkNumber = 'HQ336336';
-- 고객 번호 103의 수표 번호 'HQ336336'에 대한 지불 내역을 삭제합니다.
DELETE FROM productlines WHERE productLine = 'Classic Cars';
-- 'Classic Cars' 제품 라인을 삭제합니다.
DELETE FROM customers WHERE city = 'Tokyo';
-- 도시가 'Tokyo'인 모든 고객을 삭제합니다.
DELETE FROM products WHERE productLine = 'Motorcycles';
-- 'Motorcycles' 제품 라인의 모든 제품을 삭제합니다.
