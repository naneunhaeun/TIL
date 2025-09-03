n, m = map(int, input().split())
arr = list(map(int, input().split()))

sum_v = sum(arr[:m])
max_v = sum_v
max_idx = 0

for i in range(n-m):
    sum_v -= arr[i]
    sum_v += arr[i+m]
    
    if sum_v > max_v:
        max_v = sum_v
        max_idx += i + 1
        
print(max_idx)