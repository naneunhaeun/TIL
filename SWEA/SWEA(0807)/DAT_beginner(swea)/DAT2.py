text = 'ABCDE'


dat = [0] * 200
arr = list(input().split())

# 과정1. dat 채우기
for i in range(len(text)):
    dat[ord(text[i])] = 1 # 문자값을 dat의 인덱스로

# 과정 2. 하나씩 검사
for i in range(3):
    ch = arr[i]
    if dat[ord(ch)] == 1: print('O', end = ' ')
    else: print('X', end = ' ')