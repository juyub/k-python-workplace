def print_book_info(**args):
    # print({k:y for k, y in args.items()})
    for k, y in args.items():
        print(f'{k}:{y}')
    print('=' * 20)

print_book_info(title='홍길동전', writer='허균', price=15000)
print_book_info(title='홍길동전', writer='허균')
print_book_info(title='홍길동전')
print_book_info(title='홍길동전', price=15000)

book = {'title':'홍길동전', 'writer':'허균', 'price':15000}
print_book_info(**book)