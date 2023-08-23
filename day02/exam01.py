'''
    list 내장함수
    append      : 데이터 추가(맨마지막)
    insert      : 데이터 추가(특정위치)
    pop         : 데이터 삭제(맨마지막)
    remove      : 데이터 삭제(특정데이터)
    index       : 특정값의 위치 검색
    count       : 특정값의 빈도수
    reverse     : 위치 뒤집기
    sort        : 정렬
    clear       : 리스트 요소 전부 삭제
'''

'''
stack : lifo
queue : fifo
'''

# 스택처럼 lifo
data = []
print(data, id(data))
data.append(10)
data.append(20)
data.append(30)
print(data, id(data))
delData = data.pop()
print('삭제된 값 : ', delData)

# 큐처럼 fifo
data = list()
data.insert(0,10)
data.insert(0,20)
data.insert(0,30)
print(data, id(data))
delData = data.pop()
print('삭제된 값 : ', delData)

data = []
data.append(10)
data.append(20)
data.append(30)
print(data, id(data))
delData = data.pop(0)
print('삭제된 값 : ', delData)

# index : 제일 처음 나온 데이터만 리턴
data = [10, 20, 30, 40, 30]
idx = data.index(30)
cnt = data.count(30)
print('위치 : ', idx)
print('개수 : ', cnt)
print('before : ', data)
# index가 적용되는 데이터가 지워짐
data.remove(30)
print('after : ', data)

# print(data[0], data[1], data[2])
for i in range(len(data)):
    print(data[i], end=' ')
    # print(data.__getitem__(i), end=' ')
print()

for d in data:
    print(d, end=' ')
print()

'''
ite = iter(data)
print(next(ite))
'''

for d in iter(data):
    print(d, end=' ')
print()

for index, d in enumerate(data):
    print(f'[{index}] : {d}')

for index, d in enumerate(data, start=100):
    print(f'[{index}] : {d}')

print(data[-1])
print(data[-2])

for i in range(1, len(data)+1):
    print(data[-i], end=' ')
print()

data.reverse()
print(data)
for d in iter(data):
    print(d, end=' ')
print()

data.reverse()
print(data)

data2 = reversed(data)
print('data : ', data)
print('data2 : ', next(data2))

for d in reversed(data):
    print(d, end=' ')
print()

data.sort()
print(data)

# reversed 속성 False(default, 오름 차순) = True(내림차순)
# print(sorted(data, reverse=True))
print(sorted(data))
print(data)

data = [10]

'''
    for i in range(len(data)):
        data.pop(0)
        
    for i in range(len(data)):
        del data[i]
        
    data.clear()
'''

del data[:]
print(data)
