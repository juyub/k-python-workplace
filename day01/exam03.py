# 논리값(True, False) 대문자로 시작
print(True, False)
print(10 > 3)
print(10 == 3)
print(10 != 3)
print("Hello" == "Hello")
print("Hello" == "hello")
print(1 == 1.0) # 값비교라서 True로 나옴
print(1 is 1.0) # id에 있는 고유값을 비교하므로 False로 나옴

# 'id' : 메모리에 저장된 위치값, 객체의 고유한 값
print(id('Hello'))
print(id('Hello'))
print(id('hello'))

print(id('1'))
print(id('1.0'))

# 0아닌 모든 값을 True로 인식
print(type(bool(int(str(10)))), bool(int(str(10))))
print(bool(1), bool(8), bool(1.5), bool('false'))
print("abc" and "def")  # 결론적으로 print("def")로 인식

# 시퀀스 자료형
msg = "hello" and "안녕"
msg = "hello" or "안녕"
print(msg)

print('Hello')
print('''Hello''')
print("""Hello
여러줄도 가능
또 라인변경""")
