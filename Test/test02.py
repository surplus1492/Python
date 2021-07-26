cargo = int(input('짐의 무게는 얼마입니까? '))

if cargo >= 10:
    pay = 10000
    print('수수료는 {0:,}원 입니다.'.format(pay))
else:
    pay = 0
    print('수수료는 없습니다.')
