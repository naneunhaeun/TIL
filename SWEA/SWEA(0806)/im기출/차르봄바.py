def get_sum(y, x):
    dy = [-1, 1, 0, 0] # 4빙향 (상하좌우)
    dx = [0, 0, -1, 1] 
    sum_v = arr[y][x] # 현재위치로 초기화 
    for i in range(4): # 4방향
        for k in range(1, P + 1):
            ny, nx = y + dy[i] * k, x + dx[i] * k
            if ny < 0 or ny >= N or nx < 0 or nx >= N: continue
            sum_v += arr[ny][nx]
    return sum_v

T = int(input())
for tc in range(1, T + 1):
    result = float('-inf')
    N, P = map(int, input().split())    
    arr = [list(map(int, input().split())) for _ in range(N)]
    for y in range(N): # 행 순회
        for x in range(N):
            result = max(result, get_sum(y, x)) # 함수호출

    print(f'#{tc} {result}')


