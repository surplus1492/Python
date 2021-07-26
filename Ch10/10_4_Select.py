"""
2021/05/20
김영현
DateBase SQL 실습
"""

import pymysql

# DB 접속
conn = pymysql.connect(host='192.168.10.114', user='dudgus960408', password='1234', db='dudgus960408', charset='utf8')

# SQL 실행 객체 생성
cur = conn.cursor()

# SQL 실행
sql = "SELECT * FROM `USER1`;"
cur.execute(sql)

# SQL 결과 출력
for row in cur.fetchall():
    print('--------------------------')
    print('아이디 :', row[0])
    print('이름 :', row[1])
    print('휴대폰 :', row[2])
    print('나이 :', row[3])
    print('--------------------------')

# DB 종료
conn.close()

print('Select 종료')
