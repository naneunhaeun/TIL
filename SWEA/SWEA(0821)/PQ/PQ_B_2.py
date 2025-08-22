import heapq

pq = []

pqpq = []

heapq.heappush(pq, -5)
heapq.heappush(pq, -2)
heapq.heappush(pq, -8)
heapq.heappush(pq, -1)
heapq.heappush(pq, -9)

while pq:
    pqpq.append(-heapq.heappop(pq))

print(pqpq)