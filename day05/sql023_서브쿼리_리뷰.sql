-- 서브쿼리 리뷰

-- ALL, ANY(=SOME) : ANY(=SOME)를 사용하는 조건은 아래의 데이터로 활용이 어렵다.
-- Q. 3번 고객이 주문한 도서의 최고금액보다 더 비싼 도서를 구입한 다른 주문의 주문번호와 금액을 표시

/* 3번 고객 확인하기 */
SELECT *
FROM Customer

/* 3번 고객 장미란이 주문한 내역 중 최고 금액 */
SELECT MAX(saleprice)
FROM Orders
WHERE custid = 3;

-- 13,000원 보다 비싼 도서를 구입 한 주문번호와 금액을 표시
SELECT o1.orderid
     , o1.saleprice
FROM Orders AS o1
WHERE o1.saleprice > (SELECT MAX(saleprice)
                        FROM Orders
                       WHERE custid = 3);


-- EXISTS, NOT EXISTS : 열을 명시 하지 않음
-- Q. 대한민국 거주 고객에게 판매한 도서의 총판매액

/* 전체 판매액 : 118,000 대한민국 고객 판매액 46,000 */
SELECT SUM(saleprice) AS '대한민국 고객 판매액'
  FROM Orders AS o
 WHERE EXISTS (SELECT *
                 FROM Customer AS c
                WHERE c.address LIKE '%대한민국%'
                  AND c.custid = o.custid);

/* 조인으로도 금액을 찾을 수 있음 */
SELECT SUM(o.saleprice) AS '대한민국 고객 판매액'
  FROM Orders AS o, Customer AS c
 WHERE o.custid = c.custid
   AND c.address LIKE '%대한민국%';


-- SELECT절 서브쿼리(JOIN으로 변경 가능 다만 쿼리가 복잡해서 테이블을 추가하기 힘들면 서브쿼리 활용)
-- Q. 고객별 판매액을 확인하기

/* GROUP BY 활용 시 SELECT절에 반드시 집계함수가 들어가야 함 */
SELECT SUM(o.saleprice) AS '고객별 판매액'
  FROM Orders AS o
 GROUP BY o.custid;

/* 최종! */
SELECT SUM(o.saleprice) AS '고객별 판매액'
  -- , o.custid : 확인 했으면 줄 삭제보다 주석처리 권장
     , (SELECT [name] FROM Customer WHERE custid = o.custid) AS '고객명'
  FROM Orders AS o
 GROUP BY o.custid;


-- UPDATE에서도 사용 할 수 있음
-- 사전준비
ALTER TABLE Orders ADD bookname VARCHAR(40);

-- 업데이트 : 한꺼번에 필요한 필드값을 한 테이불에서 다른 테이블로 복사할 때 유용함
UPDATE Orders
   SET bookname = (SELECT bookname
                     FROM Book
                    WHERE Book.bookid = Orders.bookid);

-- FROM절 서브쿼리(인라인뷰[가상테이블])
-- Q. 고객별 판매액을 확인하기(서브쿼리 -> 조인)

/* 고객별 판매액 집계 쿼리가 FROM절에 들어가면 모든 속성(컬럼)에 이름 지정 필요 */
SELECT B.Total
     , C.name
  FROM (SELECT SUM(O.saleprice) AS 'Total'
             , O.custid
          FROM Orders AS O
         GROUP BY O.custid) AS B, Customer AS C
 WHERE B.custid = C.custid;


-- Q. 고객번호가 2이하인 고객의 판매액 확인하기

/* 주의! GROUP BY에 들어갈 속성(컬럼)은 최소화!! */
/* 중복이나 다른 문제 발생 시 결과가 모두 틀어짐 */
SELECT SUM(O.saleprice) AS '고객별 판매액'
     , (SELECT name FROM Customer WHERE custid = C.custid) AS '고객명'
  FROM(SELECT custid
            , [name]
         FROM Customer
        WHERE custid <=2) AS C, Orders AS O
 WHERE C.custid = O.custid
 GROUP BY C.custid;