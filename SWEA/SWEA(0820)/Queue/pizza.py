from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    # 인덱스 1부터 시작(+1), 치즈양
    pizzas = deque([[i + 1, p] for i, p in enumerate(cheese)])

    oven = deque()
    for _ in range(N):
        if pizzas: oven.append(pizzas.popleft())

    while len(oven) > 1:
        now = oven.popleft()
        now[1] //= 2
        if now[1] == 0:
            if pizzas:
                oven.append(pizzas.popleft())
        else:
                oven.append(now)

    print(f'#{tc} {oven[0][0]}')