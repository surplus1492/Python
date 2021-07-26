n, m, k = map(int, input().split())

data = list(map(int, input().split()))

result = temp = 0
F_num = S_num = 0

for i in range(n):
    if F_num < data[i]:
        S_num = F_num
        F_num = data[i]
    elif S_num < data[i]:
        S_num = data[i]

for i in range(m):
    if temp == k:
        temp = 0
        result += S_num
    else:
        temp += 1
        result += F_num

print(result)

# 풀이

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)  # 리스트를 내림차순으로 정렬

F_num = data[0]  # 정렬한 이후 제일 큰 수는 처음으로 옴
S_num = data[1]
result = 0
temp = k

# 아래는 동일

for i in range(m):
    if temp > 0:
        result += F_num
        temp -= 1
    else:
        result += S_num
        temp = k

print(result)
