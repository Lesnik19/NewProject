# my_string = 'Крепитесь, люди, скоро лето!'

# Методы по работе со строками
# new_string = my_string.upper()  # преобразование строки к ВЕРХНЕМУ РЕГИСТРУ
# new_string = my_string.lower()  # преобразование строки к нижнему регистру
# print(new_string)

# my_string = 'Крепитесь, ЛЮДИ, скоро лето!'
# index = my_string.find('ЛЮДИ')  # получение индекса найденной подстроки - 11
# index = my_string.find('люди')  # получение индекса найденной подстроки - -1 (не найдено такой подстроки)
# print(index)

# new_string = my_string.replace(' ', '_')  # замена символа (или нескольких) на другой
# new_string = my_string.replace(' ', '*')  # замена символа (или нескольких) на другой
# new_string = my_string.replace(', ', '?')  # замена символа (или нескольких) на другой
# print(new_string)

# check = my_string.count(',')  # поиск символа (или нескольких) - выдаёт их кол-во
# print(check)

# -----------------------------------------------------------------------

# str = input('Введите первую строку:')
# str2 = input('Введите вторую строку:')
#
# str = str.upper()
# str2 = str2.upper()
#
# check = str.count(str2)
#
# if check > 0:
#     print('Вот это да!')
# else:
#     print('Нет совпадений')

# или

# str = input('Введите первую строку:').upper()
# str2 = input('Введите вторую строку:').upper()
#
# if str2 in str:
#     print('Вот это да!')
# else:
#     print('Нет совпадений')

# --------------------------------------------------------------------------

# space = input('Введите предложение: ').count(' ')
#
# words = space + 1
#
# print(words)

# или

# space = input('Введите предложение: ').count(' ')
#
# print(space + 1)

# ---------------------------------------------------------------------------------

# работа со списками

# animals = ['кот', 'собака', 'рыбка', 'лошадь']
# num = [5, 9, 6, 85, [-43, 152]]
#
# print(animals[0])
# print(animals[-2])
# print(animals[2:4])
# print(animals[0:])
# num[4][1] = 356
# print(num[4][1])

# ----------------------------------------------------------

# num = [1, 2, 3, 4, 5]
#
# print('Первый элемент списка: ', num[0])
# print('Третий элемент списка: ', num[2])
# print('Срез из первых трёх элементов списка: ', num[0:3])
#
# # или
#
# print('Первый элемент списка: ', num[-5])
# print('Третий элемент списка: ', num[-3])
# print('Срез из первых трёх элементов списка: ', num[-5:-2])

# --------------------------------------------------------------------

# num = [1, 2, 3, 4]
#
# print(num[3], num[1], num[2], num[0])
#
# # или
#
# animals = ['cat', 'dog', 'fish', 'cow']
# first_element = animals[0]
# last_element = animals[-1]
# animals[0] = last_element
# animals[-1] = first_element
# print(animals)

# a,b=b,a