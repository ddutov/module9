# -*- coding: utf-8 -*-
"""Применить функции map и filter к списку так, чтобы в конечном списке оставить нечётные квадраты чисел"""


def square(x):
    return x ** 2


def odd_num(x):
    return x % 2


my_list = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
result = map(square, filter(odd_num, my_list))
print(result)
print(list(result))
print(result)
print(list(result))
