import random

def get_random_number(start, end):
    return random.randint(start, end)


def get_users_settings():
    global starting, finish
    try:
        starting = int(input('Введите начало диапазона для загаданного числа: '))
        finish = int(input('Введите конец диапазона для загаданного числа: '))
        if starting > finish:
            starting, finish = finish, starting
    except:
        print('Введены неверные данные! Попробуйте снова!')
        get_users_settings()  # рекурсия, запуск программы сама в себя.


def check_the_guees(user_number):
    global PC_number, attempts
    attempts += 1
    if user_number == PC_number:
        print('Ура, вы угадали!')
        print('Вы угадали с', attempts, 'попытки!')
        return True
    elif user_number < PC_number:
        print('Загадываемое число больше!')
        return False
    else:
        print('Загадываемое число меньше!')
        return False


def get_user_number():
    try:
        return int(input('Ваше число: '))
    except:
        print('Введены неверные данные! Попробуйте снова!')
        get_user_number()


starting = 0
finish = 0
attempts = 0  # попытки

# print('Добро пожаловать в игру ,,Угадай число"')
# get_users_settings()
# PC_number = get_random_number(starting, finish)
# is_guessed = False
# while not is_guessed:
#     is_guessed = check_the_guees(get_user_number())
