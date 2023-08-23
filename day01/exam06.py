"""
    int r= (int)(Math.random() * 10);  //(int)0.0 ~ (int)9.99  0 ~ 9

    if ( r%2 == 0 )
        sysout("짝수다");
    else {
        sysout("홀수다");
    }
"""

"""
    import random
    
    # print(int(random.random() * 10))
    r = int(random.random() * 10)
    # print(r)
    
    # 들여쓰기 반드시 지켜줘야 함
    if r % 2 == 0:
        print(f'{r} : 짝수')
    else:
        print(f'{r} : 홀수')
"""

num = int(input('정수 입력 : '))

# 파이썬에서 0은 거짓(false)으로 간주되며, 0이 아닌 모든 숫자는 참(true)으로 간주
"""
    if num > 0:
        if num % 2:
            print(num, ' : 홀수')
        else:
            print(num, ' : 짝수')
    else:
        print('음수')
"""
if num < 0:
    print('음수')
elif num % 2:
    print(num, ' : 홀수')
else:
    print(num, ' : 짝수')

