print('#2. Добавить слово в конец списка так, чтобы каждая буква стала отдельным элементом списка')
l2 = [1, 2, 3]
a2 = 'abc'
print('решение 1') # выводить отдельно каждое решение
l2.extend(a2)
print(l2, '\n')

# print('решение 2')
# for i in a:
#     l.append(i)
# print(l, '\n')
#
# print('решение 3')
# l += a
# print(l, '\n')

print('#3. Все чётные числа вывести в другой список')
l3 = [1,3,4,5,8,9,10,44,22,50,79,54,28,91]
k3 = []
for i in l3:
    if i % 2 ==0:
        k3.append(i)
print(k3, '\n')

print('#4. Все emails у которых есть слово test вывести в другой список')
l4 = ['webtest1@gmail.com',
     'alex_dr5@gmail.com',
     'elena_viktorovna@gmail.com',
     'infotest@gmail.com',
     'sigmatesst@gmail.com',
     'planet.dollsatest@gmail.com',
     'loadtestsinfo@gmail.com',
     'straightwaytest@gmail.com',
     'test.of.tests@gmail.com',
     'bigmac@gmail.com',
     'bigmactest@gmail.com',
     'kfc_test_supply@gmail.com',
     'cyberdesk@gmail.com',
     'supportonlinetest@gmail.com'
     ]
k4 = []
for i in l4:
    if 'test' in i:
        k4.append(i)
print(k4)
print(l4, '\n')


print('#5 найти самое маленькое число в списке')
l = [3,0,4,5,8,9,10,44,22,50,-1,79,54,-28,91]
a = 1000
for i in l:         # через for
    if i < a:
        a = i
print('решение через цикл: ', a)
print('решение 2: ', min(l), '\n') #решение в одной строке


print('#6. Сравнить 2 строки без учёта регистра')
s_1 = 'AlekSaNdR'
s_2 = 'aleksAndr'
print(s_1 == s_2) # строгое равенство строк с учетом регистра
print(s_1.lower() == s_2.lower(), '\n') #сравнение строк в нижний регистр lower / верхний Upper

print('#7. Проверить является ли массив подмножеством другого массива')
l71 = [1,4,6]
l72 = [9,5,1,10,4,33,2,6,0,8]
l721 = len(l72)
с = 0
for i in l71:
    if i in l72:
        с += 1
if с == len(l71):
    print('l1 входит в l2', '\n')
else:
    print('l1 НЕ входит в l2', '\n')

print('#8. Напишите функцию, которая принимает строку и возвращает количество букв английского алфавита, '
      'которые встречаются больше чем 1 раз.')
#'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
s8 = 'asdsdwwerta'
abc = 'qwertyuiopasdfghjklzxcvbnm'
for i in abc:
    count = 0
    for j in s8:
        if j == i:
            count += 1
    if count != 0:
        print(i,'встречается', count, 'раз')
print('\n')

print('9. Напишите функцию, которая принимает строки.')
# Она должна вернуть False, если в строке содержится две одинаковые буквы,
# а если таких слов нет — True.

# no_duplicate_letters("Здравствуйте, Александра") ➞ False
# Две в в «Здравствуйте», три a в «Александра».

# no_duplicate_letters("Всегда дожимай до конца") ➞ True
# Две в в «Здравствуйте», три a в «Александра».

def digit_to_word(digit):
    if digit > 7:
        return 'Многабукаф'
    words_dict = {
        1: 'Одна буква',
        2: 'Две буквы',
        # 3: 'Три буквы',
        # 4: 'Четыре буквы',
        # 5: 'Пять букв',
        # 6: 'Шесть букв',
        # 7: 'Семь букв',
    }
    return words_dict[digit]

def no_duplicate_letters(string):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result = {}
    words = string.split(' ')
    without_duplicates = True

    for word in words:
        result[word] = {}
        for i in alphabet:
            if word.lower().count(i) > 1:
                result[word][i] = word.lower().count(i)
                # print(result)
    for result_key, result_value in result.items():
        if result_value:
            for letter, count in result_value.items():
                print(f'{digit_to_word(count)} "{letter}" в "{result_key}"')
            without_duplicates = False

    return without_duplicates

print(no_duplicate_letters('Здравствуйте, Александра'), '\n')
print(no_duplicate_letters('Обороноспособность'), '\n')
print(no_duplicate_letters('Всегда дожимай до конца'), '\n')

# =============================

print('10. Напишите функцию, которая проверяет сложность пароля. Функция проверяет ряд условий и оценивает сложность пароля. За каждое выполненое условие пароль получает бал.')

# Если выполняется одно условие - функция возвращает 1, если выполненяется 5 условий - функция вернет 5.
#
# Условия которые нужно проверить:
#
# длина пароля не меньше 6 символов,
# пароль содержит хотя бы 1 цифру,
# пароль содержит хотя бы одну заглавную букву,
# пароль содержит хотя бы одну строчную букву,
# пароль содержит хотя бы один из специальных символов: !@#$%^&*()-+
#
# Типы символов, которые будут содержаться в пароле во время тестирования:

# numbers = "0123456789"
# lower_case = "abcdefghijklmnopqrstuvwxyz"
# upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# special_characters = "!@#$%^&*()-+"

# Пароль не должен содержать кириллических символов