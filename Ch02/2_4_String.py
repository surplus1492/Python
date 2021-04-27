"""
2021/04/26
김영현
파이썬 문자열 실습하기 p48
"""

# 문자열 더하기
str1 = 'Hello'
str2 = 'Python'
str3 = str1 + str2

print('str3 :', str3)

# 문자열 곱하기
name = '홍길동'
print('name * 3 :', name * 3)

# 문자열 길이
msg = 'Hello World'

print('msg 길이 :', len(msg))

# 문자열 인덱스
print('msg 1번 문자 :', msg[0])
print('msg 7번 문자 :', msg[7])
print('msg -1번 문자 :', msg[-1])  # 마지막 번호 나옴 - 붙이면 뒤에서 부터 들어감
print('msg -5번 문자 :', msg[-5])

# 문자열 자르기 (substring)
print('msg 0~5 문자열', msg[0:5])
print('msg 5까지 문자열', msg[:5])  # 앞에 비우면 처음부터
print('msg 6에서 끝까지 문자열', msg[6:])  # 뒤에 비우면 끝까지

# 문자열 분리 (분리되는 것들 = token)
people = '김유신|김춘추|장보고|감간찬|이순신'
p1, p2, p3, p4, p5 = people.split('|')  # 사용된 구분자 입력

print('p1 :', p1)
print('p2 :', p2)
print('p3 :', p3)
print('p4 :', p4)
print('p5 :', p5)

# 문자열 이스케이프
print('서울\n대전\n대구\n부산\n광주')
print('서울\t대전\t대구\t부산\t광주')
print('저는 \'홍길동\'입니다')  # = "저는 '홍길동'입니다"
