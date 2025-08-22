# 문자열 text에서 대괄호 안에 있는 숫자를 추출해 보세요.
#
# find() 메서드를 사용해 주세요.

text = 'helloworld[92084]answer'

f_str = text.find('92084', 0)
print(text[f_str: f_str + 5]) # 92084

# 강사님 풀이
text = 'helloworld[92084]answer'

# 1) '[' 위치찾기
start_idx = text.find('[') + 1

# 2) ']' 위치찾기
end_idx = text.find(']')

# 슬라이싱
number = text[start_idx : end_idx]
print(number)