data = set()
print(f'{data} 원소의 개수 : {len(data)}')
for i in range(10):
    data.add(i+1)

data.add(5)     # 중복 허용 안함(같은 자료형)
                # set 자체가 중복 허용 하지 않음
data.add('5')

print(f'{data} 원소의 개수 : {len(data)}')

data.remove('5')
print(f'remove("5") 후 {data} 원소의 개수 : {len(data)}')
# data.remove('5')  # 요소가 존재하지 않으면 오류발생
data.discard(5)
print(f'discard(5) 후 {data} 원소의 개수 : {len(data)}')

# copy = data     # 얕은 복사
copy = data.copy()  # 깊은 복사 # set은 슬라이스가 안됨. "[:]"을 못 씀
print(f'data : {data}')
print(f'copy : {copy}')
copy.add(5)
print(f'data : {data}')
print(f'copy : {copy}')

a = "I am a boy."
b = set(a.lower())
c = ['a','e','i','o','u']
print(f'{b.difference(c)}')

