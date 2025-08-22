arr= [list(map(int, input().split())) for _ in range(4)] 

for y in range(3, -1, -1):
    for x in range(3, -1, -1):
        print(arr[y][x], end = ' ')
    print()
         