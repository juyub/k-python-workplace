'''
    setdefault      새 데이터 삽입
    update          key 없으면 데이터 삽입, key 있으면 데이터 수정
    pop             데이터 삭제
    clear           전부 삭제
'''

members = {'홍길동':'010-1111-2222', '박길동':'010-3333-4444'}
print(members)
members.setdefault('윤길동','010-5555-6666')
members.setdefault('이길동')
print(members)
# members.setdefault('이길동', '010=7777=8888') # 새데이터 삽입 o 수정 안 됨
members.update(이길동 = '010-7777-8888')   # '='형태일 때는 key가 문자열만 가능
members.update(한길동 = '010-9999-0000')
members.update({2023082501:'010-2345-6789'})     # 딕셔너리 형태
members.update([[2023082502, '010-1234-5678'],['고길동', '010-4566-2345']])
members.update(zip(['park', '이길동'],['8282', None]))
print(members)

value = members.pop('이길동')
print(f'pop("이길동") : {value}')
value = members.pop('구길동', "없음")  # pop은 해당하는 key가 없으면 예외가 발생
print(f'pop("구길동") : {value}')
print(members)

members.popitem()
print(members)

value = members.get('홍길동')
print(f'홍길동 : {value}')
print(f'이길동 : {members.get("이길동", "존재하지 않음")}')