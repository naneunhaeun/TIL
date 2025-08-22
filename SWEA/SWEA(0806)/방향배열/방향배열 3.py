arr = [
    [1, 2, 1, 3, 1], 
    [2, 2, 2, 2, 2], 
    [1, 0, 1, 0, 1], 
    [3, 1, 2, 1, 3]
    ]

y, x = map(int, input().split())
multiple_v = arr[2][2]

dy = [1, 1, -1, -1]
dx = [1, -1, -1, 1]

for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    multiple_v *= arr[ny][nx]

print(multiple_v)