# -*- coding: utf-8 -*-
"""Создать класс c полями a, b которые задаются в __init__ и методом __call__, который возвращает площадь прямоугольника, то есть a*b."""


class Square:
    def __init__(self, a):
        self.a = a

    def __call__(self, b):
        return self.a * b


print('Расет площади прямоугольника')
x = int(input('Введите длину стороны 1: X = '))
y = int(input('Введите длину стороны 2: Y = '))
rectangle = Square(x)
print(f'Площадь прямоугольника: {rectangle(y)}')
