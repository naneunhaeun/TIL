# 정수 하나 n을 입력받고, 
# n이 10보다 크면 '#' 5번,
# n이 10이하면 '#' n번 출력

n = int(input())

if n > 10:
    for i in range(5):
        print('#', end = '')

elif n <= 10:
    for i in range(n):
        print('#', end = '')
    

# 헐 풀었다 !!

# 강사님 풀이 
n = int(input())

if n > 10:
    for i in range(5):
        print('#', end = '')

else:
    for i in range(n):
        print('#', end = '')
