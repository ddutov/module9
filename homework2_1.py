# -*- coding: utf-8 -*-
"""Написать функцию, которая возвращает математические функции деление и умножение в зависимости от переданных аргументов."""


def func_operation(operation):
    if operation == 1:
        def mult(a, b):
            return a * b

        return mult
    elif operation == 2:
        def div(a, b):
            try:
                return a / b
            except ZeroDivisionError:
                print('Делить на 0 нельзя')

        return div


x = int(input('введите: X = '))
y = int(input('введите: Y = '))
oper = int(input('введите 1 для выполнения X*Y или 2 для выполнения X/Y: '))  # аргумент определющий операцию функции
result = func_operation(operation=oper)
print(f'Результат вычисления: {result(x, y)}')
