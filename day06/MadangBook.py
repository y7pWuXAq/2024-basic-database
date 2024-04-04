## 파이썬 DB 연동 프로그램

import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import webbrowser
from PyQt5.QtWidgets import QWidget

## MSSQL 연동할 라이브러리(모듈)
import pymssql

## 전역변수(나중에 여기만 변경하면 편함)
severName = '127.0.0.1'
userId = 'sa'
userPass = 'mssql_p@ss'
dbName = 'Madang'
dbCharset = 'UTF8' # EUC-KR 설정 금지!

# 저장 선택 시 삽입, 수정을 구분하기 위한 구분자
mode = 'I' # U / I : Insert, U : Update


class qtApp(QMainWindow) :
    def __init__(self) -> None :
        super().__init__()
        uic.loadUi('./day06/MadangBook.ui', self)
        self.initUI()

    def initUI(self) -> None :
        # 입력제한
        self.txtBookId.setValidator(QIntValidator(self)) # 숫자만 입력하도록 제한
        self.txtPrice.setValidator(QIntValidator(self)) # 숫자만 입력하도록 제한

        # Button 4개에 대해서 사용 등록
        self.btnNew.clicked.connect(self.btnNewClicked) # 신규버튼 이벤트에 대한 슬롯함수 생성
        self.btnSave.clicked.connect(self.btnSaveClicked) # 저장
        self.btnDel.clicked.connect(self.btnDelClicked) # 삭제
        self.btnReload.clicked.connect(self.btnReloadClicked) # 조회
        self.tblBooks.itemSelectionChanged.connect(self.tblBooksSelected) # 테이블위젯 결과를 클릭 시 발생
        self.show()

        self.btnReloadClicked() # 함수 실행 시 조회버튼 자동 클릭

    def btnNewClicked(self): # 신규 버튼 선택 시
        # QMessageBox.about(self,'버튼', '신규버튼 선택')
        global mode # 전역변수 사용
        mode = 'I'
        self.txtBookId.setText('')
        self.txtBookName.setText('')
        self.txtPublisher.setText('')
        self.txtPrice.setText('')
        
        # 선택한 데이터에서 신규를 누르면 self.txtBookId를 사용가능 하도록 변경
        self.txtBookId.setEnabled(True)

    def btnSaveClicked(self): # 저장 버튼 선택 시
        # QMessageBox.about(self,'버튼', '저장버튼 선택')
        
        # 입력검증(Validation Check) 꼭!
        # 1. 텍스트박스를 비워두고 저장버튼 누르면 X!!
        bookId = self.txtBookId.text()
        bookName = self.txtBookName.text()
        publisher = self.txtPublisher.text()
        price = self.txtPrice.text()

        # print(bookId, bookName, publisher, price)
        warningMsg = '' # 경고 메세지
        isValid = True # 빈 값이 있으면 False로 변경
        if bookId == None or bookId == '' :
            warningMsg += '번호를 입력하세요.\n'
            isValid = False
        if bookName == None or bookName == '' :
            warningMsg += '제목울 입력하세요.\n'
            isValid = False
        if publisher == None or publisher == '' :
            warningMsg += '출판사를 입력하세요.\n'
            isValid = False
        if price == None or price == '' :
            warningMsg += '정가를 입력하세요.\n'
            isValid = False        
        
        if isValid == False : # 위 입력값 중 하나라도 빈값이 존재하면
            QMessageBox.warning(self, '경고', warningMsg)
            return
        
        # Mode = 'I' 일 때는 중복번호를 체크해야 하지만 Mode = 'U'일 때는 체크해서 막으면 수정이 불가함
        print(mode)
        if mode == 'I' :
        # 2. 현재 존재하는 번호를 사용했는지 체크, 이미 있는 번호면 DB입력 쿼리 실행이 안되도록 막기
            conn = pymssql.connect(server=severName, user=userId, password=userPass, database=dbName, charset=dbCharset)
            cursor = conn.cursor(as_dict = False)  # COUNT(*)는 데이터가 딱 1개 이때문에 as_dict(딕셔너리)를 False로 해야 함
            
            query = f'''SELECT COUNT(*)
                        FROM Book
                        WHERE bookid = {bookId}''' # 현재 입력하고자 하는 번호가 있는지 확인하는 쿼리
            
            cursor.execute(query)
            # print(cursor.fetchone()[0]) # COUNT(*)는 데이터가 딱 1개 이때문에 cursor.fetchone() 함수로 (1, ) 튜플을 가져옴
            valid = cursor.fetchone()[0]

            if valid == 1 : # DB Book 테이블에 같은 번호가 이미 존재한다는 뜻
                QMessageBox.warning(self, '경고', '이미 있는 번호입니다.\n번호를 변경하세요.')
                return

        # 3. 입력검증 후 DB Book 테이블에 삽입 시작
        # bookId, bookName, publisher, price
        if mode == 'I' :
            query = f'''INSERT INTO Book
                    VALUES ({bookId}, N'{bookName}', N'{publisher}', {price})'''
        elif mode == 'U' : # 수정
            query = f'''UPDATE Book
                           SET bookname = N'{bookName}'
                             , publisher = N'{publisher}'
	                         , price = {price}
                         WHERE bookid = {bookId}'''
        conn = pymssql.connect(server=severName, user=userId, password=userPass, database=dbName, charset=dbCharset)
        cursor = conn.cursor(as_dict = False) # INSERT는 데이터를 가져오는게 아니라서!

        try : 
            cursor.execute(query)
            conn.commit() # 저장을 확립!
            
            if mode == 'I' : # 신규 추가 일 때
                QMessageBox.about(self, '안내', '도서 정보를 저장했습니다.')
            else : # 기존 데이터 수정
                QMessageBox.about(self, '안내', '도서 정보를 수정했습니다.')
       
        except Exception as e :
            QMessageBox.warning(self, '경고', f'{e}')
            conn.rollback() # 원상복구
        finally :
            conn.close() # 오류가 있어도, 없어도 DB를 닫기
        
        self.btnReloadClicked() # 함수 실행 시 조회버튼 자동 클릭
    

    def btnDelClicked(self): # 삭제 버튼 선택 시
        # QMessageBox.about(self,'버튼', '삭제버튼 선택')
        # 삭제기능
        bookId= self.txtBookId.text()
        # Validation Check
        if bookId == None or bookId == '' :
            QMessageBox.warning(self, '경고', '도서 번호 없이 삭제할 수 없습니다.')
            return
        
        # 삭제 여부 확인
        re = QMessageBox.question(self, '경고', '삭제하시겠습니까?', QMessageBox.Yes | QMessageBox.No)
        if re == QMessageBox.No :
            return

        conn = pymssql.connect(server=severName, user=userId, password=userPass, database=dbName, charset=dbCharset)
        cursor = conn.cursor(as_dict = False)
        query = f'''DELETE FROM Book
                    WHERE bookid = {bookId}'''
        
        try :
            cursor.execute(query)
            conn.commit()

            QMessageBox.about(self, '안내', '삭제가 완료 되었습니다.')
        except Exception as e :
            QMessageBox.warning(self, '경고', f'{e}')
            conn.rollback()
        finally :
            conn.close()
        
        self.btnReloadClicked() # 함수 실행 시 조회버튼 자동 클릭

    def btnReloadClicked(self): # 조회 버튼 선택 시
        # QMessageBox.about(self,'버튼', '조회버튼 선택')
        listResult = []
        conn = pymssql.connect(server=severName, user=userId, password=userPass, database=dbName, charset=dbCharset)
        cursor = conn.cursor(as_dict = True)

        query = '''
                SELECT bookid
                     , bookname
                     , publisher
                     , ISNULL(FORMAT(price, '#,#'), '-') AS price
                    FROM Book
                '''
        cursor.execute(query)

        for row in cursor :
            # print(f'bookid = {row["bookid"]}, bookname = {row["bookname"]}, publisher = {row["publisher"]}, price = {row["price"]}')
            # dictionary로 만든 결과를 listResult에 append()하기
            temp = {'bookid' : row["bookid"], 'bookname' : row["bookname"], 'publisher' : row["publisher"], 'price' : row["price"]}
            listResult.append(temp)
            
        conn.close() # DB는 접속해서 일이 끝나면 무조건 닫기
       
        # print(listResult) # tblBooks 테이블 위젯에 표시
        self.makeTable(listResult)

    def makeTable(self, data) : # tblBooks 위젯을 데이터와 컬럼 생성해주는 함수
        # print(len(data)) # 행의 갯수 확인하기
        self.tblBooks.setColumnCount(4) # bookid, bookname, publisher, price
        self.tblBooks.setRowCount(len(data)) # 조회에서 나온 리스트의 갯수로 결정
        self.tblBooks.setHorizontalHeaderLabels(['번호', '제목', '출판사', '정가']) # 커ㅗㄹ럼 설정

        n = 0
        for item in data : # 테이블 위젯에 데이터 표시하기
            print(item)

            idItem = QTableWidgetItem(str(item['bookid']))
            idItem.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter) # 책번호 정렬
            self.tblBooks.setItem(n, 0, idItem) # set(row, column, text)

            self.tblBooks.setItem(n, 1, QTableWidgetItem(item['bookname'])) # 책이름
            self.tblBooks.setItem(n, 2, QTableWidgetItem(item['publisher'])) # 출판사

            priceItem = QTableWidgetItem(str(item['price']))
            priceItem.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            self.tblBooks.setItem(n, 3, priceItem) 

            n += 1

        # 컬럼의 넓이 수정하기
        self.tblBooks.setColumnWidth(0, 65) # 책번호 컬럼의 넓이
        self.tblBooks.setColumnWidth(1, 230) # 책제목 컬럼의 넓이
        self.tblBooks.setColumnWidth(2, 130) # 출판사 컬럼의 넓이
        self.tblBooks.setColumnWidth(3, 80) # 책가격 컬럼의 넓이

        # 컬럼 더블클릭 금지
        self.tblBooks.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def tblBooksSelected(self): # 조회결과 테이블위젯 내용 클릭
        # QMessageBox.about(self,'테이블위젯', '내용 변경')
        rowIndex = self.tblBooks.currentRow() # 현재 마우스로 선택한 행의 인덱스

        bookId = self.tblBooks.item(rowIndex, 0).text() # 책번호
        bookName = self.tblBooks.item(rowIndex, 1).text() # 책제목
        publisher = self.tblBooks.item(rowIndex, 2).text() # 출판사
        price = self.tblBooks.item(rowIndex, 3).text().replace(',','') # 가격
        # print(bookId, bookName, publisher, price) # 차후 디버깅 시 필요

        # 지정된 lineEdit(TextBox)에 각각 할당하기
        self.txtBookId.setText(bookId)
        self.txtBookName.setText(bookName)
        self.txtPublisher.setText(publisher)
        self.txtPrice.setText(price)

        # 모드를 Update로 변경
        global mode 
        mode = 'U'

        #txtBookId를 사용하지 못하게 설정
        self.txtBookId.setEnabled(False)


    # 원래 PyQt에 있는 함수 closeEvent를 재정의(Override)
    def closeEvent(self, event) -> None:
        re = QMessageBox.question(self, '종료', '종료하시겠습니까?', QMessageBox.Yes | QMessageBox.No)
        if re == QMessageBox.Yes:
            event.accept() #프로그램 종료
        else : event.ignore()

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    inst = qtApp()
    sys.exit(app.exec_())

