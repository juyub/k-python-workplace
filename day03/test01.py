'''
    정수 2개 입력받아 최대공약수 출력
'''

num = input()
answer = [int(i) for i in num if num % i == 0]
print(answer)