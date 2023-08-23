"""
    20~50 사이 랜덤 숫자 축출
    34
    1                       짝
    2                       짝
    짝                       짝짝
    4                       짝
    5
    짝
    7
    8
    짝
    뽀숑  뽀뽀숑 뽀뽀뽀숑 짝
"""

import random

num = random.randint(20,50)

print(num)

"""
for i in range(1, num + 1):
    num_str = str(i)
    if '0' in num_str:
        if '3' in num_str or '6' in num_str or '9' in num_str:
            print('뽀'*(int(num_str)//10)+'쑝', '짝')
        else:
            print('뽀'*(int(num_str)//10)+'쑝')
    elif '3' in num_str or '6' in num_str or '9' in num_str:
        print('짝')
    else:
        print(i)
"""

"""
for i in range(1, num + 1):
    num_str = str(i)
    count = num_str.count('3') + num_str.count('6') + num_str.count('9')
    if '0' in num_str:
        if count > 0:
            print('뽀'*(int(num_str)//10)+'쑝', '짝'*count)
        else:
            print('뽀'*(int(num_str)//10)+'쑝')
    elif count > 0:
        print('짝'*count)
    else:
        print(i)

print()
"""

for i in range(1, num + 1):
    number = i
    count = 0
    count_10 = i // 10

    while number > 0:
        digit = number % 10
        if digit in (3, 6, 9):
            count += 1
        number //= 10

    if i % 10 == 0:  # 10의 배수일 때
        print('뽀' * count_10 + '쑝', end='')
        if count > 0:  # 3, 6, 9가 있다면 출력
            print(' 짝' * count)
        else:
            print()
    elif count > 0:
        print('짝' * count)
    else:
        print(i)

print()

"""
def check_count(number):
    count = 0
    while number > 0:
        digit = number % 10
        if digit in (3, 6, 9):
            count += 1
        number //= 10
    return count

for i in range(1, num + 1):
    count_369 = check_count(i)
    count_10 = i // 10

    if i % 10 == 0 and count_10 != 0:
        if count_369 > 0:
            print('뽀'*count_10 + '쑝', '짝'*count_369)
        else:
            print('뽀'*count_10 + '쑝')
    elif count_369 > 0:
        print('짝'*count_369)
    else:
        print(i)
"""
