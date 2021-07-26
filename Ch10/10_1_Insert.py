"""
2021/05/20
김영현
DateBase SQL 실습
"""

import pymysql

# DB 접속
conn = pymysql.connect(host='192.168.10.114', user='dudgus960408', password='1234', db='dudgus960408', charset='utf8')

# SQL 실행 객체 생성
cur=conn.cursor()

# SQL 실행
sql="INSERT INTO `USER1` VALUES ('p102','김춘추','010-124-1002',23);"
cur.execute(sql)
conn.commit()

# DB 종료
conn.close()

print('Insert 완료')