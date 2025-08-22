# level이 3이고 branch가 2인 재귀호출 코드 구현
def fx(x):
    if x == 3:
        return
    for i in range(2):
        fx(x + 1)
    print(x)
fx(0)