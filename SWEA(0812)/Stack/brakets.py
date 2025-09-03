T = int(input())
for t in range(1, T+1):
    text = input()
    stack = []
    for i in text:
        # 1. 여는 괄호면 스택에 추가(append)
        if i == '{' or i == '(': stack.append(i)
        # 2. 닫는 괄호가 중괄호면 스택이 비어있지 않고, 짝이 맞는지 확인 후 제거(pop)
        elif stack and i == '}' and stack[-1] == '{': stack.pop()
        # 3. 닫는 괄호가 소괄호면 스택이 비어있지 않고, 짝이 맞는지 확인 후 제거(pop)
        elif stack and i == ')' and stack[-1] == '(': stack.pop()
        # 4. 닫는 괄호인데 짝이 맞지 않으면 -> stack에 추가(append)
        elif i == '}' or i == ')': stack.append(i)

    if stack: result = 0 # 스택이 비어있지 않으면
    else: result = 1 # 스택이 비어있으면(괄호의 짝이 다 맞음)

    print(f'#{t} {result}')