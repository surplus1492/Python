n, m = map(int, input().split())

game = [0 for i in range(n)]
S_num = [10000 for i in range(n)]
result = 0

for i in range(n):
    game[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        if game[i][j] < S_num[i]:
            S_num[i] = game[i][j]

for i in range(n):
    if result < S_num[i]:
        result = S_num[i]

print(result)

# 풀이

n, m = map(int, input().split())
num = []

for i in range(n):
    data = list(map(int, input().split()))
    data.sort()

    num.append(data[0])

num.sort(reverse=True)
result = num[0]

print(result)
