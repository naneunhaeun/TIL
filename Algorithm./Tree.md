# 📅 2025.08.29

# 🌳 트리 (Tree)

## 📌 개념
- 비선형 구조
- 원소들 간 **1:N 관계**를 가지는 자료구조
- 원소들 간 **계층 구조**를 가짐
- 상위 원소에서 하위 원소로 확장되는 **나무 모양 구조**

---

## 📌 정의
- 한 개 이상의 **노드(node)**로 이루어진 유한 집합
  - 최상위 노드 = **루트(root)**
  - 나머지 노드들은 `T1, T2, ... , Tn` 의 부분 트리(subtree)로 분리됨 → **재귀적 정의**

---

## 📌 용어 정리
- **노드(node)**: 트리의 원소
- **간선(edge)**: 부모 ↔ 자식 연결 선
- **루트 노드(root)**: 시작 노드
- **형제 노드(sibling)**: 같은 부모를 가진 노드
- **조상 노드(ancestor)**: 루트까지 경로 상의 모든 노드
- **자손 노드(descendant)**: 서브 트리에 속한 모든 하위 노드
- **서브 트리(subtree)**: 간선을 끊었을 때 생기는 작은 트리
- **차수(degree)**  
  - 노드 차수: 자식 노드 개수  
  - 트리 차수: 모든 노드 차수 중 최댓값
- **단말 노드(leaf)**: 자식 없는 노드 (차수 0)
- **높이(height)**  
  - 노드 높이: 루트에서 해당 노드까지의 간선 수  
  - 트리 높이: 모든 노드 높이 중 최댓값

---

## 📌 이진 트리 (Binary Tree)
- 모든 노드가 최대 2개의 자식만 가지는 트리
  - 왼쪽 자식 (left child)
  - 오른쪽 자식 (right child)

### 종류
- **포화 이진 트리**: 모든 레벨이 꽉 찬 트리
- **완전 이진 트리**: 마지막 레벨을 제외하고 모두 채워지고, 마지막 레벨은 왼쪽부터 채워진 트리
- **편향 이진 트리**: 한쪽으로만 자식이 연결된 트리

---

## 📌 순회 (Traversal)
트리의 모든 노드를 중복 없이 방문하는 방법

### 전위 순회 (Preorder, VLR)
부모 → 왼쪽 → 오른쪽
```python
def pre_order(T):
    if T:
        print(T)           # V
        pre_order(left[T]) # L
        pre_order(right[T])# R

중위 순회 (Inorder, LVR)

왼쪽 → 부모 → 오른쪽

def in_order(T):
    if T:
        in_order(left[T])  # L
        print(T)           # V
        in_order(right[T]) # R

후위 순회 (Postorder, LRV)

왼쪽 → 오른쪽 → 부모

def post_order(T):
    if T:
        post_order(left[T]) # L
        post_order(right[T])# R
        print(T)            # V

📌 이진 탐색 트리 (BST)

탐색을 빠르게 하기 위한 이진 트리

규칙:
왼쪽 < 루트 < 오른쪽

특징

모든 원소는 **유일한 키(key)**를 가짐

중위순회 → 오름차순 정렬

평균 시간 복잡도

탐색: O(log N)

삽입: O(log N)

삭제: O(log N)

📌 힙 (Heap)

완전 이진 트리 기반의 자료구조

부모와 자식 간 우선순위 관계 존재

종류

최대 힙 (Max Heap): 부모 ≥ 자식

최소 힙 (Min Heap): 부모 ≤ 자식

연산

삽입 (enq)

삭제 (deq) → 항상 루트만 삭제 가능

# 최대 힙 구현
def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

def deq():
    global last
    tmp = heap[1]
    heap[1] = heap[last]
    last -= 1
    p = 1
    c = p * 2
    while c <= last:
        if c + 1 <= last and heap[c] < heap[c+1]:
            c += 1
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p * 2
        else:
            break
    return tmp


✅ 오늘 배운 핵심

트리 기본 개념 & 용어

이진 트리 종류

순회 방법 (전위/중위/후위)

이진 탐색 트리 원리

힙 구조 & 구현
