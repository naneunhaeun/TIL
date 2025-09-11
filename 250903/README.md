# 🗂️ TIL

📅 2025.09.03 수요일

---

## 🔢 비트 연산 (Bitwise Operations)

* `&` 연산 (AND): 둘 다 1이면 1
* `|` 연산 (OR): 하나라도 1이면 1
* `^` 연산 (XOR): 같으면 0, 다르면 1

  * 특이점: **같은 값을 두 번 XOR 하면 원래 숫자 복구 가능 (암호화/복호화 활용 가능)**
* `<<` 연산 (Left Shift): 왼쪽으로 비트 이동 (빈자리는 `0`으로 채움)
* `>>` 연산 (Right Shift): 오른쪽으로 비트 이동 (맨 오른쪽 1비트가 삭제됨)

---

## 📌 break / continue 차이

```python
arr = [1, 2, 3, 4, 5]

for i in arr:
    if i == 3:
        break
    print(i)  
# 출력: 1 2

for i in arr:
    if i == 3:
        continue
    print(i)  
# 출력: 1 2 4 5
```

---

## 🧮 이진수 표현 문제

### 방법 1: `&` 연산 활용

```python
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    TOGGLE = "ON"
    for i in range(N):
        if M & (1 << i):
            continue
        TOGGLE = "OFF"
        break

    print(f'#{tc} {TOGGLE}')
```

### 방법 2: `>>` 연산 활용

```python
def solve():
    tar = M
    for i in range(N):
        if tar & 0x1 == 0:  # 맨 오른쪽 비트 확인
            return 'OFF'
        tar >>= 1           # 오른쪽으로 한 칸씩 이동
    return 'ON'

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    print(f'#{tc} {solve()}')
```

---

## 🧾 이진수로 변환 문제 

소수 부분을 2진수로 변환하기.

```python
def change(n):
    binary = ""
    power = -1  # 2의 -1제곱부터 시작
    cnt = 0

    while n > 0 and cnt < 13:
        value = 2 ** power
        if n >= value:        # 해당 자리값을 뺄 수 있다면
            binary += "1"
            n -= value
        else:
            binary += "0"

        power -= 1
        cnt += 1

    if n > 0:   # 13자리 넘어가도 표현 불가
        return 'overflow'
    else:
        return binary

T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    result = change(N)
    print(f'#{tc} {result}')
```

---

## 🔟 소수점을 가진 10진수를 2진수로 변환

* 예시 1: `0.75 → 0.11(2)`
* 예시 2: `0.40625 → 0.01101(2)`

👉 규칙: `2⁻¹, 2⁻², 2⁻³ …` 자리값을 차례대로 빼가며 0 또는 1 결정

---

## ✌️ 2의 보수 (Two’s Complement)

2의 보수를 만드는 방법:

1. 모든 비트를 뒤집는다 (0→1, 1→0).
2. 1을 더한다.

* 예시 1: 17의 2의 보수
  `10001 → 01110`
  `01110 + 1 → 01111 (= 15)`

* 예시 2: -5 표현
  `5 → 00000101`
  `뒤집기 → 11111010`
  `1 더하기 → 11111011`

---

## 🚫 NOT 연산과 음수 표현

예: -5를 NOT 연산으로 표현

* 5를 이진수로: `00000101`
* NOT 연산 → `11111010`
* 2의 보수 취하기 → `11111011`
* 최종값 = -5

---

## ✨ 오늘 배운 점

* 소수 부분의 이진수 변환은 2의 거듭제곱 역수를 차례대로 빼면서 구한다.
* 2의 보수는 음수 표현의 핵심 방식으로, **비트 반전 후 +1**로 얻을 수 있다.
* NOT 연산 역시 음수 표현과 연계되어, 2의 보수 과정에서 중요한 역할을 한다.
