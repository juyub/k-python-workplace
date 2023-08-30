# print('abc')
# print(10)
# print([1,2,3,4,5],[10,20,30,40])
# print(10,20,30,40,'abc', end='', sep='')

def myPrint(*values, end='>', sep='\t'):
    for value in values:
        print(value, end=end, sep=sep)

myPrint(10, end='\n')
myPrint(10, 'A')
myPrint((10,20,30,40),[100,200,300,400])

print()
print()

'''
def calc(mode, *values):
    if mode == 'add':
        answer = 0
        for value in values:
            answer += value
    if mode == 'mul':
        answer = 1
        for value in values:
            answer *= value
    return answer
'''
def calc(command, *args):
    # print('command : ', command)
    # print('args : ', args)

    # if command == 'add':
    #     return sum(args)

    s = 0 if command == 'add' else 1
    for value in args:
        if command == 'add':
            s += value
        elif command == 'mul':
            s *= value
    return s

print(calc('add', 12, 7))
print(calc('add', 12, 6, 9))
print(calc('mul', 12, 7))
print(calc('mul', 1, 2, 3, 4, 5))

# 고민해보기
# print(calc('add', 12, [6, 9, 10]))

