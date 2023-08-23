num = 1
# 증가나 감소 연산자가 없음
while num <= 10:
    print(num, end=' ')
    num += 1
print()

# for 변수 in range(횟수):
for i in range(1,11):
    print(i, end=' ')
print()

for i in range(10):
    print(i+1, end=' ')
print()

for i in range(10):
    if (i+1) % 2:
        print(i+1, end=' ')
print()

for i in range(0, 10, 2):
    print(i+1, end=' ')
print()

# range 대신 시퀀스형은 다 가능
names = ['홍길동', '강길동', '윤길동']
for name in names:
    print(name, end=' ')
print()

for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()

for i in range(5):
    print('*' * (i+1))
print()

for i in range(9):
    if i < 5:
        print('*' * (i+1))
    else:
        print('*' * (9-i))
print()

for i in range(9):
    # 참문장 if 조건식 else 거짓문장
    cnt = (i+1) if i < 5 else (9-i)
    print('*' * cnt)
print()

for i in range(5):
    print(' ' * i, end='')
    print('*' * (5-i))
print()

