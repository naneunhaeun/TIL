# 가장 작은 두 수를 선택하기 위해 정렬
# 더한 값을 배열에 다시 넣고(append) 정렬
# 모든 수가 하나로 합쳐질 때까지 반복

n = int(input())
arr = list(map(int, input().split()))

# 내림차순 정렬
arr.sort(reverse=True)

sum_v = 0
while len(arr) > 1: # 1개 이하가 될 때 까지 반복
    temp = arr.pop() + arr.pop() # 작은 거 두 개 빼서 더하기
    sum_v += temp # 합계 누적

    arr.append(temp) # append로 넣고
    arr.sort(reverse=True) # 다시 정렬

print(sum_v)
