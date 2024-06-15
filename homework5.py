import sympy


def is_prime(func):  # декоратор распечатывает "Простое", если результат функции sum_three будет простым числом и "Составное" в противном случае.
    def wrapper(*args):
        x = func(*args)
        while sympy.isprime(x):  # проверка что число простое или нет
            return f'\033[32mПростое - {x}\033[0m'
        return f'\033[33mСоставное - {x}\033[0m'
    return wrapper


@is_prime
def sum_three(*args):  # Функция, которая складывает передаваемые ей числоввые аргументы
    s = 0
    for i in range(0, len(args)):
        s += args[i]
    return s


while True:
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        c = int(input('Введите третье число: '))
        print('Проверяем является ли сумма введенных чисел простым числом.')
        result = sum_three(a, b, c)
        print(result)
    except ValueError:
        print('\033[31m Кажется Вы ввели не число!!! Повторите попытку.\033[0m')
