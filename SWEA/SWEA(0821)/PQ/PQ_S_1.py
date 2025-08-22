import heapq

arr = [5, 2, 8, 1, 9, 4]
pq = []

for x in arr:
    is_odd = x % 2
    heapq.heappush(pq, (is_odd, x))

while pq:
    priority, num = heapq.heappop(pq)
    print(num, end = ' ')
