arr = [list(map(int, input().split())) for _ in range(5)]

cnt = 0
max_v = float('-inf') # 음의 무한대
min_v = float('inf') # 양의 무한대
sum_v = 0


# for i in arr:
#     if i > max_v: max_v = i
#     if i < min_v: min_v = i
#     print(max_v, min_v)


for y in range(5):
    for x in range(5):
        if arr[y][x] == 2: cnt += 1
        if arr[y][x] > max_v: max_v = arr[y][x]
        if arr[y][x] < min_v: min_v = arr[y][x]

    sum_v += arr[y][y] #00, 11, 22, 33, 44

print(cnt)
print(max_v, min_v)
print(sum_v)