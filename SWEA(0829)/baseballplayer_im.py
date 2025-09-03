t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    players = list(map(int, input().split()))
    players.sort() # 오름차순 정렬
    
    right, left = 0, 0
    ret = 0    

    while left < n and right < n:
        if players[right] - players[left] > k:
            left += 1
        else: 
            right += 1
            
        ret = max(right-left, ret)
        
    print(f'#{tc} {ret}')
    