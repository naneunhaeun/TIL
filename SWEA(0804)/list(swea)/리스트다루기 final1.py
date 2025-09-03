# arr = []
# for i in range(10, -3, -3):
#     arr.append(10)
#     print(*(arr[i], end = ' '))

    #모르겠음 ㅜㅠㅜㅜㅜㅇ엉엉


# 강사님 풀이
# 첫 번째 방법
arr = []
for i in range(10, -3, -3): # 10, 7, 4, 1, -2
    arr.append(i)

print(*arr)

# 두 번째 방법
temp = 10
for i in range(5):
    arr.append(temp)  # 10, 7, 4, 1, -2
    temp -= 3

print(*arr)