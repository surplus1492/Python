from Ch06.sub1.Account import Account


class StockAccount(Account):

    def __init__(self, bank, id, name, money, stock, amount, price):
        super().__init__(bank, id, name, money)  # 부모 클래스 상속
        self.stock = stock
        self.amount = amount
        self.price = price

    def sell(self, amount, price):
        print('{}를 {}개 {}가격에 판매'.format(self.stock, amount, price))

    def buy(self, amount, price):
        print('{}를 {}개 {}가격에 구매'.format(self.stock, amount, price))

    def show(self):
        super().show()  # override 자식이 불러온 부모 클래스를 덮어 씌움
        print('주식종목 :', self.stock)
        print('주식수량 :', self.amount)
        print('주식가격 :', self.price)
