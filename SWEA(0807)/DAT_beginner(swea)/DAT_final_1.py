# 땅: dat배열로 만들고
# 주민: 결과 2중 for문으로 작성
# -> get_count()함수 만들면 4중 for문,
# dat 배열쓰면 2중 for문

arr = [
    [4, 5, 7, 6],
    [1, 5, 5, 4],
    [1, 1, 1, 1]
]

tar = [
    [5, 6, 4],
    [1, 5, 3]
]

dat = [0] * 8

for y in range(3):  # 행순회
    for x in range(4):
        dat[arr[y][x]] += 1  # 값을 인덱스로

for y in range(2):  # 행순회
    for x in range(3):
        print(dat[tar[y][x]], end=' ')
    print()
