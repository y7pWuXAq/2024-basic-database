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
        - DCL(Data Control Lang) : 권한 부여 or 제거 가능, 

- SQL 기본 학습
    - SSMS 실행

    ![SSMS 로그인](https://github.com/y7pWuXAq/2024-basic-database/blob/main/images/db002.png))

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