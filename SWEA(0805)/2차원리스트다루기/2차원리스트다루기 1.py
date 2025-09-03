arr = [[0]*4 for x in range(4)] # [0, 0, 0, 0] 4번 반복
arr[0][0] = 7
arr[1][3] = 1
arr[2][1] = 3
arr[3][3] = 9


for x in arr:
    print(*x)

# 7 0 0 0
# 0 0 0 1
# 0 3 0 0
# 0 0 0 9