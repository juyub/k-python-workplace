data = [10, 20, 30, 40]

print(data, type(data))

print(*data)    # print(*[10, 20, 30, 40])  # print(10, 20, 30, 40)

def getTotal(a,b,c,d):
    return a+b+c+d

print(f'종합 : {getTotal(1,2,3,4,)}')
print(f'종합 : {getTotal(10,20,5,6)}')
print(f'종합 : {getTotal(*[10, 20, 30, 40])}')

'''
def getSum(nums):
    s = 0
    for n in nums:
        s += n
    return s
'''
def getSum(*nums):
    # print(nums, type(nums))
    s = 0
    for n in nums:
        s += n
    return s

# print(getSum([10,20,30,40]))
print(getSum(10,20,30,40))
print(getSum(10,20,30,40,50,60))
print(getSum(10,20,30))

