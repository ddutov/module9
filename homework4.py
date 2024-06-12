def all_variants(text):  # функция-генератор которая возвращает все подпоследовательности принятой строки
    for x in range(len(text)):
        for y in range(x, len(text)):
            yield text[x:y + 1]


a = all_variants(input('Введите текст: '))
for str_ in a:
    print(str_)
