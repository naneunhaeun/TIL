text = 'BBQBHCBTS'

dat = [0] * 200

for i in range(len(text)):
    dat[ord(text[i])] += 1 # 알파벳의 아스키코드 값을 인덱스로 사용
max_v = 0

for i in range(200):
    if dat[i] > max_v : max_v = dat[i] # 최댓값 갱신

print(max_v)
# count메서드나 counting하는 경우 시간복잡도가 O(n제곱)
# dat의 경우: O(n) -> 효율적

