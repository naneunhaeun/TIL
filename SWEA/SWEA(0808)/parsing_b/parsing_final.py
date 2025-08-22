# text = ['GOLDABCGOLD', 'HELLOWORLD', 'WHITEGOLD']
# a = 0
# b = 0
# cnt = 0
# word = GOLD
# while True:
#     b = text.find('GOLD', a)
#     if b == -1: break
#     cnt += 1
#     a = b + 1
#
# for word in text:
#     result =


arr = ['GOLDABCGOLD', 'HELLOWORLD', 'WHITEGOLD']

def get_count(word):
    cnt = 0

    for text in arr:
        a = 0
        while True:
            b = text.find(word, a)
            if b == -1: break
            cnt += 1
            a = b + 1
    return cnt
print(get_count('GOLD'))