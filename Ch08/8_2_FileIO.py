"""
2021/05/03
김영현
파일 입출력 실습 p217
"""

# 파일 읽기 (File Input)
file1 = open('C:/Users/6기 김영현/Desktop/workspace/File Input,Output/Sample.txt', 'r')
line = file1.readline()

print('line :', line)
file1.close()

# 여러줄 읽기
file2 = open('C:/Users/6기 김영현/Desktop/workspace/File Input,Output/Sample.txt', 'r')

while True:
    line = file2.read()

    if not line:
        break

    print(line)

file2.close()

# 파일 쓰기 (File Output)
file3 = open('C:/Users/6기 김영현/Desktop/workspace/File Input,Output/Test.txt', 'w')
file3.write('안녕하세요\n')
file3.write('반갑습니다\n')
file3.write('감사합니다\n')

file3.close()

# 구구단 쓰기
file4 = open('C:/Users/6기 김영현/Desktop/workspace/File Input,Output/Gugudan.txt', 'w')

for i in range(2, 10):
    file4.write('%d단 \n' % i)
    for j in range(1, 10):
        file4.write('{} * {} = {}\n'.format(i, j, i * j))
    file4.write('\n')

file4.close()
