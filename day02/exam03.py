# 1 ~ 10 사이의 정수 10개를 원소로 가지는 리스트 data 선언
'''
data = list(range(1,11))
print(data)
'''
# 방법 1
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(data)

# 방법 2
data = list()
for i in range(10):
    data.append(i+1)
print(data)

# 방법 3 : 리스트 컴프리헨션(list comprehension)방식
data = [i+1 for i in range(10)]
print(data)

data = [i+1 for i in range(10) if (i+1) % 2]
print(data)

data = [2*i+1 for i in range(5)]
print(data)

# 구구단 데이터 생성
dan = 4
guguData = [dan*i for i in range(1, 10)]
print(guguData)
print()

guguData = [dan*i for dan in range(2, 10) for i in range(1, 10)]
print(guguData)
print()

guguData = [dan*i for dan in range(2, 10) for i in range(1, 10)]
for index, value in enumerate(guguData):
    print(value, end=' ')
    if (index + 1) % 9 == 0: # 'i'가 한 바퀴 돌 때마다 (즉 매9번째 요소에서)
        print() # 줄바꿈을 합니다.
print()

guguData = [[dan*i for i in range(1, 10)] for dan in range(2, 10)]
for dan in guguData:
    print(dan)
print()

strData = ['hello', 'good', 'bye', 'welcome', 'apple', 'sorry']
fiveStrData = [s for s in strData if len(s) == 5]
print(fiveStrData)
print()

copyStrData = strData[:]
copyStrData2 = strData.copy()

print('strData : ', strData, id(strData))
print('copyStrData : ', copyStrData, id(copyStrData))
print('copyStrData2 : ', copyStrData2, id(copyStrData2))

'''
오류
tupleData = tuple()
tupleData.__add__(10)
print(tupleData)
'''

