coins = [10, 50, 100, 500]

coins.sort(reverse = True)

# 거스름돈
change = int(input())
cnt = 0

for coin in coins: # 500, 100, 50, 10 순서대로 순회
    # 현재 동전으로 거슬러 줄 수 있는 갯수
    num_coins = change // coin
    # 계산을 이어서 하기 위해선 나머지(나머지 거스름돈)를 알아야 함
    change %= coin
    # 총 동전 개수 누적
    cnt += num_coins

print(cnt)