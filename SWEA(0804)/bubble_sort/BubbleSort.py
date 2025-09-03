# arr = [12, 3, 9, 1, 15, 7]

# Big-O표기법
# O(nlogn) == O(n)과 비슷
# O(logn) == O(1)과 비슷

# sort로 정렬할 수 있음
# result = sorted(arr) # 원본 변경 안됨 sort는 변경됨
# print(*result)

# 버블정렬 하는 방법
# a: 리스트, N: element 개수
def bubble_sort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(i): # i - 1 까지
            if a[j] > a[j+1]: # 왼쪽이 더 크면 자리교환
                a[j], a[j+1] = a[j+1], a[j] 

    # 원하는 결과
    return a 

# 하드코딩
arr = [12, 3, 9, 1, 15, 7]

# 함수 호출
result = bubble_sort(arr, len(arr))
print(*result)

