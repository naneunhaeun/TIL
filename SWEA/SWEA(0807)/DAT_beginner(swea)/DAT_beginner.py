# DAT(Direct Address Table)
# 값을 인덱스로 쓰는 자료구조
#
# ex) arr = [4, 2, 4, 4, 2]
# -> DAT = [0] * 5
# DAT 배열
# 0 -> 0
# 1 -> 0
# 2 -> 2
# 3 -> 0
# 4 -> 3

# 코드화
A = [4, 2, 4, 4, 2]

dat = [0] * (4 + 1)
idx = 0

for i in range(len(A)):
    idx = A[i]
    dat[idx] += 1

# print(dat)
for i in range(len(A)):
    if dat[i] > 0: print(f'{i} : {dat[i]}')


# 만약 값이 string이면 인덱스로 어떻게 쓸까??
# Q) "BTSKFCBBQ" 문자열에서 각 알파벳이 몇개 씩 있을까?
# A) 아스키코드로 변환

text = "BTSKFCBBQ"

dat = [0] * 200 # 0 ~ 199까지의 인덱스(소문자 a의 아스키코드 97)
for i in range(len(text)):
    dat[ord(text[i])] += 1 # 값(아스키코드)을 인덱스로

for i in range(200):# 0 ~ 199
    if dat[i] == 0: continue
    print(f'{chr(i)} : {dat[i]}')


# DAT 자료구조 쓰는 이유
# arr = [4, 4, 5, 5, 9, 1]
# 3 4 1 5 5 4  몇 개씩 있을까?
# -> for 문으로 순회 cnt += 1
#     -> 시간복잡도 O(n)
# DAT 배열은 미리 초기세팅이 되어있어서 for문 순회를 하지 않고 바로 갯수 확인 가능
# -> 시간복잡도 O(1) -> 매우 빠름(효율적)
# 단점은 메모리 사용량이 큼, 인덱스를 써서 음수 처리가 불가능