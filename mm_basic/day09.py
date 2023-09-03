#
intStrs = ["0123456789","9876543210","9999999999999"]
k, s, l = 50000, 5,	5
answer = []
c = []
for i in intStrs:
    b = list(i)
    c.append(''.join(b[s:s+l]))
for i in c:
    if int(i) > k:
        answer.append(i)
print(answer)

#
result = "programmers"

my_strings = ["progressive", "hamburger", "hammer", "ahocorasick"]
parts = [[0, 4], [1, 2], [3, 5], [7, 7]]
answer = ''
for i in range(len(my_strings)):
    a = list(my_strings[i])
    print(a)
    answer += ''.join(a[parts[i][0]:parts[i][1]+1])
    print(answer)

#
my_string = "banana"
# my_string = list(my_string)
# answer = []
# for i in range(len(my_string)):
#     answer.append(my_string[:i+1])
# print('순행', answer)
answer = []
for i in range(len(my_string), 0, -1):
    answer.append(my_string[-i:])
print('역행', sorted(answer))

#
my_string = "ProgrammerS123"
n = 11
my_string = list(my_string)
answer = []
for i in range(len(my_string)-1, len(my_string)-n-1,-1):
    answer.append(my_string[i])
answer.reverse()
print(''.join(answer))