# n =int(input())

# if n % 2 == 0:
#     for n in range(n, n+11, 2):
#         print(n, end = ' ')

# else: 
#     for n in range(n, n+31, 3):
#         print(n, end = ' ')

# 풀었당

# 강사님 풀이
n = int(input())

if n % 2 == 0: # 짝수인 경우
    for i in range(6):
        print(n + 2 * i, end = ' ')

else:  # 홀수인 경우
    for j in range(11):
        print(n + 3 * j, end = ' ')