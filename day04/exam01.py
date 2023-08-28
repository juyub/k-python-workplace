data = {}          # dict
data = {1, 2, 3}   # set
print(type(data))

# data = set{}
data = set([1, 2, 3, 4])
print(type(data), data)

data2 = {1, 4, 5, 6}
print(type(data2), data2)

print(f'합집합(data, data2) : {data.union(data2)}')
print(f'합집합(data, data2) : {data | data2}')
print(f'교집합(data, data2) : {data.intersection(data2)}')
print(f'교집합(data, data2) : {data & data2}')
print(f'차집합(data, data2) : {data.difference(data2)}')
print(f'차집합(data, data2) : {data - data2}')
print(f'대칭차집합(data, data2) : {data.symmetric_difference(data2)}')
print(f'대칭차집합(data, data2) : {data ^ data2}')
print(data, data2)      # 원본은 바뀌지 않음



