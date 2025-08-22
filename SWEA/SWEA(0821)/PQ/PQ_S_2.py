import heapq
pq = []

data = [(7, 'A'), (9, 'C'), (7, 'C'), (6, 'D'), (5, 'A')]

for num, char in data:
    heapq.heappush(pq, (char, -num))

while pq:
    char, neg_num = heapq.heappop(pq)
    print(f'({-neg_num}, {char})', end = ' ')