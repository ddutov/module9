# -*- coding: utf-8 -*-

def square(x):
    return x ** 2


def odd_num(x):
    return x % 2


my_list = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
result = map(square, filter(odd_num, my_list))
print(list(result))
