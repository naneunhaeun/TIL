arr = [
    [1, 2, 1, 3, 1], 
    [2, 2, 2, 2, 2], 
    [1, 0, 1, 0, 1], 
    [3, 1, 2, 1, 3]
    ]

y, x = map(int, input().split())
max_v = arr[y][x]

dy = [0, 1, 1, 0]
dx = [1, 1, 0, -1]

for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if ny < 0 or ny >= 4 or nx < 0 or nx >= 5: continue
    if max_v < arr[ny][nx]:
        max_v = arr[ny][nx]

print(max_v)    
