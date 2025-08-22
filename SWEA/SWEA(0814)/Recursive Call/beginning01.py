# 중복순열 [1, 1, 1] ~ [6, 6, 6]까지 출력하는 코드를 재귀호출로 구현해 보세요.

# [출력]
# 111
# 112
# ......
# ......
# 666

path = []


def fx(lev):
    if lev == 3: # 주사위 3개 던짐 (level = 3)
        print(*path)
        return

    for i in range(1, 7): # 주사위 1부터 6까지 (branch 6)
        path.append(i)
        fx(lev + 1)
        path.pop()


fx(0)
