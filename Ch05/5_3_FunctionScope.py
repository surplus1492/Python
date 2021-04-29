"""
2021/04/29
김영현
함수 스코프 실습 p132
"""


def sum(x, y):
    tot = 0

    for k in range(x, y + 1):
        tot += k

    return tot


tot = 0
start = 1
end = 10

tot = sum(start, end)

print('tot :', tot)
