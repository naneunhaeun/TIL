# N = int(input())

# for _ in range(N+1):
#     arr = list(map(int, input().split()))
#     K = int(input())

# # 4 방향
# for i in range(4):
#     # k만큼 퍼져나가는 파워
#     for j in range(1, k+1): #0을 곱하면 안됨(1부터 k까지 퍼져나감)
#         ny = y + dy[i] * j
#         nx = x + dx[i] * j
#         if ny < 0 or ny >= 5 or nx < 0 or nx >= 5: continue
#         arr[ny][nx] = 0
#         arr[ny][nx] += arr[ny][nx]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)] #N행 2차원 리스트
K = int(input())

# 4중 for문 --> 행순회, 방향배열 --> 함수로 작성
def magic(y, x):
    dy = [-1, 1, -1, 1] #대각선
    dx = [1, 1, -1, -1]
    sum_v = 0 

    for i in range(4): # 4방향
        for j in range(1, K+1): # k는 1부터 k까지
            ny = y + dy[i] * j # k만큼 퍼져나가는 형태 
            nx = x + dx[i] * j
            if ny < 0 or nx < 0 or ny >= N or nx >= N: continue
            sum_v += arr[ny][nx]
    return sum_v # 마법이 사용된 좌표에서 합계 계산되고 return 
        
result = float('-inf') # 최댓값 구하는 공식

for y in range (N): # 행순회
    for x in range(N):
        result = max(result, magic(y, x)) # 최댓값 갱신 

print(result)

