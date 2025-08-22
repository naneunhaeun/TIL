n = int(input())

# 세로로 봤을 때 n의 두 배 까지 
for i in range(n, n*2 + 1):
    # 가로로 봤을 때 1씩 증가
    print(i, i+1, i+2)
