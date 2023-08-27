# range형 객체는 연산이 안됨
'''
list()      # []    [10,20,30]
tuple()     # ()    (10,20,30)
str()       # ""    "Hello"
dict()      # {}    {key:value,key:value,key:value}
'''

data = {'hong':1111, 'kang':2222, 'han':3333, 'park':4444}
print(data, type(data))
data = {'hong':1111, 'kang':2222, 'han':3333, 'park':4444, 'kang':5555}
print(data, type(data))
data = {'hong':1111, 'kang':2222, 'han':3333, 'park':4444, 'kang':5555, 100:'max'}
print(data, type(data))

stuInfo = {'name':'hong', 'age':28, 'score':[100,100,70]}
print(stuInfo)

data = {}
data = dict()
# data = dict(key=value, key=value, ...)    'key' 작은 따옴표 붙이 않음/ value는 문자면 작은 따옴표를 붙여야 함
data = dict(name='hong', age=28, addr='seoul')   # key는 문자형태만 가능
data = dict([('name', 'hong'), ('age', 28), ('addr', 'seoul'), (100, 'max')])   # key를 tuple의 형태로 하면 숫자를 쓸 수있다
data = dict(zip(['name', 'age', 'addr'], ['hong', 28, 'seoul']))
print(data, type(data))
print(zip(['name', 'age', 'addr'], ['hong', 28, 'seoul']))
