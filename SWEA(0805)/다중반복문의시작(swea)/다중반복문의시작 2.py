arr = ['A', 'B', 'Q', 'T']

for i in range(4):
    for j in range(len(arr)-1, -1, -1):
        print(arr[j], end = '')
    print()

# 강사님 풀이
for i in range(4): # 4회 반복
    for j in range(3, -1, -1): # 역순 출력 -> 외웟
        print(arr[j], end = '')
    print()

    # TQBA
    # TQBA
    # TQBA
    # TQBA