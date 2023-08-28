print('< 읽어온 데이터 >')
# 방법1
# with open('text2.txt', 'r') as file:
#     while True:
#         line = file.readline()
#         if line == '':
#             break
#         print('[{}]'.format(line.rstrip("\n")))


    # line = file.readline()
    # print('[{}]'.format(line.rstrip("\n")))
    #
    # line = file.readline()
    # print('[{}]'.format(line.rstrip("\n")))
    #
    # line = file.readline()
    # print('[{}]'.format(line.rstrip("\n")))

#  방법2
with open('text2.txt', 'r') as file:

    for line in file:
        print(line.rstrip('\n'))

    # line = file.readline().rstrip('\n')
    # while line != '':
    #     print(line)
    #     line = file.readline().rstrip('\n')

    # while (line = file.readline()) != '':
    #     print(line)

    # while (line = file.readline() and line != ''):