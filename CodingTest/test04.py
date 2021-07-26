n = int(input())
x, y = 1, 1
plans = input().split()

for plan in plans:

    if plan == 'L':
        if y - 1 > 1:
            y -= 1
    elif plan == 'R':
        if y + 1 < n:
            y += 1
    elif plan == 'U':
        if x - 1 > 1:
            x -= 1
    elif plan == 'D':
        if x + 1 < n:
            x += 1

print(x, y)
