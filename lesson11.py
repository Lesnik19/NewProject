# Вложенные циклы

# for a in range(5):
#     print(a + 1, '*')

# stars = ''
#
# for zvezda in range(5):
#     stars += '*'
#     print(stars)
# print(stars)

# for a in range(5):
#     print('*', end='')

# ---------------------------------------------------------------------

# Вывести квадрат из звёздочек с периметром 5

# for a in range(5):
#     for x in range(5):
#         print('*', end='')
#     print()

# ------------------------------------------------------------------

# for a in range(6):
#     for x in range(a):
#         print('*', end='')
#     print()
#
# for a in range(6):
#     for x in range(a):
#         print(a, end='')
#     print()

# -------------------------------------------------------------------

# for a in range(7):
#     for x in range(a):
#         print('* ', end='')
#     print()
#
# for a in range(6):
#     for x in range(x):
#         print('* ', end='')
#     print()

# ---------------------------------------------------

# Операторы циклов
# braek

# for letter in 'Hello, world!':
#     if letter == ',':
#         break
#     print(letter)

# a = 0
#
# while True:
#     if a > 11:
#         break
#     print('Мяу')
#     a += 1

# my_list = []
#
# while True:
#     element = input('Введите строку: ')
#     if element == 'выход':
#         break
#     my_list.append(element)

# continue - переход к следующей итерации

# my_list = [1, 2, 3, 4, 5, 6, 7]
#
# for element in my_list:
#     if element % 2 != 0:
#         continue
#     print(element)

# ---------------------------------------------------

# sum = 0
#
# for num in range(5, 58):
#     if num == 34 or num == 46 or num == 52:
#         continue
#
#     sum += num
#
# print(sum)

# ----------------------------------------------------

# Вывести ромб со стороной 7

# side_rhombus = 7
#
# for i in range(side_rhombus + 1):
#     print('  ' * ((side_rhombus + 1 - a) - 1), '* ' * a + ('* ' * (a - 1)))
#
# for a in range(side_rhombus - 1, 0, -1):
#     print('  ' * ((side_rhombus + 1 - a) - 1), '* ' * a + ('* ' * (a - 1)))

# Вариант с выбором длины стороны ромба

# side_rhombus = int(input('Введите длину стороны ромба: '))
#
# for a in range(side_rhombus + 1):
#     print('  ' * ((side_rhombus + 1 - a) - 1), '* ' * a + ('* ' * (a - 1)))
#
# for i in range(side_rhombus - 1, 0, -1):
#     print('  ' * ((side_rhombus + 1 - a) - 1), '* ' * a + ('* ' * (a - 1)))

# ---------------------------------------------------------------

# Вариант с выбором длины стороны ромба + распознавание ошибки

# side_rhombus = int(input('Введите длину стороны ромба: '))
#
# if side_rhombus > 0:
#     for a in range(side_rhombus + 1):
#         print('  ' * ((side_rhombus + 1 - a) - 1), '* ' * a + ('* ' * (a - 1)))
#
#     for a in range(side_rhombus - 1, 0, -1):
#         print('  ' * ((side_rhombus + 1 - a) - 1), '* ' * a + ('* ' * (a - 1)))
#
# else:
#     print('ОШИБКА, СТОРОНА МОЖЕТ БЫТЬ ТОЛЬКО ПОЛОЖИТЕЛНОЙ ЦИФРОЙ!')
