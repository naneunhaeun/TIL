# N, M = map(int, input().split())
# k = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]

# for y in range(N):
#     for x in range(N):
#         def bomb(y, x):
#             dy = [-1, 1, 1, -1]
#             dx = [-1, -1, 1, 1]
#         for i in range(4):
#             for j in range(1, k+1):
#                 ny = y + dy[i] * j
#                 nx = x + dx[i] * j
#             if ny < 0 or nx < 0 or ny >= N or nx <= N: continue
#             arr[ny][nx] == '%'
#             if arr[ny][nx] == '#' : break
    
#     arr[y][x] == '@'

# for j in arr:
#     print(*j)

def bomb(arr):
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    for y in range(N):
        for x in range(M):
            if arr[y][x] == '@': # 폭탄 발견하면 터뜨리기
                for i in range(4): # 4방향으로
                    for k in range(1, K + 1): # k만큼
                        ny, nx = y + k *dy[i], x + k *dx[i]
                        if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
                        if arr[ny][nx] == '_': arr[ny][nx] = '%' # 폭탄이 터짐 
                        elif arr[ny][nx] == '#': break # 벽 만나면 break
                arr[y][x] = '%' # 현재위치에서 폭탄터지기



N, M = map(int, input().split())
K = int(input())
arr = [list(input()) for _ in range(N)]

bomb(arr)

for row in arr:
    print(*row, sep = '')