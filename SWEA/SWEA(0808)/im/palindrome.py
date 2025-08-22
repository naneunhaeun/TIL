# T = int(input())
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# for y in range(N):
#     for x in range(N-M+1):
#         text1 = arr[y][x]
#         if text1 == text1[::-1]:
# return text1
#
# for x in range(N):
#     for y in range(N-M+1):
#         text2 = arr[y][x]
#         if text2 == text2[::-1]
# return text2
# print('f#{T} {arr[y][x]}')

def is_p(text):
    return text == text[::-1]

def find_p():
    # 가로 회문 찾기 (행순회)
    for y in range(N):
        for x in range(N-M+1):
            word =''
            for k in range(M): # k를 M만큼(단어의 길이만큼)
                word += arr[y][x+k]
            if is_p(word): # 만약 회문이면
                return word # 첫 번째 return

    # 세로 회문 찾기 (열순회)
    for x in range(N):
        for y in range(N-M+1):
            word = ''
            for k in range(M):
                word += arr[y+k][x]
            if is_p(word):
                return word
    return '' # 세 번째 return: 회문을 찾지 못한 경우

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    result = find_p() # 원본을 바꾸려거나, 디버깅에 필요하면 매개변수(여기선 N,M) 넣으면 됨
    print(f'#{tc} {result}')