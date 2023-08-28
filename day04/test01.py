'''
    input.txt 읽어 다음의 결과를 출력하시오
    1. 총 단어의 개수 세어보기
    2. 단어의 빈도수 (알파벳순으로 출력)
        a       15
        above   1
        ...
    3. 단어가 몇번째 라인에 나왔는지 출력
        a   15  2,3,5,11,
        ...
'''
from collections import Counter

lines = ''
with open('input.txt', 'r') as file:
    for line in file:
        # print(line.rstrip('\n'))
        lines += line.rstrip('\n')
print(lines)

a = list(lines.split())
a = [s.lower() for s in a]
# a = [s.replace(',', '').replace('.', '').replace(' ', '') for s in a]
a = [s.rstrip(',').rstrip('.').rstrip(' ').rstrip(';') for s in a]
print(len(a))
b = dict(Counter(a))
b = sorted(b.items())
for key, value in b:
    print(f'{key.ljust(12)} : {value}')


