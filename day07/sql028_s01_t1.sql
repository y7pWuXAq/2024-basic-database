-- 트랜잭션 1

BEGIN TRANSACTION;
USE madang;

SELECT *
FROM Book
WHERE bookid = 1;

UPDATE book
SET price = 7100
WHERE bookid = 1;

SELECT *
FROM book
WHERE bookid = 1;

ROLLBACK;
COMMIT;