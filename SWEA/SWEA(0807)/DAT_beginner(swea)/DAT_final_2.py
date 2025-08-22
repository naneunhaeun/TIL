criminal = [
    [5, 7, 9, 55],
    [30, 10, 6, 8]
]

people = [
    [1, 2, 3, 4],
    [5, 7, 10, 15]
]

dat = [0] * 56
crim = 0
ppl = 0

for y in range(2):
    for x in range(4):
        dat[criminal[y][x]] = 1 # criminal 의 값을 인덱스로 변환

for y in range(2):
    for x in range(4):
        if dat[people[y][x]]: crim += 1
        else: ppl += 1

print(crim, ppl)



