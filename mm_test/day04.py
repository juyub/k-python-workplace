# 피자
slice = 7
n = 10
sum = 0
for i in range(n):
    if 7*i < n:
        sum = sum + 7*i


# 배열의 평균값
a = [i+1 for i in range(10)]
print(a)
answer = 0
sum = 0
for i in a:
    sum = sum + i
print(sum)
print(len(a))
answer = sum / len(a)
print(answer)
