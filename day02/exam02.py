data = [10, 40, 20, 70, 50, 60, 30, 50]

'''
maximum = data[0]
minimum = data[0]

for d in data:
    if minimum > d:
        mininum = d
    if maximum < d:
        maximum = d
'''

sortData = sorted(data)
maximum = sortData[-1]
minimum = sortData[0]
print(f'가장큰수 : {maximum}, 가장작은수 : {minimum}')
print(f'가장큰수 : {max(data)}, 가장작은수 : {min(data)}')   # sum도 있음
print(f'총합 : {sum(data)}')



