i = tot = 10
i += 1
tot += i
print(i, tot)

print('출력1', end=',')
print('출력2')

v1, v2 = 100, 200
v2, v1 = v1, v2
print(v1, v2)

lst = [1, 2, 3, 4, 5]
v1, *v2 = lst
*v1, v2 = lst
print(v1, v2)
