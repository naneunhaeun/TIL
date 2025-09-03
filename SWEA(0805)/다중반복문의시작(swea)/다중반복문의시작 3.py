# 2중 for문을 사용하여 다음과 같이 출력
# 0000
# 1111
# 2222
# 3333

# 행 y, 열 x 변수를 사용 했을 때,
# 방법 1) y를 출력
# 방법 2) 임시변수 t를 출력

# 1)
for y in range(4): # 0, 1, 2, 3 
    for x in range(4): # 0을 4번 출력, 1을 4번 출력 ...
        print(y, end = '')
    print()

# 2)
for y in range(4):
    for x in range(4):
        print(t, end = '') # 4번 출력
    t += 1 # 0 -> 1 -> 2 -> 3
    print() # 줄바꿈 