"""
2021/05/03
김영현
정규표현식 실습 p192

정규표현식(Regular Expression)
 - 특정한 규칙을 갖는 문자열을 처리하기 위한 문법
 - 일반적으로 특정 문자 검색, 매치 여부를 확인할 때 정규표현식을 사용
"""

import re
from re import findall, match

str1 = '1234 abc 홍길동 ABC_555_6 부산광역시'

# 숫자검색
print(findall('1234', str1))
print(findall('[0-9]', str1))
print(findall('[0-9]{3}', str1))
print(findall('[0-9]{3,}', str1))

# 문자열 검색
print(findall('[가-힣]{3,}', str1))
print(findall('[a-z|A-Z]{3,}', str1))

str2 = 'test1abcABC 123mbc 45test'

print(findall('^test', str2))  # ^ start
print(findall('st$', str2))  # $ finish

# 단어 검색
str3 = 'test^홍길동 abc 대한*민국 123'

print(findall('\\w{3,}', str3))

# 응용
jumin = '123456-1891234'
result = match('[0-9]{6}-[1-2][0-9]{6}', jumin)

if result:
    print('주민번호가 맞습니다')
else:
    print('주민번호가 아닙니다')
