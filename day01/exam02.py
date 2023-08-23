'''
num01 = int(input('첫번째 정수를 입력 : '))
num02 = int(input('두번째 정수를 입력 : '))
print(num01, num02)
'''

'''
map(int, ['12', '5']) ==> int('12') int('5')
print(type('12, 5'.split()))
num01, num02 = input('두 개의 정수를 입력 : ').split()
print(type(num01), type(num02))
'''

num01, num02 = map(int, input('두 개의 정수를 입력 : ').split(':')) # .split() 의 기본은 공백
print(type(num01), type(num02))

