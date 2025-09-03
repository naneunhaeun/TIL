# 첫 번째 방법
T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())

    TOGGLE = "ON"
    for i in range(N):
        if M & (1 << i):
            continue
            
        TOGGLE = "off"
        break

    print(f'#{tc} {TOGGLE}')