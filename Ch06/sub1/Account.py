# Class 정의
class Account:  # class는 일반적으로 대문자 시작
    # 속성
    def __init__(self, bank, id, name, money):
        self.__bank = bank # python은 __두번 java 에서는 private => 캡슐화 ,은닉화
        self.__id = id
        self.__name = name
        self.__money = money

    # 기능
    def deposit(self, money):
        self.__money += money

    def withdraw(self, money):
        self.__money -= money

    def show(self):
        print('------------------------')
        print('은행명 :', self.__bank)
        print('계좌번호 :', self.__id)
        print('입금주 :', self.__name)
        print('현재잔액 :', self.__money)