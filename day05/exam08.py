class Parent:
    def __init__(self):
        self.name = '부모'
        print('Parent() 호출')
    def info(self):
        print('Parent info() 호출...')

class Child(Parent):
    def __init__(self):
        # 파이썬은 상속을 해도 자동으로 객체를 생성하지는 않음
        super().__init__()
        print('Child 호출')

    def info(self):
        super().info()
        print('Child info() 호출...')

# p = Parent()
p = Child()
p.info()

# 파이썬은 상속을 해도 자동으로 객체를 생성하지는 않음
# super().__init__() 없으면 에러 발생
print(p.name)


