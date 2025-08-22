arr = [9, 5, 1, 15, 7, 3]

# 리스트 순회하는 방식
# 1. iterator 방식
# 2. indexing 방식

for i in range(len(arr)-1, -1, -1):
    print(arr[i], end = ' ') #indexing 방식 
    
# 3 7 15 1 5 9 