# 한줄 주석

'''
여러줄 주석
'''

"""
여러줄 주석
"""

'''
알트 쉬프트 f10 : 실행 파일 지정
쉬프트 f10 : 실행했던 파일 실행
'''

'''
    정수 2개 입력받아 사칙연산의 결과 출력
'''

# 파이썬은 들여쓰기가 중요하므로 꼭 맞추어 써야 한다

print('첫번째 정수를 입력 : ', end='')    # end='\n'

# 데이터가 할당되면 타입이 정해짐
num01 = int(input())
# num01 = int(input('첫번째 정수를 입력 : '))
# print(type(num01))

print('두번째 정수를 입력 : ', end='')
num02 = int(input())

# print(num01, num02, sep=':')
print(num01, '+', num02, '=', num01 + num02)
print('%d - %d = %d' % (num01, num02, num01 - num02))
print('%d * %d = %d' % (num01, num02, num01 * num02))

# 파이썬이 자동으로 정수로 바꿔 줌 (java에서는 미스타입 오류)
# print('%d / %d = %d' % (num01, num02, num01 / num02))
print('%d / %d = %f' % (num01, num02, num01 / num02))
# print('%d / %d = %.2f' % (num01, num02, num01 / num02)) 결과값 소숫점 2자리

print('{0} / {1} = {2}'.format(num01, num02, num01 / num02))
                               # 인덱스   0      1         2
print(f'{num01} / {num02} = {num01 / num02}')
# print(f'{num01} / {num02} = {num01 / num02:.2f}') 결과값 소숫점 2자리

# 몫만 구하기
print(int(num01 / num02))
print(f'{num01} / {num02} = {num01 // num02}')

# 나머지 '%'
print(f'{num01} % {num02} = {num01 % num02}')

# 제곱
# print(2 ** 3)
print(f'{num01} ** {num02} = {num01 ** num02}')
# 문자열과 결합하면 '반복'
print('2' * 3)
