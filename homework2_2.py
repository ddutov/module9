# -*- coding: utf-8 -*-
# bспользовать лямбда-функцию для реализации простой операции и написать такую же функцию с использованием def. Например, возведение числа в квадрат
square = lambda x: x ** 2
print(f"X**2 = {square(int(input('Введите X: ')))}")


def square_2(a):
    return a ** 2


print(f"Y**2 = {square_2(int(input('Введите Y: ')))}")
