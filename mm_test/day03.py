# Day3
# 더 크게 합치기
a = 9
b = 91
answer = max(int(str(a)+str(b)), int(str(b)+str(a)))
print(answer)

# 두 수의 연산값 비교하기
a = 2
b = 91
# answer = max(int(str(a)+str(b)), 2*a*b)
answer = max(int(f"{a}{b}"), 2*a*b)
# f"{a}{b}"
print(answer)