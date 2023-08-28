# 문자열을 입력받아 모음을 제거하고 출력
# data = input()
data = input()
print(data)

# data2 = [s for s in data if s not in 'aeiouAEIOU']
# data2 = [s for s in data if s.isalpha() and s not in 'aeiouAEIOU']
# data2 = {s for s in data if s.isalpha() and s not in 'aeiouAEIOU'}
data2 = {s for s in data if s.isalpha() and s not in 'aeiouAEIOU '}    # 공백추가
print(data2)