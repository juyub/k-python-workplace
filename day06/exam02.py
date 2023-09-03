'''
try:
    pass
except:
    pass
else:
    pass
finally:
    pass
'''

import random
try:
    num = random.randint(0, 2)
    result = 10/num
    print(f'10/{num} = {result}')
except Exception as e:
    print('예외발생! : ', e)
else:
    pass
finally:
    print('프로그램 종료...')