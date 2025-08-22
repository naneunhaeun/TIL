# text = list(input())
#
# def get_num(text):
#     while True:
#         if text.find('[') == -1:
#             return ''
#         start1 = text.find('[') + 1
#         end1 = text.find(']')
#         return text[start1 : end1]
#
#         if text.find('{') == -1:
#             return ''
#         start2 = text.find('{') + 1
#         end2 = text.find('}')
#         return text[start2: end2]
#
# lst = print()

# 접근 방식
# '['를 찾고 이 위치를 a로 설정
# b = text.find(']', a + 1)
# int(text[a + 1 : b]) --> 정수로 변환

text = input()
n = len(text)
a, b = 0, 0
cal_v = 0
i = 0 # while 초기식
while i < n: # while 조건식
    # 덧셈 계산
    if text[i] =='[':
        a = i
        b = text.find(']', a + 1) # 열리는 위치 이후로
        cal_v += int(text[a + 1 : b])
        i += (b - a)  # +1 은 증감식에서

    # 곱셈 계산
    elif text[i] == '{':
        a = i
        b = text.find('}', a + 1)  # 열리는 위치 이후로
        cal_v *= int(text[a + 1:b])
        i += (b - a)  # +1은 증감식에서

    i += 1 # while 증감식

print(cal_v)

