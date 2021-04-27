"""
2021/04/27
김영현
자료구조 DICTIONARY 실습 p98
"""

# DICTIONARY 생성
dic1 = {1: '서울', 2: '대전', 3: '대구', 4: '부산', 5: '광주'}
dic2 = {
    'A': 'Apple',
    'B': 'Banana',
    'C': 'Cherry'
}
dic3 = {
    101: [1, 2, 3, 4, 5],
    102: (6, 7, 8, 9, 10),
    103: {'한국', '미국', '중국', '일본'},
    104: {'p1': '김유신', 'p2': '김춘추', 'p3': '장보고'}
}

# DICTIONARY 출력
print('dic1 type :', type(dic1))
print('dic1[1] :', dic1[1])
print('dic1[4] :', dic1[5])
print('dic1[4] :', dic1[5])

print('dic2 type :', type(dic2))
print("dic2['A'] :", dic2['A'])
print("dic2['B'] :", dic2['B'])
print("dic2['C'] :", dic2['C'])

print('dic3 type :', type(dic3))
print('dic3[101] :', dic3[101])
print('dic3[101] :', dic3[101])
print('dic3[101] :', dic3[101])