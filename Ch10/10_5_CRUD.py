"""
2021/05/20
김영현
DateBase SQL 실습
"""

"""
약자 , 의미   sql문 
C = create -> insert
R = read ->select
U = update -> update
D = delete -> delete
"""

import pymysql

conn = pymysql.connect(host='192.168.10.114', user='dudgus960408', password='1234', db='dudgus960408', charset='utf8')

while True:
    print('0: 종료, 1: 등록, 2: 조회, 3:검색, 4: 삭제')
    result = int(input('입력 : '))

    if result == 0:
        break
    elif result == 1:
        uid = input('아이디 입력 : ')
        name = input('이름 입력 : ')
        hp = input('휴대폰 입력 : ')
        age = input('나이 입력 : ')

        cur = conn.cursor()

        sql = "INSERT INTO `USER1` VALUES ('%s','%s','%s',%s);"
        cur.execute(sql % (uid, name, hp, age))
        conn.commit()

        print('입력 성공')
    elif result == 2:
        cur = conn.cursor()
        sql = "SELECT * FROM `USER1`;"
        cur.execute(sql)

        for row in cur.fetchall():
            print('-------------------')
            print('아이디 : ', row[0])
            print('이름 : ', row[1])
            print('전화번호 : ', row[2])
            print('나이 : ', row[3])
            print('-------------------')

    elif result == 3:
        uid = input('검색할 아이디 : ')

        cur = conn.cursor()

        sql = "SELECT * FROM `USER1` WHERE `uid`='%s';"
        cur.execute(sql % uid)
        rows = cur.fetchall()

        if len(rows) == 0:
            print('검색 결과가 없습니다')
        else:
            for row in rows:
                print('-------------------')
                print('아이디 : ', row[0])
                print('이름 : ', row[1])
                print('전화번호 : ', row[2])
                print('나이 : ', row[3])
                print('-------------------')

    elif result == 4:
        uid = input('삭제할 아이디 : ')

        cur.execute()

        sql = "DELETE FROM `USER1` WHERE `uid`='%s';"
        rs = cur.execute(sql % uid)
        conn.commit()

        if rs > 0:
            print('삭제 성공')
        else:
            print('삭제할 아이디가 없습니다')

conn.close()

print('종료합니다')
