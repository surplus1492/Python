def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


def multi(x, y):
    return x * y


def div(x, y):
    return x / y


if __name__ == '__main__':
    # 모듈 파일의 프로그램 시작점을 선언하여 의도하지 않은 코드 실행을 차단할 수 있음
    print('plus :', plus(1, 2))
    print('minus :', minus(1, 2))
    print('multi :', multi(2, 3))
    print('div :', div(4, 2))
# 콘솔, 쉘 등의 명령어 기반으로 동작을 하려고 할때 필수적으로 사용해야함
