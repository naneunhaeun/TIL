# arr = [['_'] * 5 for _ in range(4)] # 4행 5열 '_' 채워진 2차원 배열

# y, x = map(int, input().split())

# dy = [-1, -1, -1, 0, 0, 1, 1, 1]
# dx = [-1, 0, 1, -1, 1, -1, 0, 1]

# for i in range(8):
#     ny = y + dy[i]
#     nx = x + dx[i]
#     if ny < 0 or ny >= 4 or nx < 0 or nx >= 5: continue
#     if arr[y][x]:
#         arr[ny][nx] = '#' 
#     else:
#         pass
#     print(*arr)


arr = [['_'] * 5 for _ in range(4)]
for _ in range(2):
    y, x = map(int, input().split())
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= 4 or nx < 0 or nx >= 5: continue
        arr[ny][nx] = '#' 

for row in arr:
    print(*row)