arr = [
    [1, 5, 10, 15],
    [15, 15, 20, 30]
]

dat = [0] * 31 # 인덱스를 0부터 30까지 써야하므로 31개

for y in range(2): # 행 순회
    for x in range(4):
        dat[arr[y][x]] += 1 # 값을 인덱스로 씀

n = int(input())
print(dat[n])