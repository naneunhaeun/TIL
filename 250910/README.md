# 🗂️ TIL  
📅 2025-09-10 수요일  

---

## ✨ 오늘 배운 것: **분할 정복(Divide & Conquer)**

문제를 **작은 하위 문제로 나누고(분할)** → **각각 해결(정복)** → **결과를 통합** 하여 원래 문제를 해결하는 알고리즘 기법.

### 1️⃣ 핵심 설계 전략
- **Divide**: 문제를 여러 작은 부분으로 나눈다.  
- **Conquer**: 작은 문제를 각각 해결한다.  
- **Combine**: 필요한 경우, 해결된 결과를 모아 전체 문제의 해답을 만든다.

---

## 🧩 주요 알고리즘

### 🟢 병합 정렬 (Merge Sort)
- 여러 개의 **정렬된 자료 집합**을 병합해 하나의 정렬된 집합을 만드는 방식.
- **Top-down** 방식, 시간 복잡도 **O(n log n)**.
- 외부 정렬(External Sort)의 기본, 멀티코어 병렬 정렬 등에 활용.

<details>
<summary>파이썬 예제</summary>

```python
def merge_sort(li):
    if len(li) == 1:
        return li
    mid = len(li) // 2
    left = merge_sort(li[:mid])
    right = merge_sort(li[mid:])
    return merge(left, right)
```
</details>

---

### 🟠 퀵 정렬 (Quick Sort)
- Pivot(기준값)을 중심으로 **왼쪽은 작은 값**, **오른쪽은 큰 값**으로 분할 후 재귀적으로 정렬.
- 평균 시간 복잡도 **O(n log n)**.
- 대용량 데이터에 강력한 성능.

<details>
<summary>대표 코드</summary>

```python
def quick_sort(left, right):
    if left < right:
        pivot = hoare_partition(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)
```
</details>

---

### 🟡 이진 검색 (Binary Search)
- **정렬된 데이터**에서만 사용.
- 중간값과 목표값을 비교해 탐색 범위를 절반씩 줄이며 검색.
- Lower Bound / Upper Bound 로 확장 가능.

<details>
<summary>반복문 구현</summary>

```python
def binary_search_while(target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target: return mid
        if target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
```
</details>

---

## 📝 정리
- **병합 정렬**: 외부 정렬·병렬화에 유용.
- **퀵 정렬**: 평균적으로 가장 빠른 정렬 알고리즘 중 하나.
- **이진 검색**: 정렬된 데이터에서 빠른 탐색.

---

## 💡 오늘의 배움
- “분할하고 정복하라”는 전략이 단순히 정렬뿐 아니라 다양한 문제 해결 패턴에 적용될 수 있음을 이해.
- 병합·퀵 정렬의 파티셔닝 및 재귀 호출 흐름을 코드로 직접 구현하며 재귀적 사고를 강화.
- 이진 검색에서 **정렬된 데이터**라는 전제의 중요성을 재확인.

---

## ✅ 다음 목표
- Lower/Upper Bound 문제 심화 학습
- 퀵 정렬의 피벗 선택 전략별 성능 비교 실습
