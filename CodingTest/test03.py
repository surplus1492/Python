n, k = map(int(input().split()))
result = 0

while True:
    if n == 1:
        break
    else:
        result += 1
        if n%k == 0:
            n = n / k
        else:
            n -= 1

print(result)
