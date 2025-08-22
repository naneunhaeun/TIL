sum_v = 0
max_v = float('-inf') # 음의 무한대
min_v = float('inf') # 양의 무한대

arr = [2, 5, 1, 6, 4, 3]

# iterator 방식
for i in arr:
    if i > max_v: max_v = i #최대값 코드
    if i < min_v: min_v = i #최소값 코드 
    sum_v += i   # 누적 합계

print(sum_v)
print(max_v - min_v)

# indexing 방식
for i in range(len(arr) - 1):
    arr[i]