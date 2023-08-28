# 코드 처리하기
'''
code를 앞에서부터 읽으면서 만약 문자가 "1"이면 mode를 바꿉니다.
mode에 따라 code를 읽어가면서 문자열 ret을 만들어냅니다.
mode는 0과 1이 있으며, idx를 0 부터 code의 길이 - 1 까지 1씩 키워나가면서 code[idx]의 값에 따라 다음과 같이 행동합니다.

mode가 0일 때
code[idx]가 "1"이 아니면 idx가 짝수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
code[idx]가 "1"이면 mode를 0에서 1로 바꿉니다.
mode가 1일 때
code[idx]가 "1"이 아니면 idx가 홀수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
code[idx]가 "1"이면 mode를 1에서 0으로 바꿉니다.
문자열 code를 통해 만들어진 문자열 ret를 return 하는 solution 함수를 완성해 주세요.

단, 시작할 때 mode는 0이며, return 하려는 ret가 만약 빈 문자열이라면 대신 "EMPTY"를 return 합니다.
'''
'''
mode 0 일때 i가 짝수일때만 ret 뒤에 code[i] 추가
mode 1 일때 i가 홀수일때만 ret 뒤에 code[i] 추가
'''
'''
i	code[i]	mode	ret
0	"a"	    0	"a"
1	"b"	    0	"a"
2	"c"	    0	"ac"
3	"1"	    1	"ac"
4	"a"	    1	"ac"
5	"b"	    1	"acb"
6	"c"	    1	"acb"
7	"1"	    0	"acb"
8	"a"	    0	"acba"
9	"b"	    0	"acba"
10	"c"	    0	"acbac"
'''
'''
mode 0 일때 i가 짝수일때만 ret 뒤에 code[i] 추가
mode 1 일때 i가 홀수일때만 ret 뒤에 code[i] 추가
'''
code = "abc1abc1abc"
code = list(code)
mode = 0
ret = ''
for i in range(len(code)):
    if mode == 0:
        if code[i] == '1':
            mode = 1
            continue
        if i % 2 == 0:
            ret += code[i]
    elif mode == 1:
        if code[i] == '1':
            mode = 0
            continue
        if i % 2 != 0:
            ret += code[i]
if ret == '':
    ret = 'EMPTY'

print(ret)

# 등차수열의 특정한 항만 더하기
'''
두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다.
첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때,
이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 return
'''
a, d = (3, 4)
included = [true, false, false, true, true]
print(len(included))

key = []
for i in range(len(included)):
    key.append(a + (d * i))
print(key)

result_dict = {k: v for k, v in zip(key, included)}
print(result_dict)

sum_keys = sum(k for k, v in result_dict.items() if v == 'true')
print(sum_keys)

key = []
for i in range(len(included)):
    key.append(a + (d * i))
result_dict = {k: v for k, v in zip(key, included)}
sum(k for k, v in result_dict.items() if v == True)

# 주사위 게임 2
'''
    세 주사위를 굴렸을 때 나온 숫자를 각각 a, b, c
    세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
    세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 (a + b + c) × (a2 + b2 + c2 )점을 얻습니다.
    세 숫자가 모두 같다면 (a + b + c) × (a2 + b2 + c2 ) × (a3 + b3 + c3 )점을 얻습니다.
'''
a, b, c = (5, 3, 3)
if a != b != c:
    print(a+b+c)
elif (a == b and b != c) or (b == c and a != b) or (a == c and a != b):
    print((a+b+c)*(a*a+b*b+c*c))
elif a == b == c:
    print((a+b+c)*(a*a+b*b+c*c)*(a*a*a+b*b*b+c*c*c))
'''
a = b / c
a / b=c
a=c / b
'''

# 원소들의 곱과 합
# 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return
num_list = [3, 4, 5, 2, 1]
a = 1
b = 0
for i in num_list:
    a = a * i
    b = b+i
print(a)
print(b)
print(b*b)
if a < b*b:
    print(1)
else:
    print(0)



# 이어 붙인 수
num_list = [3, 4, 5, 2, 1]
a = []
b = []
for i in range(len(num_list)):
    if num_list[i] % 2 != 0:
        a.append(num_list[i])
    else:
        b.append(num_list[i])
print(a)
print(b)
str_a = []
str_b = []
for i in range(len(a)):
    str_a += str(a[i])

for i in range(len(b)):
    str_b += str(b[i])
str_a = ''.join(str_a)
str_b = ''.join(str_b)
print(int(str_a)+int(str_b))

