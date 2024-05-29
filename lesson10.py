# цикл for - переводится как 'для'
# str = 'Hello world'
#
# for letter in str:
#     if letter == 'o':
#         print(letter)

# ---------------------------------------------------------

# можно перебирать элементы списка

# animals = ['cat', 'dog', 'fish', 'cow', ['horse', 'donkey']]
#
# for i in animals:
#     print(a)

# -------------------------------------------------------------------

# list = [7, 7, -4, 2.5, -0.9, 0]
# num_minus = 0
#
# for minus in list:
#     if minus < 0:
#         num_minus +=1
# print(num_minus)

# ------------------------------------------------------------------

# list = ['три', '', 'конь', 'свет', '']
# new_list = []
#
# for slovo in list:
#     if slovo != '':
#         new_list.append(slovo)
# print(new_list)

# --------------------------------------------------------------

# функция range
# # с 1 аргументом
#
# for a in range(5):
#     print(a)

# с 2 аргументами

# for a in range(1, 11):
#     print(a)

# или

# for a in range(1, 10 + 1):
#     print(a)

# с 3 аргументами

# for a in range(1, 11, 2):
#     print(a)

# или

# for a in range(11, 1, -2):
#     print(a)

# или

# for a in range(10, 1, -1):
#     print(a)

# --------------------------------------------------------------

# num = int(input('Введите целое число больше 10: '))
#
# for num in range(5, num + 1):
#     print(num)
#
# print('')
#
# for num in range(num, 5 - 1, -1):
#     print(num)

# ----------------------------------------------------------

# list = [1, 2, 3, 1, 2]
# check = []
#
# # check.append(list[0])
#
# for num in list:
#     if num not in check:
#         check.append(num)
#
# print(check)
