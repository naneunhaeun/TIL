# 두 번째 방법
def solve():
    tar = M
    for i in range(N):
        if tar & 0x1 == 0:
            return 'OFF'

        tar >>= 1 # N번 반복하면서 오른쪽으로 한번씩 민다. M의 1비트가 1인지 확인
    return 'ON'

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    print(f'#{tc} {solve()}')