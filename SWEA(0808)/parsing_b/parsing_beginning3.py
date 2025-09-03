# text = 'B[45]AB[9994]'
#
# def get_find(text):
#     if text.find('[') == -1:
#         return ''
#     start = text.find('[') + 1
#     end = text.find(']')
#     return text[start:end]
#
# for


text = 'B[45]AB[9994]'

a = text.find('[')
b = text.find(']', a + 1)
c = text.find('[', b + 1)
d = text.find(']', c + 1)

t1 = text[a+1 : b]
t2 = text[c+1 : d]

print(int(t1) + int(t2))