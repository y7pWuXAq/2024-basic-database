-- VIEW

-- Q. 고객명과 책이름을 같이 볼 수 있는 주문 뷰를 만들기

/* 기본 */
SELECT o.orderid
     , o.custid
     , c.name
     , o.bookid
     , b.bookname
     , o.saleprice
     , b.price
     , o.orderdate
  FROM Customer AS c, Orders AS o, Book AS b
 WHERE c.custid = o.custid
   AND o.bookid = b.bookid


/* VIEW 사용하기 */
CREATE VIEW v_orderdetail
    AS
SELECT o.orderid
     , o.custid
     , c.name
     , o.bookid
     , b.bookname
     , o.saleprice
     , b.price
     , o.orderdate
  FROM Customer AS c, Orders AS o, Book AS b
 WHERE c.custid = o.custid
   AND o.bookid = b.bookid;


-- Q. 대한민국 고객으로 구성된 뷰 만들기
CREATE VIEW v_kcustomer
    AS
SELECT *
  FROM Customer
 WHERE [address] LIKE '%대한민국%';

/* 조회 */
SELECT *
  FROM v_kcustomer

/* 뷰를 사용해서 데이터 입력, 삭제도 가능함 */
INSERT INTO v_kcustomer
VALUES (6, '손흥민', '대한민국 강원도', '010-9876-1234');

/* v_orderdetail, JOIN으로 만든 뷰는 삽입, 수정, 삭제 불가 */
INSERT INTO v_orderdetail
VALUES (11, 6, '손흥민', 1, '축구의 역사', 6500, 7000, '2024-04-03');

/* 단!! 뷰에는 되도록 삽입, 수정, 삭제를 하지 말 것 */
DROP VIEW v_kcustomer

-- 시스템 뷰, DBMS가 미리 만들어 둔 뷰들
-- 내 데이터 베이스에 있는 DB 종류
SELECT * FROM sys.databases;

SELECT * FROM INFORMATION_SCHEMA.COLUMNS
 WHERE TABLE_NAME = 'Book';