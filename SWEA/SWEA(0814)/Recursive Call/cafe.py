arr = input().split()
n = len(arr)
# 0b110 (이진수) -> 6 (십진수)

def get_sub(tar):
    cnt = 0
    for i in range(n):
        # if tar & 1: -> 0x1 가독성 : 이 연산은 비트연산입니다.
        if tar & 0x1: # 마지막 자리가 1인지 확인
            cnt += 1
        tar >>= 1 # 오른쪽으로 한번씩 민다.
    return cnt

result = 0
for tar in range(1 << n): # 2의 n제곱(모든 부분집합의 개수)
    if get_sub(tar) >= 2: # bit가 2개이상 1이라면,
        result += 1

print(result)
