"""
2021/04/30
김영현
파이썬 캡슐화 실습 p 161
"""


from Ch06.sub1.Account import Account

kb = Account('국민은행', '123-12-12345', '홍길동', 10000)
kb.deposit(40000)  # kb. 참조연산자
kb.withdraw(7000)

# 캡슐화시 불가능
# money -= 1

kb.show()
