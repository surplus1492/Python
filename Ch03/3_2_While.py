"""
2021/04/28
김영현
반복문 WHILE 실습 p64
"""

# while
num1 = 1

while num1 < 5:
    print('num1 :', num1)
    num1 += 1

# 1~10 합
k, sum = 1, 0

while k <= 10:
    sum += k
    k += 1

print('합은 ', sum)

# 1~10 짝수 합
i, tot = 1, 0

while i <= 10:
    if i % 2 == 0:
        tot += i
    i += 1

print('짝수 합은 ', tot)

# break
num = 1

while True:
    if num % 5 == 0 and num % 7 == 0:
        break
    num += 1

print('num :', num)

# continue
s, total = 1, 0

while s <= 10:
    s += 1
    if s % 2 == 1:
        continue

    total += s

print('짝수 합 :', total)