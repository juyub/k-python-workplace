# 홀짝에 따라 다른 값 반환하기
a = 10

answer = 0
for i in range(a+1):
    if a % 2 != 0:
        if i % 2 != 0:
            answer += i
    else:
        if i % 2 == 0:
            answer += i*i
print(answer)

# 조건 문자열
ineq = "<"
eq = "="
n = 20
m = 50
# 참이면 1
if ineq == "<":
    if n < m:
        print(1)



# flag에 따라 다른 값 반환하기
a = -4
b = 7
flag = 'false'

answer = 0
if flag == 'True':
    answer = a + b
elif flag == 'false':
    answer = a-b
print(answer)
