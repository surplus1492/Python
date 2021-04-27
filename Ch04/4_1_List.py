"""
2021/04/27
김영현
자료구조 LIST 실습 p84
"""

# List 생성
list1 = 1, 2, 3, 4, 5  # 배열과 같음

print('list1 type :', type(list1))
print('list1[0] :', list1[0])
print('list1[2] :', list1[2])
print('list1[3] :', list1[3])

list2 = [5, 3.14, True, 'Apple']

print('list2 type :', type(list2))
print('list2[1] :', list2[1])
print('list2[2] :', list2[2])
print('list2[3] :', list2[3])

list3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print('list3 type :', type(list3))
print('list3[0][0] :', list3[0][0])
print('list3[1][1] :', list3[1][1])
print('list3[2][1] :', list3[2][1])

# List 덧셈
animal1 = ['사자', '호랑이', '코끼리']
animal2 = ['곰', '기린']

result = animal1 + animal2
print('result :', result)

# List 수정,추가,삭제
nums = [1, 2, 3, 4, 5]

print('nums :', nums)

nums[1] = 7  # 수정

print('nums :', nums)

nums[2:4] = [8, 9, 10]  # 추가

print('nums :', nums)

nums[3:5] = []  # 삭제

print('nums :', nums)
