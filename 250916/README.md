# TIL - 최소 비용 신장 트리 & 최단 경로

오늘은 그래프에서 **최소 비용 신장 트리(MST)** 와 **최단 경로 알고리즘**을 학습했다.

---

## 최소 비용 신장 트리 (MST)

- 그래프에서 모든 정점을 연결하는 간선들의 가중치 합이 최소가 되는 트리.
- 대표 알고리즘
  - **Prim 알고리즘**: 정점을 기준으로 인접한 간선 중 최소 비용을 선택하며 MST를 확장.
  - **Kruskal 알고리즘**: 간선을 가중치 오름차순으로 정렬 후, 사이클을 피하며 간선을 선택.

### Prim 예시 코드
```python
from heapq import heappush, heappop

def prim(start_node, graph, V):
    pq = [(0, start_node)]  # (가중치, 노드)
    visited = [0] * V
    total = 0

    while pq:
        weight, node = heappop(pq)
        if visited[node]:
            continue
        visited[node] = 1
        total += weight

        for next_node in range(V):
            if graph[node][next_node] and not visited[next_node]:
                heappush(pq, (graph[node][next_node], next_node))
    return total
```

### Kruskal 핵심
1. 간선을 가중치 기준 오름차순 정렬
2. 사이클이 없으면 간선을 선택 → 서로소 집합(Union-Find) 활용

```python
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def kruskal(V, edges):
    parent = [i for i in range(V)]
    edges.sort(key=lambda x: x[2])
    total = 0
    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            total += w
    return total
```

---

## 최단 경로

- **목표**: 간선의 가중치 합이 최소가 되는 경로를 찾기.

### Dijkstra 알고리즘
- 음의 가중치가 없는 그래프에서 한 정점에서 다른 모든 정점까지의 최단 경로를 찾음.
- 우선순위 큐를 활용해 현재까지의 최단 거리가 가장 작은 노드를 반복적으로 탐색.

```python
from heapq import heappush, heappop

def dijkstra(start, graph, V):
    INF = float('inf')
    dist = [INF] * V
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cost, node = heappop(pq)
        if dist[node] < cost:
            continue
        for next_cost, next_node in graph[node]:
            new_cost = cost + next_cost
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heappush(pq, (new_cost, next_node))
    return dist
```

---

오늘 학습을 통해 **그래프 알고리즘의 핵심 패턴**(우선순위 큐 활용, 탐욕적 선택, 사이클 판별 등)을 실습과 함께 정리할 수 있었다.
