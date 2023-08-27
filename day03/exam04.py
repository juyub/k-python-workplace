members = {'홍길동':'1111-2222','박길동':'3333-4444','윤길동':'5555-6666'}

print(members.keys())
print(members.values())
print(members.items())

# in 연산자로 value는 안되고 key로
print(f'홍길동 존재여부 : {"홍길동" in members}')
print(f'고길동 존재여부 : {"고길동" in members}')

for data in members:
    # print(data, end=' ')
    print(f'{data} : {members.get(data)}')
print()

# 더 직관적으로 보임
for data in members.keys():
    print(data, end=' ')
print()

for data in members.values():
    print(data, end=' ')
print()
print()

# .items()로 key, value 각각 받아옴
'''
a, b = [2,3]
nums = [2,3]
a, b = nums     # a = nums[0], b = nums[1]
print(f'a:{a}, b:{b}')
'''

for key, value in members.items():
    print(f'{key} : {value}')
print()

keys = ['name', 'age', 'addr']
mem = dict.fromkeys(keys, "")
print(mem)





