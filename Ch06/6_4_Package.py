"""
2021/04/30
김영현
파이썬 패키지와 모듈 실습 p 175
"""

# 패키지 = sub2 , 모듈 파일 = (sub2 안에 있는) StockAccount

import Ch06.sub2.calc  # 이 방식으로 사용시 함수 쓸 때마다 경로 전부 적어줘야함   => Ch06.sub2.calc.함수
import Ch06.sub2.calc as c  # 이 방식으로 쓸 경우 as 뒤에 있는 이름.함수 로 바로 불러올 수 있음 (별칭을 붙임)  => 별칭.함수
from Ch06.sub2.calc import *  # 이 방식을 사용하면 가지고 있는 모든 함수를 그냥 바로 사용이 가능해짐   => 함수

r1 = Ch06.sub2.calc.plus(1, 2)
r2 = c.plus(2, 3)
r3 = multi(3, 4)
r4 = div(4, 2)

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)
print('r4 :', r4)
