# 마지막 두 원소
'''
정수 리스트 num_list가 주어질 때,
마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을
마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가
'''
num_list = [5, 2, 1, 7, 5]
print(num_list[-1])
if num_list[-2] < num_list[-1]:
    num_list.append(num_list[-1] - num_list[-2])
else:
    num_list.append(num_list[-1]*2)
print(num_list)

# 수 조작하기 1
'''
"w" : n이 1 커집니다.
"s" : n이 1 작아집니다.
"d" : n이 10 커집니다.
"a" : n이 10 작아집니다.
'''

control = "wsdawsdassw"
n = 0

control = list(control.lower())

for i in range(len(control)):
    if control[i] == 'w':
        n += 1
        continue
    if control[i] == 's':
        n -= 1
        continue
    if control[i] == 'd':
        n += 10
        continue
    if control[i] == 'a':
        n -= 10
        continue

print(n)

# 수 조작하기 1
'''
"w" : n이 1 커집니다.
"s" : n이 1 작아집니다.
"d" : n이 10 커집니다.
"a" : n이 10 작아집니다.
'''
numLog = [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]
result = ''
for i in range(len(numLog)-1):
    if int(numLog[i+1]) - int(numLog[i]) == 1:
        result += 'w'
        continue
    if int(numLog[i+1]) - int(numLog[i]) == -1:
        result += 's'
        continue
    if int(numLog[i+1]) - int(numLog[i]) == 10:
        result += 'd'
        continue
    if int(numLog[i+1]) - int(numLog[i]) == -10:
        result += 'a'
        continue
print(result)

# 수열과 구간 쿼리 3
arr = [0, 1, 2, 3, 4]
queries = [[0, 3],[1, 2],[1, 4]]
answer = list(arr)
for q in queries:
    answer[q[1]] = arr[q[0]]
    answer[q[0]] = arr[q[1]]
    arr = list(answer)
print(answer)

# 수열과 구간 쿼리 2
arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 2],[0, 3, 2],[0, 2, 2]]
# answer = []
# qu = []
# for i in queries:
#     if i[2] < i[1]:
#         qu.append([a for a in range(i[2]+1,i[1]+1)])
#     else:
#         qu.append(-1)
# print(qu)
# for q in qu:
#     if q != -1:
#         answer.append(min([arr[i] for i in q]))
#     else:
#         answer.append(-1)
# print(answer)

# answer = []
# for q in queries:
#     if q[2] < q[1]:
#         min_val = float('inf')   # 초기 최솟값 설정
#         for i in range(q[2]+1,q[1]+1):
#             if arr[i] < min_val:
#                 min_val = arr[i]
#         answer.append(min_val)
#     else:
#         answer.append(-1)
# print(answer)

answer = []
for q in queries:
    s, e, k = q[0], q[1], q[2]
    min_vals = []   # k보다 큰 값들을 저장할 리스트

    for i in range(s,e+1):
        if arr[i] > k:
            min_vals.append(arr[i])

    if min_vals:  # 리스트가 비어있지 않은 경우
        answer.append(min(min_vals))
    else:
        answer.append(-1)
print(answer)

