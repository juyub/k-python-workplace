# 간단한 논리 연산

# 주사위 게임2
a, b, c, d = 1, 2, 3, 4  # 예시 입력
answer = 0

# 인터넷 풀이
# dice = [a, b, c, d]
# arr = list(set(dice))
#
# if len(arr) == 1:
#     answer = 1111 * a
# elif len(arr) == 2:
#     if max([dice.count(num) for num in arr]) > 2:
#         p = max(dice, key=dice.count)
#         q = min(dice, key=dice.count)
#         answer = pow(((10 * p) + q), 2)
#     else:
#         answer = ((arr[0] + arr[1]) * abs(arr[0] - arr[1]))
# elif len(arr) == 3:
#     p = max(dice, key=dice.count)
#     tmp = [num for num in arr if num != p]
#     answer = tmp[0] * tmp[1]
# elif len(arr) == 4:
#     answer = min(dice)
# print(answer)

# gpt 풀이
# def solution(a, b, c, d):
#     dice = [a,b,c,d]
#     unique_dice = set(dice)
#
#     # 네 주사위에서 나온 숫자가 모두 같다면
#     if len(unique_dice) == 1:
#         return 1111 * a
#
#     # 세 주사위에서 나온 숫자가 같고 나머지 다른 주사위에서 나온 숫자가 다르다면
#     elif len(unique_dice) == 2:
#         for num in unique_dice:
#             if dice.count(num) == 3:
#                 return (10*num + (sum(dice)-3*num))**2
#
#         # 두 개의 주사위에서 각각 같은 값이 나오는 경우
#         p, q = unique_dice
#         return (p+q)*abs(p-q)
#
#     # 어느 두 개의 주사위에서 같은 값이 나오고, 나머지 두 개의 주사위에서 각각 다른 값을 가진 경우
#     elif len(unique_dice) == 3:
#         for num in unique_dice:
#             if dice.count(num) == 2:
#                 p = num
#                 break
#
#         q,r = [num for num in unique_dice if num != p]
#         return q*r
#
#     # 네 개의 주사위에 모두 다른 값이 적혀 있는 경우
#     else:
#        return min(a,b,c,d)


# 모두 같은 경우
if a == b == c == d:
    answer = 1111*a
    print("모두 같은 경우")

# 모두 다른 경우
elif a != b != c != d:
    answer = min(a,b,c,d)
    print("모두 다른 경우")

# 세 개가 같고 하나가 다른 경우
elif (a == b == c and a != d) or (a == b == d and a != c) or (a == c == d and a != b) or (b == c == d and b != a):
    if a == b == c:
        p = a
        q = d
    elif a == b == d:
        p = a
        q = c
    elif a == c == d:
        p = a
        q = b
    else:
        p = b
        q = a
    answer = ((10 * p) + q) * ((10 * p) + q)
    print("세 개가 같고 하나가 다른 경우")

# 두개씩 같은 경우
elif (a==b!=c!=d) or (a==c!=b!=d) or (a==d!=b!=c) or (b==c!=a!=d) or (b==d!=a!=c) or (c==d!=a!=b):
    if a == b and c == d:
        p = a
        q = c
    elif a == c and b == d:
        p = a
        q = b
    else:
        p = a
        q = b
    answer = (p + q) * abs(p - q)
    print("두개씩 같은 경우")

# 두 개가 같고 나머지 둘 각각 다른 경우
else:
    if a == b:
        p = a
        q = c
        r = d
    elif a == c:
        p = a
        q = b
        r = d
    else:  # in this case we know that a == d and b != c
        p = a
        q = b
        r = c
    answer = q * r
    print("두 개가 같고 나머지 둘 각각 다른 경우")
print(answer)


# 글자 이어 붙여 문자열 만들기
my_string = "cvsgiorszzzmrpaqpe"
index_list = [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]
my_string = list(my_string)
print(my_string)
answer = ''
for i in index_list:
    answer += my_string[int(i)]
print(answer)

# 9로 나눈 나머지
number = 123
number = list(str(number))
print(number)
answer = 0
for i in number:
    answer += int(i)
print(answer)

# 문자열 여러 번 뒤집기
my_string = "rermgorpsam"
queries = [[2, 3], [0, 7], [5, 9], [6, 10]]
# 나의 풀이
# my_string = list(my_string)
# for q in queries:
#     re_string = my_string[q[0]:q[1]+1]
#     re_string.reverse()
#     my_string = list(''.join(my_string[:q[0]]) + ''.join(re_string) + ''.join(my_string[q[1]+1:]))
# print(''.join(my_string))

# gpt 풀이
def solution(my_string, queries):
    my_list = list(my_string)
    for q in queries:
        my_list[q[0]:q[1]+1] = reversed(my_list[q[0]:q[1]+1])
    return ''.join(my_list)

print(solution(my_string, queries))

'''
reverse() - 메소드
리스트 객체에서만 사용할 수 있으며, 원본 리스트 자체를 바꿉니다.
즉, 리스트의 요소들의 순서를 직접 뒤집습니다. 반환값은 없습니다(None).

my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # 출력: [3, 2, 1]

reversed() - 함수
어떤 반복 가능한 객체에도 사용할 수 있으며(예: 리스트, 문자열, 튜플 등),
원본 객체를 변경하지 않고 역순 iterator를 반환합니다.
이 iterator는 필요에 따라 새로운 반전된 시퀀스로 변환될 수 있습니다.

my_str = "abc"
rev_str = reversed(my_str)
print(''.join(rev_str))  # 출력: "cba"

reversed() 함수가 반환하는 것은 역순 iterator이므로
이것을 다시 문자열 등으로 변환하기 위해서는 추가적인 작업(예: ''.join(rev_str))이 필요합니다.
'''