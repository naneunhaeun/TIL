from collections import deque
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = deque(map(int, input().split()))
    for i in range(M):
        # 가장 왼쪽 원소 제거하고, 이 원소를 다시 덱에 넣음
        arr.append(arr.popleft())

    result = arr[0]
    print(f'#{tc} {result}')





