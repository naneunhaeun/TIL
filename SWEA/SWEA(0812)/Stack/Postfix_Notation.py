# T = int(input())
# for t in range(1, T+1):
#     arr = [list(map(str, input().split())) for _ in range(T)]
#     stack = []
#     for cal in arr:
#         if cal ==

def get_caculate(arr):
    stack = []
    for i in arr[:-1]: # 마지막을 element를 제외하고 순회
        if i.isdecimal(): # 피연산자면 스택에 넣기
            stack.append(int(i))
        elif i in {'+', '-', '*', '/'}: # 연산자면
            if len(stack) < 2: # pop을 해야되는데 2개 미만이면
                return 'error'
            b = stack.pop()
            a = stack.pop()
            if i == '+': stack.append(a + b) # 계산해서 다시 스택에 넣기
            elif i == '-': stack.append(a - b)
            elif i == '*': stack.append(a * b)
            elif i == '/': stack.append(a // b)
    if len(stack) != 1:
        return 'error'
    return stack[0] # stack에 정수가 1개 있을 떄

T = int(input())
for tc in range(1, T + 1):
    Forth = input().split()
    result = get_caculate(Forth)
    print(f'#{tc} {result}')


