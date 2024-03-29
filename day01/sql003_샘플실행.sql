-- 책중에서 '축구의 역사' 도서의 출판사와 가격을 알고싶어.
-- dbo는 DataBase Owner(지금은 몰라도 OK)
SELECT publisher, price
  FROM Book
 WHERE bookname = '축구의 역사';

 /*
	- SQL에서는 == 연산자 사용 X , = 사용
	- 문자열에 "" 사용 X , '' 사용
	- 대소문자 구분 X, 하지만 키워드는 대문자로 사용
	- 문장 끝에 ; 필수 X 하지만 중요한 사항에서는 사용
 */

 -- 김연아 고객의 전화번호를 찾으세요.
 
 -- 1 step
SELECT * -- * 기호는 ALL 이라고 호칭
  FROM Customer;

-- 2 step
SELECT *
  FROM Customer
 WHERE [name] = '김연아';

-- 3 step
SELECT phone
  FROM Customer
 WHERE [name] = '김연아';