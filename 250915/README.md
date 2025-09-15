# 📚 Today I Learned: 그래프 기본

## 그래프란?
아이템(사물·추상 개념)들과 이들 사이의 **연결 관계**를 표현하는 자료구조  
→ 선형 구조나 트리로 표현하기 어려운 **N:N 관계**를 표현하기 적합

- **구성**: 정점(Vertex) 집합 + 간선(Edge) 집합
- 정점 개수 |V|, 간선 개수 |E|  
  최대 간선 수: `|E| = |V| * (|V|-1) / 2`  
  예) 정점 5개 → 최대 간선 10개

### 그래프 유형
- **완전 그래프**: 가능한 모든 간선을 가진 그래프
- **부분 그래프**: 원래 그래프에서 일부 정점·간선을 제외한 그래프

---

## 인접(Adjacency)
두 정점이 간선으로 연결돼 있으면 **인접**  
완전 그래프의 임의 두 정점은 모두 인접

---

## 경로와 사이클
- **경로**: 간선들을 순서대로 나열한 것  
  예) 정점 0–2–4–6
- **단순 경로**: 한 정점을 최대 한 번만 지나는 경로
- **사이클**: 시작 정점에서 다시 시작 정점으로 돌아오는 경로

---

## 그래프 표현 방식
1. **인접 행렬**  
   - |V|×|V| 2차원 배열  
   - 두 정점이 인접하면 1, 아니면 0  
   - 검색 빠름, **공간 낭비 큼**
2. **인접 리스트**  
   - 각 정점이 인접한 정점을 리스트로 저장  
   - 간선이 적은 **희소 그래프**에 효율적
3. **간선 배열**  
   - 간선 (start, end)만 배열로 저장

---

## DFS (Depth First Search)
- **깊이 우선 탐색**: 한 방향으로 갈 수 있을 때까지 탐색 후, 막히면 되돌아와 다른 경로 탐색

```python
def dfs(node):
    print(node, end=' ')
    for nxt in graph[node]:
        if visited[nxt]: 
            continue
        visited[nxt] = 1
        dfs(nxt)
```

---

## BFS (Breadth First Search)
- **너비 우선 탐색**: 가까운 정점부터 차례로 탐색
- `collections.deque` 활용

```python
from collections import deque

def bfs(start):
    q = deque([start])
    while q:
        now = q.popleft()
        print(now, end=' ')
        for nxt in graph[now]:
            if visited[nxt]:
                continue
            visited[nxt] = 1
            q.append(nxt)
```

---

## Union–Find (Disjoint Set)
서로 교집합이 없는 집합을 관리하는 자료구조

### 주요 연산
- **Make-Set(x)**: 원소 x를 대표로 집합 생성
- **Find-Set(x)**: x가 속한 집합의 대표 찾기
- **Union(x, y)**: 두 집합을 합침

```python
def make_set(n):
    parents = [i for i in range(n + 1)]
    ranks = [0] * (n + 1)
    return parents, ranks

def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])  # path compression
    return parents[x]

def union(x, y):
    rx, ry = find_set(x), find_set(y)
    if rx == ry: return
    if ranks[rx] < ranks[ry]:
        parents[rx] = ry
    elif ranks[rx] > ranks[ry]:
        parents[ry] = rx
    else:
        parents[ry] = rx
        ranks[rx] += 1
```

### 최적화
- **Path Compression**: 탐색 시 루트로 바로 연결 → 깊이 축소
- **Union by Rank**: 랭크(트리 높이)가 낮은 집합을 높은 집합 밑으로 합침

---

## 오늘 느낀 점
- 그래프는 다양한 실생활 문제(네트워크, 지도 탐색 등)에 바로 적용 가능
- DFS·BFS의 차이와 구현 패턴이 명확해졌다.
- Union–Find의 경로 압축·랭크 기법으로 효율을 크게 개선할 수 있음을 이해했다.

---
