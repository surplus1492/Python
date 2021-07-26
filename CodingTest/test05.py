h=int(input())

count=0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(k):
                count += 1
            elif '3' in str(j):
                count += 1
            elif '3' in str(i):
                count += 1
print(count)