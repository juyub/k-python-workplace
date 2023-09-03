'''
try:
    pass
except:
    pass
'''

import random
try:
    num = random.randint(0,2)
    print('추출된 난수 : ', num)
    print(10/num)
    data = [10, 20]
    print(data[2])
# except Exception as e:    모든 예외를 Exception해서 받을 수도 있음
except ZeroDivisionError as e:
    print('ZeroDivisionError 예외발생!!!', e)
except IndexError as e:
    print('IndexError 예외발생!!!', e)



