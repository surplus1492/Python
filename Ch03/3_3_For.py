"""
2021/04/28
김영현
반복문 FOR 실습 p70
"""

# for
for i in range(5):
    print('i :', i)

for j in range(10, 20):
    print('j :', j)

for k in range(10, 0, -1):
    print('k :', k)

# 1~10 합
sum1 = 0

for k in range(11):
    sum1 += k

print('1~10 합은 ', sum1)

# 1~10 짝수 합
sum2 = 0

for k in range(0, 11, 2):
    sum2 += k

print('짝수 합은 ', sum2)

# 중첩 for

for a in range(3):
    print('a ', a)
    for b in range(4):
        print('b ', b)

# 구구단
for x in range(2, 10):
    print(x, '단')
    for y in range(2, 10):
        z = x * y
        print('%d x %d = %d' % (x, y, z))

# 별삼각형
for a in range(1, 11):
    for b in range(a):
        print('☆', end=' ')
    print()

# for a in range(10, 0, -1):
#    for b in range(a):
#        print('☆', end=' ')
#    print()

for i in range(10):
    print('★' * i)

# list 이용한 for
nums = [1, 2, 3, 4, 5]

for num in nums:
    print('num :', num)

for person in ['김유신', '김춘추', '장보고']:
    print('person :', person)

scores = [62, 86, 72, 74, 96]
total = 0

for score in scores:
    total += score

print('총점 :', total)

# list index value 출력
for index, value in enumerate(scores):
    print('{}, {}'.format(index, value))

# list comprehension
list1 = [1, 2, 3, 4, 5]

list2 = [num * 2 for num in list1]
list3 = [num * 3 for num in list1 if num % 2 == 1]

print('list2 :', list2)
print('list3 :', list3)