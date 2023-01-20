# a = 5
# n = 0
#
# while a <= 10:
#     print (n, '==', a)
#     a +=1
#
#     n+=1
# else:
#     print(f'------ a=={a}')

    # message = 'good morning'
    # for m in range (0,10,2):
    #     print(m)
    # else:
    #     print('end')

# ТАБЛИЦА ПИФАГОРА
# i = 1
# n = 1
# while i <10:
#     while n < 10:
#         result = i*n
#         print (result, end = "\t") #tab
#         n+=1
#     i += 1
#     n = 1
#     print ("\n") #probel

# n = 0
    # while n <5:
    #     n +=1
    #     print('n--', n)
    #
    #     if n == 3:
    #         print ('n==',3)
    #         break # прерывание цикла

        # while n < 5:
        #     n +=1
        #     print('n--', n)
        #
        #     if n == 3:
        #         print ('n==',3)
        #         continue # vse chto niqe ne vupolnaetsa
        #
        #     print('item n ==', n)

# ll = [1,4,7,9,2,3,56,87, 'ee', 'good', False, [33,66], {'key_1':'value_1'}]
#
# for i in ll: # объявление переменной i
#
#     if type(i) == list:
#         for nn in i: # объявление переменной nn
#             print(nn)

    # for i in ll:
    #     if i == 'good':
    #         print('good in list')
    #         break
    #     print(i)

# print('good' in ll)
#
# if 'good' in ll:
#     print(True)

import names
for i in range(0,100):
    name = names.get_full_name(gender='male') # male, если все то убрать в скобках
    print(i, '--', name)