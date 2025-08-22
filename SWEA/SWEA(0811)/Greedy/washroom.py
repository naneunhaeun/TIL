# 전략: 시간이 가장 적은 사람부터 이용
times = [15, 30, 50, 10]

times.sort()

# 총 대기시간
total_wait = 0
for i in range(len(times)):
    # 현재 사람의 이용시간 * 뒤에 남아있는 사람
    total_wait += times[i] * (len(times) - i - 1)

print(total_wait)