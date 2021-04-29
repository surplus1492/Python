"""
2021/04/29
김영현
Class 실습 p148
"""

"""
# Class 정의
class Account:  # class는 일반적으로 대문자 시작
    # 속성
    def __init__(self, bank, id, name, money):
        self.bank = bank
        self.id = id
        self.name = name
        self.money = money

    # 기능
    def deposit(self, money):
        self.money += money

    def withdraw(self, money):
        self.money -= money

    def show(self):
        print('------------------------')
        print('은행명 :', self.bank)
        print('계좌번호 :', self.id)
        print('입금주 :', self.name)
        print('현재잔액 :', self.money)
"""

from Ch06.sub1.Account import Account  # 불러올 파일의 출처를 써줌
from Ch06.sub1.Computer import Computer

# 객체 생성
kb = Account('국민은행', '123-12-12345', '홍길동', 10000)
kb.deposit(40000)  # kb. 참조연산자
kb.withdraw(7000)
kb.show()

wr = Account('우리은행', '234-23-12345', '김춘추', 30000)
wr.deposit(10000)
wr.withdraw(5000)
wr.show()

# Computer 객체 생성
samsung = Computer('삼성', 'Intel i7', '16GB', '1TB')
imac = Computer('애플', 'Intel i7', '32B', '1TB')

samsung.info()
imac.info()
