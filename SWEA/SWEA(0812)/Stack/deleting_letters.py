# T = int(input())
# for t in range(1, T+1):
#     stack = list(input())
#     chr_n = 0
#     for i in range(len(stack)):
#         if stack[i] == stack[i+1]:
#             stack.pop(i)
#
#         else:
#             chr_n += 1
#
# print(f'#{t} {chr_n}')

T = int(input())

for tc in range(1, T + 1):
    string = list(input())
    stack = []
    for char in string:
        # 스택이 비어있지 않고, 현재문자와 stack의 마지막 문자와 같다면
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)

    print(f'#{tc} {len(stack)}')

