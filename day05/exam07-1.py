# __ 비공개의 의미. 외부에서는 사용할 수 없음

class Person:
    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.__addr = addr

    @property
    def addr(self):
        return self.__addr

    def getAddr(self):
        return self.__addr

    @addr.setter
    def addr(self, addr):
        self.__addr = addr

    def setAddr(self, addr):
        self.__addr = addr

    def info(self):
        print(f'name : {self.name}, age : {self.age}, addr : {self.__addr}')

p = Person('홍길동', 25, '서울')
p.info()
print(p.name)
print(p.age)

# __를 쓰면 사용 할 수 없음
# print(p.__addr)
print(p.getAddr())

# @property
# def addr(self): 를 호출
print(p.addr)

p.addr = '부산'
print(p.addr)

# 삭제 작업을 하고 싶으면
# def __del__(): 을 사용

# 사원수
# def __init__(): 입사할 때
# def __del__():  퇴사할 때