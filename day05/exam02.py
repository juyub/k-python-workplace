def print_book(title, writer, price):
    print(f'제목 : {title}')
    print(f'글쓴이 : {writer}')
    print(f'가격 : {price}')
    pass

print_book('홍길동전', '허균', 15000)
print_book('허균', '홍길동전', 15000)

# 인자명을 적으면 순서가 달라도 동작함
print_book(title='홍길동전', writer='허균', price=15000)
print_book(price=15000, writer='허균', title='홍길동전')

book = {'title':'홍길동전', 'writer':'허균', 'price':15000}


# key값만 들어감
# def f(a,b,c):
#     f(*[10,20,30])
#
# def g(*args):
#     g(10,20,30)
print(*book)


# print(**book)
#     title='홍길동전', writer='허균', price=15000 이런 형태로 들어감
#     함수가 동작하려면 함수의 변수로 title, writer, price가 필요하게 됨
print_book(**book)

# key값만 들어감
print_book(*book)
