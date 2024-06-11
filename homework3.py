class EvenNumbers:
    """класс-итератор EvenNumbers для перебора чисел из диапазона start – начальное значение (если значение не передано, то 0)
    end – конечное значение (если значение не передано, то 1)"""
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end

    def __iter__(self):
        self.i = self.start - 2
        return self

    def __next__(self):
        self.i += 2  # перебор чётных чисел
        if self.i > self.end:  # проверка достижения конца определённого числового диапазона
            raise StopIteration()
        return self.i


en = EvenNumbers(10, 25)
for i in en:
    print(i)
