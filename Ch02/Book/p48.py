oneLine = "this is one line string"
print(oneLine)

multiLine = """this is
multi line
string"""
print(multiLine)

multiLine2 = "this is\nmulti line\nstring"
print(multiLine2)

# p50
print(oneLine)
print("문자열 길이 :", len(oneLine))
print(oneLine[0:4])
print(oneLine[:])
print(oneLine[::2])

print(oneLine[0:-1:2])
print(oneLine[-6:-1])
print(oneLine[-6:])

subString = oneLine[-11:]
print(subString)

# p52
print('t 글자수 :', oneLine.count('t'))

print(oneLine.startswith('this'))
print(oneLine.startswith('that'))

print(oneLine.replace('this', 'that'))


sent = multiLine.split('\n')
print('문장 : ', sent)

words = oneLine.split(' ')
print('단어 : ', words)

sent2 = ','.join(words)
print(sent2)