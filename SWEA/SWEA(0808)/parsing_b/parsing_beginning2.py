# arr = [
#     [A, B, C, Q],
#     [B, [4], R],
#     [C, C, D, A],
#     [B, T, [15]]
# ]

# def get_find(text):
#     # 못찾으면 빈 문자열 return
#     # if find == -1 : return''
#     # 찾으면 슬라이싱 return
#     # return text[start:end]
#
#     if text.find('['):
#         return
#
# print(get_find(text))

# 다음 배열의 모든 element에서 대괄호 안에 있는 숫자만 출력해 보세요.
# find() 메서드를 사용해 주세요.
# get_find(text) 함수를 만들어 주세요.


arr = ['ABCQ', 'B[4]R', 'CCDA', 'BT[15]']
def get_find(text):
    # 못찾으면 빈문자열 return
    if text.find('[') == -1:
        return ""
    start = text.find('[') + 1
    end = text.find(']')
    # 찾으면 슬라이싱 return
    return text[start : end]

for text in arr:
    result = get_find(text)
    # 문자열이 비어있으면 False
    # 문자열이 있으면 True
    if result:
           print(result, end = ' ')
