A = [
    [5, 5, 2, 6],
    [9, 1, 1, 3]
]

tar = [5, 6, 1, 1, 1, 1, 5, 4]

# def get_count(n):
#     cnt = 0
#     for i in range(8):
#         if A[i] == tar[i]: cnt += 1
#     return cnt
#
#     for j in cnt:
#         print(*j, end = '')
#
# print()


def get_count(n):
    cnt = 0
    for i in range(len(tar)):
        if tar[i] == n: cnt += 1
    return cnt

for y in range(2):
    for x in range(4):
        result = get_count(A[y][x])
        print(result, end = ' ')
    print()