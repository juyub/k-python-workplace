# Day3
# 중앙값 구하기
array = [9,-1,0,5]
a = [int(i) for i in array]
a.sort()
print(a)
print(a[len(a)-1])

if len(a) % 2 != 0:
    print(a[(len(a) // 2)])
else:
    print((a[0]+a[len(a)-1])//2)

# 최빈값 구하기
array = [1, 1, 2, 2, 3, 3]

from collections import Counter

# 중복 제거 및 빈도 계산
array_dict = dict(Counter(a))
print(array_dict)

# {value: key} 형태로 dictionary 변환
answer = max({v: k for k, v in array_dict.items()})
# 가장 큰 value를 가진 key 출력
print(answer)

array_dict = dict(Counter(array))
modes = [k for k,v in array_dict.items() if v == max(array_dict.values())]
print(modes)
answer = modes[0] if len(modes) == 1 else -1
print(answer)

## 순수 알고리즘 풀이
# 빈도수를 저장할 딕셔너리 초기화
freq_dict = {}

# array의 각 요소에 대해 빈도수 계산
for num in array:
    if num in freq_dict:
        freq_dict[num] += 1
    else:
        freq_dict[num] = 1

# 최빈값을 찾기 위한 변수 초기화
max_freq = -1
modes = []

# 빈도수 딕셔너리의 각 항목에 대해 반복하면서 최빈값 찾기
for num, freq in freq_dict.items():
    if freq > max_freq:  # 현재 빈도수가 이전 최빈값보다 크면 업데이트
        max_freq = freq
        modes = [num]
    elif freq == max_freq:  # 현재 빈도수가 이전 최빈값과 같으면 modes에 추가
        modes.append(num)

answer = modes[0] if len(modes) == 1 else -1   # 모드의 개수에 따라 반환 값 결정
print(answer)

'''
a = int(input())
if a % 2 == 0:
    print(str(a)+' is even')
else:
    print(str(a) + ' is odd')
'''

'''
numbers = list(input().split())
print(numbers)
for i in numbers[:]:
    numbers[i]=int(numbers[i])*2
print(numbers)
'''
'''
my_string = "He11oWor1d"
overwrite_string = "lloWorl"
s = 2
answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
print(answer)
'''
'''
arr = ["a","b","c"]
answer = ''.join(arr)
print(answer)
'''
'''
str1 = "aaaaa"
str2 = "bbbbb"
answer = ''
for i in range(max(len(str1), len(str2))):
    answer += str1[i] + str2[i]
print(answer)
'''

