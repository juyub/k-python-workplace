#
my_string = "Progra21Sremm3"
s = 6
e = 12
answer = ''
my_string = list(my_string)
re_string = ''
for i in range(e,s-1,-1):
    re_string += my_string[i]
print(re_string)
answer = ''.join(my_string[:s]) + re_string + ''.join(my_string[e+1:])
print(answer)

#
my_string = "ihrhbakrfpndopljhygc"
m, c = 4, 2
print(len(my_string))
sub_string = []
answer = []
for i in range(0,len(my_string)-m+1,m):
    sub_string.append([my_string[a] for a in range(i,i+m)])
print(sub_string)
for i in range(len(sub_string)):
    answer.append(sub_string[i][c-1])
print(''.join(answer))

#
code = "qjnwezgrpirldywt"
print(len(code))
q, r = 3, 1
code = list(code)
answer = []
for i in range(len(code)):
    if i % q == r:
        answer.append(code[i])
print(''.join(answer))

