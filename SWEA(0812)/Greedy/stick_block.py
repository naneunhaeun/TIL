# 오름차순 정렬 후 합이 100이 넘지 않을 때까지 더하기
n = int(input())
blocks = list(map(int, input().split()))

blocks.sort()
cnt, total = 0, 0

for block in blocks:
    total += block
    if total > 100: break # counting 하기 전에 break
    cnt += 1

print(cnt)
