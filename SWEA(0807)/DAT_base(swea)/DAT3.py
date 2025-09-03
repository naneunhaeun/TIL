# A = [5, 2, 5, 7, 3]
# x = int(input())
# cnt = 0
#
# def get_count(n):
#     for i in A:
#         if A[i] == x: cnt += 1
#         else: pass
#
#         print(cnt)
#

A = [5, 2, 5, 7, 3]

def get_count(n):
    cnt = 0
    for i in range(5):
        if A[i] == n: cnt += 1

    return cnt
n= int(input())
result = get_count(n)
print(result)