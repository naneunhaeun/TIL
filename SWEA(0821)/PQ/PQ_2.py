import heapq

data = [(2, 'BHC'), (1, 'NeNe'), (3, 'KFC'), (1, 'BBQ'), (2, 'Moms'), (4, 'Mc')]
pq = []

for size, name in data:
    heapq.heappush(pq, (size, name))

while len(pq) > 1:
    size1, name1 = heapq.heappop(pq)
    size2, name2 = heapq.heappop(pq)

    new_size = size1 + size2

    new_name = min(name1, name2)

    heapq.heappush(pq, (new_size, new_name))

final_size, final_name = heapq.heappop(pq)
print(final_name, final_size)