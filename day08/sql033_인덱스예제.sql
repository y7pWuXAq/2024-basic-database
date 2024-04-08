-- 지난 주 잘못 생성 한 데이터를 전부 초기화(삭제)


/* 삭제 */
DELETE FROM Users; -- WHERE절이 없으면 모두 삭제하는 것.
-- 단, indentity(1,1)로 설정한 테이블에서 다시 1부터 넣도록 설정 하려면
-- 모두 삭제 후 초기화까지 진행 해야 함
TRUNCATE TABLE Users;


/* 200만건 더미데이터 생성 */
DECLARE @i INT;
SET @i = 0;

WHILE (@i < 2000000) -- 200만건
BEGIN
	SET @i = @i + 1;
	INSERT INTO Users (username, guildno, regdate)
	VALUES (CONCAT('user', @i), @i/100, DATEADD(dd, -@i/100, GETDATE()));
END;

-- 현재는 인덱스가 없는 상태
-- 100만건 정도의 데이터를 조회할 때 4~8초 시간 소요
-- 인덱스를 걸기 위해서 userid에 기본키(PK) 설정
ALTER TABLE Users ADD PRIMARY KEY(userid);

-- PK에 클러스터드 인덱스 설정됨

-- ! WHERE절에 검색을 위해서 username를 사용함
-- 인덱스를 PK에 거는 게 아니라 username 
CREATE CLUSTERED INDEX IX_Users_username ON Users(username);

DROP INDEX IX_Users_username ON Users;