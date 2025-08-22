T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # dat 배열 생성 (정류장 1~5000번)
    dat = [0] * 5001

    # 각 버스 노선에 대해
    for _ in range(N):
        A, B = map(int, input().split())
        # A부터 B까지 dat에 기록
        for i in range(A, B + 1):
            dat[i] += 1

    P = int(input()) # 정류장수
    result = [] # 출력할것

    for _ in range(P):
        C = int(input())
        result.append(dat[C]) # 1 2 2 1 1

    print(f'#{tc}', end =' ')
    print(*result)