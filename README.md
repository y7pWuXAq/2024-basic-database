# 2024-basic-database
IoT 개발자과정 SQLSever 학습 리포지토리


### 1일차
- NS SQL Sever 설치 : https://www.microsoft.com/ko-kr/sql-server/sql-server-downloads 2022 최신버전
    - DBMS 엔진 설치 : 개발자 버전(ios 다운로드 후 설치 추천!!)
        - SQL Sever에 대한 Azure 확장은 비활성화 후 진행

        ![기능선택](https://github.com/y7pWuXAq/2024-basic-database/blob/main/images/db001.png)

        - 중요!! 데이터베이스 엔진 구성
            - Windows 인증 모드로 설치 시 외부에서 접근 불가, 혼합 모드로 설치
            - 혼합 모드(sa)에 대한 암호를 지정 / mssql_p@ss (8자 이상, 대소문자 구분, 특수문자 1개)
            - 데이터 루트 디렉토리는 변경 필요
    - [개발툴 설치](https://learn.microsoft.com/ko-kr/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16)
        - SSMS(SQL Sever Management Studio) DB에 접근, 여러 개발 작업을 할 수 있는 개발 도구
        
- 데이터베이스 개념
    - 데이터를 보과느 관리, 서비스하는 시스템
    - Data, Infomation, Knowlege 개념
    - DBMS > Database > data(Model)

- DB 언어
    - SQL(Structured Query Languge) : 구조화 된 질의 언어
        - DDL(Data Definition Lang) : 데이터 베이스 테이블, 인덱스 생성
        - DML(Data Manipulation Lang) : 제어, 검색, 삽입, 수정, 삭제 등 기능
        - DCL(Data Control Lang) : 보안, 권한 부여 or 제거 가능
        - TCL(Transaction) : 트랜스액션을 제어 하는 기능 COMMIT(확립), ROLLBACK(되돌리기)

- SQL 기본 학습
    - SSMS 실행

    ![SSMS 로그인](https://github.com/y7pWuXAq/2024-basic-database/blob/main/images/db002.png)

    - 특이사항 : SSMS 쿼리 창에서 소스코드 작성 시 빨간색 오류 및줄이 가끔 표현됨 (모두 오류는 아님!)

- DML 학습
    - SQL 명령어 키워드 : SELECT, INSERT, UPDATE, DELETE
    - IT 개발 표현 언어 : Request, Create, Update, Deletd(CRUD로 부름)
    - SELECT
        ```sql
        SELECT [ALL | DISTINCT] 속성이름(들)
        FROM 테이블이름(들)
        WHERE 검색조건(들) : 옵션이라 없어도 상관X
        GROUP BY 속성이름(들)
        HAVING 검색조건 (들)
        ORDER BY 속성이름(들) [ASC | DESC]
        ```
    - SELECT 문 학습
        - 기본, 조건검색 학습

### 2일차
- Database 학습
    - DB 개발시 사용할 수 있는 툴
        - SSMS : 기본 개발 툴
        - Visual Studio : 아무런 설치 없이 개발 가능
        - Visual Studio Code : SQL Sever(mssql) 플러그인 설치 필요
    - SeverName(HostName) : 내 컴퓨터 이름 | 내 네트워크 주소 | locahost(LoopBack URL) | 127.0.0.1(LoopBack IP)
    - 관계 데이터 모델
        - 릴레이션 : 행과 열로 구성 된 테이블(관계 데이터모델에서만 적용)
            - 행, 튜플, 열, 속성, 스키마, 인스턴스 용어
        - 매핑되는 이름 테이블(실제 DB)
            - 행, 레코드, 열, 컬럼, 컬럼이름, 데이터
        - 차수(degee) : 속성의 개수
        - 카디날리(cardinality) : 튜플의 수

        - 릴레이션의 특징
            - 속성은 단일값을 가짐(한 칸에 한 이름만)
            - 속성은 다른 이름으로 구성 되어야 함(속성이 중복될 수 없다)
            - 속성의 값은 정의된 도메인값만 가짐
            - 속성의 순서는 상관 없음
            - 릴레이션 내 중복된 튜플 허용 안함(동일한 내용의 정보가 있을 수 없음)
            - 튜플 순서는 상관 없음

        - 관계 데이터 모델은 아래의 요소로 구성됨
            - 릴레이션(Relation)
            - 제약조건(Constraints)
            - 관계대수(Relation algebra)

- DML 학습
    - SELECT문 
        - 복합조건, 정렬
        - 집계함수와 GROUP BY
            - SUM(총합), AVG(평균), COUNT(개수), MIN(최소), MAX(최대값)
            - 집계함수 외 일반 컬럼은 GROUP BY 절에 속한 컬럼만 SELECT문에 사용가능 
            - HAVING은 집계함수의 필터로 GROUP BY 뒤에 작성. WHERE절과 필터링이 다르다.

        - 두개 이상의 테이블 질의(Query)
            - 관계형 DB에서 가장 중요한 기법중 하나 : JOIN!
            - INNER JOIN(내부 조인) [참조](https://sql-joins.leopard.in.ua/)
            - LEFT|RIGHT OUTER JOIN(외부 조인) - 어느 테이블이 기준인지에 따라서 결과가 상이함

        ![외부조인](https://github.com/y7pWuXAq/2024-basic-database/blob/main/images/db004.png)