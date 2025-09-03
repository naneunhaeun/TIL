A = [4, 2, 5, 3, 7, 6]
B = [5, 3, 7]
n = int(input())

# 방법1) flag 처리
flag = 0

for i in range(3):
    if A[i+n] != B[i]:
        flag = 1
        break

if flag: print('X')
else: print('O')

# 방법2) is_same 함수

def is_same(n):
    for i in range(3):
        if A[n+i] != B[i]: return 0
    return 1

result = is_same(n)
if result: print('O')
else: print('X')