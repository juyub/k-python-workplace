class Car:

    addr = '서울'

    __slots__ = ['name', 'price', 'company']

    def __init__(self, **args):
        if 'name' in args:
            self.name = args['name']
        if 'price' in args:
            self.price = args.get('price')
        if 'company' in args:
            self.company = args['company']
            Car.addr = '부산'

    def info(self):
        print(f'{self.name} \t {self.price}')
        # if self.company is not None:
        #     print(self.company)
        # else:
        #     print()

c1 = Car(name='그렌저', price='4000', company='현대')
c2 = Car(name='모닝', price='2100')

c1.info()
c2.info()

print(c1.addr)
print(c2.addr)
