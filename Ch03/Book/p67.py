import  random
help(random)

help(random.random)

r=random.random()
print('r=',r)

cnt=0
while True:
    r=random.random()
    print(random.random())
    if r<0.01:
        break
    else:
        cnt+=1

print('난수 개수 =',cnt)

#p68
help(random.randint)
help(random.choice)

names=['홍길동','이순신','유관순']
print(names)
print(names[2])

if '유관순' in names:
    print('유관순 있음')
else:
    print('유관순 없음')

idx=random.randint(0,2)
print(names[idx])