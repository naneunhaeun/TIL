N1, M1 = map(int, input().split())
person = [list(map(int, input().split())) for _ in range(N1)]

N2, M2 = map(int, input().split())
black_list = [list(map(int, input().split())) for _ in range(N2)]

# 블랙리스트로 -> dat 배열 (블랙리스트 값이 몇부터 몇까지인지)
dat = [0] * 100001

black = 0 # 블랙리스트 수
per = 0 # 일반시민 수

# 1번 dat 배열 만들기
for y in range(N2):
    for x in range(M2):
        dat[black_list[y][x]] = 1 # counting할 필요는 없음

# 2번 검사
for y in range(N1):
    for x in range(M1):
        if dat[person[y][x]]: black += 1 # 블랙리스트
        else: per += 1


print(black)
print(per)