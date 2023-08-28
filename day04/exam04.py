'''
    open(파일명, 모드)   # "r","w" 모드
    read()/write()
    close()

    with open() as 파일객체:    # 자동으로 close됨(자동 호출)
        read()/write()      # 들여쓰기 필요
'''

'''
file = open('text.txt', "w")
file.write('hello')
file.close()
'''
'''
file = open('text.txt', 'r')
# file = open('text2.txt', 'r')     # 없는 파일을 열면 예외 발생
data = file.read()
file.close()
'''

# close()를 쓰지 않는 방식(close()를 자동 호출)
with open('text.txt', 'r') as file:
    data = file.read()

print(f'읽어온 데이터 : {data}')



