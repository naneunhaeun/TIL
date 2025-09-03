# 🗂️ TIL
📅 2025.09.03 수요일  

---

## 🔢 비트 연산 (Bitwise Operations)

- `&` 연산 (AND): 둘 다 1이면 1  
- `|` 연산 (OR): 하나라도 1이면 1  
- `^` 연산 (XOR): 같으면 0, 다르면 1  
  - 특이점: **같은 값을 두 번 XOR 하면 원래 숫자 복구 가능 (암호화/복호화 활용 가능)**
- `<<` 연산 (Left Shift): 왼쪽으로 비트 이동 (빈자리는 `0`으로 채움)
- `>>` 연산 (Right Shift): 오른쪽으로 비트 이동 (맨 오른쪽 1비트가 삭제됨)

---

## 📌 예제: break / continue 차이
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

🧮 이진수 표현 문제
방법 1: & 연산 활용
python
코드 복사
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
방법 2: >> 연산 활용
python
코드 복사
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
🧾 이진수로 변환 문제
소수 부분을 2진수로 변환하기.

python
코드 복사
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
    
✨ 오늘 배운 점
비트 연산은 마스크 연산, 비트 이동 등을 통해 효율적으로 특정 자리의 값을 확인할 수 있음.

xor 연산은 암호화/복호화 같은 트릭에 유용하게 쓰일 수 있음.

실수의 이진수 변환에서는 표현 가능 비트 수(여기선 13자리 제한)를 반드시 고려해야 함.