def say_hello(name, surname):  # (name, surname) - параметры
    print('Hello')
    print(name)
    print(surname)
    print('!')


# say_hello('Ivan', 'Ivanov')  # ('Ivan', 'Ivanov') - аргументы
# say_hello('Tom', 'Soyer')
# say_hello('Piter', 'parker')
# say_hello('Mark', 'Symen')

def get_area(a, b):
    print('Площадь комнаты равна', a * b)


# get_area(int(input('Введите длину комнаты: ')), int(input('Введите ширину комнаты: ')))

def multiplication(nam1, nam2):
    return nam1 * nam2


# print(multiplication(4, 6))


def is_even(num):
    return num % 2 == 0


# a = int(input('Введите число: '))
# b = is_even(a)
# print(b)

def capitalize(str):
    return str.upper()


# print(capitalize('hello world'))

def get_season_name(month_number):
    if month_number in [12, 1, 2]:
        result = 'Зима'
    elif month_number in range(3, 6):
        result = 'Весна'
    elif month_number in [6, 7, 8]:
        result = 'Лето'
    elif month_number in [9, 10, 11]:
        result = 'Осень'
    else:
        result = 'Ошибка'
    return result


# print(get_season_name(25))

def sun_range(start, end):
    sum = 0
    if start < end:
        for num in range(start, end + 1):
            sum += num

    elif start > end:
        for num in range(end, start + 1):
            sum += num

    return sum


# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
#
# print(sun_range(a, b))

# или

def sum_range(start, end):
    sum = 0
    if start > end:
        start, end = end, start

    for num in range(start, end + 1):
        sum += num

    return sum


# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
#
# print(sum_range(a, b))
