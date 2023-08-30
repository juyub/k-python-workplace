# 문자열 뒤집기
my_string = "jaron"
my_string = list(my_string)
string = ''
for i in range(len(my_string)):
    string += my_string[-i-1]
print(string)

# 직각삼각형 출력하기
n = 3
for i in range(n):
    print('*'*(i+1))

# 짝수 홀수 개수
num_list = [1, 2, 3, 4, 5]
odd = []
even = []
for num in num_list:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print(odd,even)
answer = [len(even), len(odd)]
print(answer)

# 문자 반복 출력하기
my_string = "hello"
n = 3

my_string = list(my_string)
print(my_string)
answer = ''
for str in my_string:
    answer += str * n
print(answer)