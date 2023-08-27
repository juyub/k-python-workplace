str = "Hello, World"
print(str, str.upper(), str.lower())
print(str)

strList = str.split(',')
print(strList)
str2 = '/'.join(strList)
print(str2)
'''
a = ['ab','cd','efg']
b = ''.join(a)          # abcdefg
c = '-'.join(a)         # ab-cd-efg
d = ' : '.join(a)       # ab : cd : efg
'''
print(f'[{strList[1]}]')
print(f'[{strList[1].lstrip()}]')

str = '  !  Hello World    '
print(f'str : [{str}]')
print(f'lstrip() : [{str.lstrip(" !")}]')
print(f'rstrip() : [{str.rstrip()}]')
print(f'strip() : [{str.strip("! ")}]')

str = 'hello'
print(f'str : [{str}]')
print(f'str : [{str.center(11)}]')
print(f'str : [{str.center(10)}]')
print(f'str : [{str.ljust(10)}]')
print(f'str : [{str.rjust(10)}]')
print(f'str : [{str.zfill(10)}]')

str = 'Hello World!!'
# index는 없으면 예외 발생 / find 는 없으면 '-1' 반환
print(f'"0" 위치 : {str.index("o")}')
print(f'"0" 위치 : {str.find("p")}')
print(f'"0" 위치 : {str.rfind("o")}')    # 오른쪽에서 왼쪽으로 검색
print(f'"l" 개수 : {str.count("l")}')
print(f'"l" => "rr" 변환 : {str.replace("l","rr")}')




