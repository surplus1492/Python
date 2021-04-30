"""
2021/04/30
김영현
파이썬 클래스 상속 실습 p 163
"""

from Ch06.sub2.StockAccount import StockAccount

kb = StockAccount('kb금융', '111-11-11111', '김유신', 10000, '삼성전자', 10, 8000)
kb.deposit(40000)
kb.withdraw(5000)
kb.buy(10, 80000)
kb.sell(10, 80000)

kb.show()
