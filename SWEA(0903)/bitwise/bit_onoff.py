def turn(n, m):
    if m & (1 << n):
        return 'ON'
    else: return 'OFF'

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    result = turn(n,m)
    print(f'#{tc} {result}')