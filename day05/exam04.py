# print(type(10), type(12.34), type(True), type('hello'))

class Dog:
    pass

# data = list() tupule()
dog = Dog()
print(type(dog))

class Car:

    # 생성자
    # def __init__():
    #     pass

    # self는 'this'의 개념
    # 정보들을 self로 안다
    # self를 쓰고 그 다음에 인자들은 쓴다
    def drive(self):
        print('운전을 합니다')

c = Car()
c.drive()

# isinstanceof(10, int)
# isinstanceof('111', str)

print(f'type(Car) 판단 : {isinstance(c, Car)}')
print(f'type(Car) 판단 : {isinstance(10, Car)}')
print(f'type(Car) 판단 : {isinstance([10,20,30], Car)}')


l = [10,20,30]
print(l[0], l.__getitem__(0))
