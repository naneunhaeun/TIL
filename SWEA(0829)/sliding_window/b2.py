arr = [4, 5, 1, 1, 5, 4, -3, -13, 9, 20, 13]

def get_sum(idx):
    sum_v = 0
    for i in range(5):
        sum_v += arr[idx + i]
    return sum_v

N = len(arr)
M = 5

max_v = float('-inf')
for idx in range(N-M+1):
    ret = get_sum(idx)
    if ret > max_v:
        max_v = ret
        max_idx = idx
        
print(max_idx)        
    