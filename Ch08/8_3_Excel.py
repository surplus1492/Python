"""
2021/05/03
김영현
외부 패키지 설치 p239

(패키지 확인 파이썬 폴더 내의) venv(파이썬의 패키지 폴더) > Lib
(아래의 Terminal에 입력 : pip install openpyxl (외부 패키지 설치하는 명령문, Excel 파일 쓰기)
"""

from openpyxl import Workbook

# Excel 파일 쓰기

# Excel 파일 객체 생성
workbook = Workbook()

# 활성화된 sheet 선택
sheet = workbook.active

# 데이터 입력
sheet['A1'] = '홍길동'
sheet.append([1, 2, 3])
sheet.append(['김유신', '김춘추', '장보고'])
sheet.cell(6, 2, '사과')

# Excel 파일 저장/닫기
workbook.save('C:/Users/6기 김영현/Desktop/workspace/File Input,Output/Sample.xlsx')
workbook.close()

print('작업 종료 ')