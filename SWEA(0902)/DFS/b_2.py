arr= [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0]
]

num = int(input())
n = num - 1
for i in range(5): 
    if arr[n][i] == 0: continue
    print(i + 1)