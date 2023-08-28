'''
    정수 2개 입력받아 최대공약수 출력
'''

num1, num2 = map(int, input().split(' '))

divNum1 = set([i for i in range(1, num1+1) if num1 % i == 0])
divNum2 = set([i for i in range(1, num2+1) if num2 % i == 0])

print(divNum1)
print(divNum2)

divisor = [n for n in divNum1 if n in divNum2]
'''
divisor = []
for n in divNum1:
    if n in divNum2:
        divisor.append(n)
print(divisor)
'''
print(f'최대 공약수 : {max(divisor)}')

# set { } :  교집합
print(f'최대 공약수 : {max(divNum1 & divNum2)}')