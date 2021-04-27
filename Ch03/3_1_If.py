"""
2021/04/27
김영현
조건문 IF 실습 p60
"""

# IF (중괄호를 안쓰기에 들여쓰기 되는게 범위임)
num1, num2 = 1, 2

if num1 > 0:
    print('num1은 0보다 크다')

if num1 > num2:
    print('num1은 num2보다 크다')

if num1 > 0:
    if num2 > 1:
        print('num1은 0보다 크고 num2는 1보다 크다')

if num1 > 0 and num2 > 1:
    print('num1은 0보다 크고 num2는 1보다 크다')

# IF ~ ELSE
num3, num4 = 3, 4

if num3 > num4:  # 내용을 비워서 지나갈때 pass 사용
    pass  # 조건 참
else:
    # 조건 거짓
    print('num3이 num4보다 작다')

# IF ~ ELIF ~ ELSE
if num1 > num2:
    print('num1이 num2보다 크다')
elif num2 > num3:
    print('num2이 num3보다 크다')
elif num3 > num4:
    print('num3이 num4보다 크다')
else:
    print('num4가 가장 크다')

# 삼항 조건문
num = 3

result = num * 2 if num >= 5 else num + 2
#       조건이 참      조건        조건이 거짓
num = 5
result1 = num * 2 if num >= 5 else num + 2

print('result :', result)
print('result1 :', result1)

# 확인문제
score = int(input('점수 입력 : '))

print('점수 확인 :', score)

if 100 >= score >= 90:
    print('A 입니다')
elif 90 > score >= 80:
    print('B 입니다')
elif 80 > score >= 70:
    print('C 입니다')
elif 70 > score >= 60:
    print('D 입니다')
elif 60 > score:
    print('F 입니다')
