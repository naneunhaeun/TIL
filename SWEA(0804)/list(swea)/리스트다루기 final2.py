# arr = []
# a, b = map(int, input().split())
# for i in range(8):
#     arr[0:3].append(a)
#     arr[3:5].append(b)
#     arr[5:].append(a+b)

# print(*arr)

# ㅜ 몰라

# 강사님 풀이
arr = []
a, b = map(int, input().split())

for _ in range(3):
    arr.append(a)

for _ in range(2):
    arr.append(b)

for _ in range(3):
    arr.append(a+b)

print(*arr)