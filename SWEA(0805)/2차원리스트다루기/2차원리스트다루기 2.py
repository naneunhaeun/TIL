# y를 고정시키고 x를 순회

arr = [[0]*4 for _ in range(4)] # [0, 0, 0, 0] 4번 반복
arr[0][0] = 7
arr[1][3] = 1
arr[2][1] = 3
arr[3][3] = 9

for i in range(4): #0, 1, 2, 3
    print(arr[3][i], end = ' ')

# 0 0 0 9 마지막 행 출력