-- 인덱스 : 책의 목차와 기능이 동일
-- Q. Book의 bookname 열에 넌클러스터링 인덱스 IX_Book_bookname을 생성하기
CREATE INDEX IX_Book_bookname ON BOOK(bookname);

-- Q. Customer의 name에 클러스터링 인덱스 CIX_Customer_name을 생성하기
-- 기본키에 클러스터드, 나머지 컬럼 넌클러스터드 인덱스 설정
CREATE CLUSTERED INDEX CIX_Customer_name ON Customer(name);

-- Book에 publisher, price 동시에 인덱스 IX_Book_pubprice 인덱스 생성
CREATE INDEX IX_Book_pubpric ON Book(publisher, price);