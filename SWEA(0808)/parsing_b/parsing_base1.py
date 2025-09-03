text = list(input())

def is_same(text):
    return text == text[::-1]

print(int(is_same(text)))


