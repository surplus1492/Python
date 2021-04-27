"""
2021/04/27
김영현
자료구조 SET 실습 p96
"""

# SET 생성 (순서 없고 ,중복 불가)
set1 = {1, 2, 3, 4, 5, 3}

print('set1 type :', type(set1))
print('set1 :', set1)

set2 = set('Hello World')

print('set2 type :', type(set2))
print('set2 :', set2)

# SET 출력 (LIST로 변환)
list1 = list(set1)

print('list1 :', list1)
print('list1[0] :', list1[0])
print('list1[3] :', list1[3])

list2= list(set2)

print('list2 :', list2)
print('list2[0] :', list2[0])
print('list2[3] :', list2[3])
