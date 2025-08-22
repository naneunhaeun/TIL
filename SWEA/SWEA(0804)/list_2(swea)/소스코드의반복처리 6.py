# 정수 a,b를 입력 받고,
# a가 b 이하면 a부터 b까지 출력(증가)
# a가 b보다 크면 a부터 b까지 출력(감소)

# 반드시 for문을 사용해 주세요.


a, b = map(int, input().split())

if a <= b:   # 증가하는 경우
    for i in range(a, b+1):
        print(i, end = ' ')

else:    # 감소하는 경우
    for j in range(a, b-1, -1):
        print(j, end = ' ')

# 우앗 풀었다  

# 2 5 (input)
# 2 3 4 5 (output)