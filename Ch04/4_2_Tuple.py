"""
2021/04/27
김영현
자료구조 Tuple 실습 p92
"""

# TUPLE (고정 List) 생성
tuple1 = (1, 2, 3, 4, 5)  # tuple은 수정 추가 삭제 불가능

print('tuple1 type :', type(tuple1))
print('tuple1[0]', tuple1[0])
print('tuple1[4]', tuple1[4])

tuple2 = ('서울', '대전', '대구', '부산', '광주')

print('tuple2 type :', type(tuple2))
print('tuple2[0] : %s' % tuple2[0])
print('tuple2[4] : {}'.format(tuple2[4]))

tuple3 = 1, 2, 3, 4, 5

print('tuple3 type :', type(tuple3))

# tuple3[1] = 7 불가능
# tuple3[4] =[] 불가능