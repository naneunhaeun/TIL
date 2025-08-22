# text = 'ABCDEFABCKKKKKABC'
# cnt = 0
# while True:
#     text.find('ABC', 0)
#     if text.find('ABC') == -1: break
#
# for i in text_find():
#     cnt = 0
#
# print(cnt)

text = 'ABCDEFABCKKKKKABC'

a = 0
b = 0
cnt = 0

while True:
    b = text.find('ABC', a)
    # 더 이상 찾을 수 없을 때까지 반복
    if b == -1: break
    cnt += 1
    a = b + 1

print(cnt)
