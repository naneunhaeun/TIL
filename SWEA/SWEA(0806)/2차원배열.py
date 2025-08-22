arr = [[0]*4 for _ in range(3)]

arr[1][1] = 10
arr[2][1] = 20
print(arr)
for x in arr:
    print(x)

# arr2 = [[0]*4]*3
# arr2[1][1] = 10
# arr2[2][1] = 20
# print(arr2)

# i 행의 좌표
# j 열의 좌표


# 행 우선 순회 

s = 0 # 합을 구할 떄

for i in range(n):
    for j in range(m):
        f(array[i][j]) # 필요한 연산 수행 
        s += arr[i][j] # 합을 구할 때 


max_v = 0 # 최댓값 구할 때

for i in range(n):
    s= 0
    for j in range(m):
        s += arr[i][j] 
    if max_v < s:
        max_v = s 
        
#

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

s = 0

for i in range(N):
    for j in range(M):
        s += arr[i][j]

# 열 우선 순회
for j in range(m):
    for i in range(n):
        f(array[i][j]) # 필요한 연산 수행 


# 지그재그 순회
# i 행의 좌표
# j 열의 좌표

