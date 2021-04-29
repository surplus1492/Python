t=(10,)
print(t)

t2=(1,2,3,4,5,3)
print(t2)

print(t2[0],t2[1:4],t2[-1])

for i in t2:
    print(i,end=' ')
print()
if 6 in t2:
    print('6 있음')
else:
    print('6 없음')

# p95
lst=list(range(1,6))
t3=tuple(lst)
print(t3)

print(len(t3), type(t3))
print(t3.count(3))
print(t3.index(4))