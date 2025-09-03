arr = [0] * 8
for i in range(4): #0, 1, 2, 3
    arr[i] = 7

for j in range(4, 8): # 4, 5, 6, 7
    arr[j] = 15

print(*arr)

# 7 7 7 7 15 15 15 15