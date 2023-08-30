class TV:
    def __init__(self):
        # print('초기화 진행')
        self.power = False
        self.channel = 10
# 객체가 생성될 때 생성자는 생성되지 않음
# 생성자는 공유영역에 생성됨
# (메서드는 변하는 것이 아니므로 공유영역에 한번 저장하면 되므로)
# 공유영역에서 this를 이용하여 객체를 불러 옴
# 파이썬에선 self가 this의 역활을 수행함
    def info(self):
        print(f'채널정보 : {self.channel}')
        if 'volume' in self.__dict__:
            print(f'음량정보 : {self.volume}')


tv = TV()

# self가 멤버변수 역활도 수행함
# 지역변수뿐만 아닌
# 함수를 가지는 클래스에서도 사용할 수 있음
# self.power = False
print(tv.power)

# if 'volume' in self.__dict__:
#     print(f'음량정보 : {self.volume}')
# 조건문이 있어서 예러 안남
# 조건문이 없으면 volume이 아직 없어서 에러 남
tv.info()

# 그냥 하면 에러나지만
# print(tv.volume)

# self를 쓰면 좀더 표준적으로 쓸 수 있고
# 그냥 쓰면 특정 경우에만 쓸 수 있음
tv.volume = 20

print(tv.volume)
tv.info()

class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        print(f'자동차명 : {self.name}\t가격 : {self.price}')
        
c1 = Car('그렌저', 4000)
c2 = Car('모닝', 2100)
c1.info()
c2.info()