'''
def get_number():
    num = int(input('짝수를 입력하세요'))
    if num % 2:
        raise Exception(f'입력하신 정수 {num}은 짝수가 아닙니다')
    return num

try:
    num = get_number()
    print(num)
except Exception as e:
    print(e)
'''

def get_number():
    try:
        num = int(input('짝수를 입력하세요'))
        if num % 2:
            raise Exception(f'입력하신 정수 {num}은 짝수가 아닙니다')
        return num
    except:
        print('get_number() 예외발생')
        raise
    return num

try:
    num = get_number()
    print(num)
except Exception as e:
    print(e)

