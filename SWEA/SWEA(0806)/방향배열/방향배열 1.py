arr = [
    [1, 2, 1, 3, 1], 
    [2, 2, 2, 2, 2], 
    [1, 0, 1, 0, 1], 
    [3, 1, 2, 1, 3]
    ]

y = 1
x = 2
sum_v = 0
# sum_v += arr[y-1][x+0] # 위
# sum_v += arr[y+1][x+0] # 아래
# sum_v += arr[y+0][x+1] # 오른쪽
# sum_v += arr[y+0][x-1] # 왼쪽

# 방향 배열(델타 배열) 자료 구조 : 이동방향을 미리 정의해둔 자료 구조 
#    상  하  좌  우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
# direction의 d

# 4방향이기 때문에 4번 반복
#ny: next y, y: 현재좌표, dy: 방향배열
for i in range(4):
    ny = y + dy[i] # next y, x 가 
    nx = x + dx[i] # 상하좌우로 
    sum_v += arr[ny][nx]

print(sum_v)







