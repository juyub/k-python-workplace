# 외계행성의 나이
age = 23
age = list(str(age))
print(age)
answer = ''
for a in age:
    answer += chr(int(a)+97)
print(answer)

# 진료 순서 정하기
emergency = [1, 2, 3, 4, 5, 6, 7]
answer = [0 for i in range(len(emergency))]
print(answer)
print(max(emergency))
print(emergency.index(max(emergency)))
for i in range(len(emergency)):
    answer[emergency.index(max(emergency))] = i+1
    print(answer)
    emergency[emergency.index(max(emergency))] = 0

# 순서쌍의 개수
n = 20
answer = []
for i in range(1,n+1):
    if n % i == 0:
        answer.append(f'{i}, {n//i}')
print(len(answer))
