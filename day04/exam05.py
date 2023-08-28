# quit가 나올때까지 문자열을 입력방아 test02.txt 저장
# text02.text에 저장된 모든 문자열 읽어서 모니터에 출력

'''
with open('text2.txt', 'w') as file:
    print('문자열들을 입력하세요. quit 입력시 종료')
    while True:
        msg = input()
        if msg == 'quit':
            break
        file.write(f'{msg}\n')
        # file.write('{0}\n'.format(msg)) # 데이터가 하나일 때는 '0'도 생략할 수도 있음
        # file.write('{1}:{0}\n'.format(msg, "aaa")) # 응용

print('파일 저장 완료...')
'''


# print('< 읽어온 데이터 >')
# with open('text2.txt', 'r') as file:
#     lines = file.readlines()
#
# print(lines)

# hello\n|안녕하세요\n|bye\n   개행까지 문자열에 포함되어 있음

# print('<읽어온 데이터 출력>')
# for line in lines:
#     print(line.rstrip('\n'))
# print()


# with open('text2.txt', 'r') as file:
#     for line in file:
#         print(line.rstrip('\n'))
#         input()



