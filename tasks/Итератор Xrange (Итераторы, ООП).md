# Итератор Xrange

Реализуйте класс `Xrange`, порождающий итераторы, конструктор которого принимает три аргумента в следующем порядке:

- `start` — целое или вещественное число
- `end` — целое или вещественное число
- `step` — целое или вещественное число, по умолчанию имеет значение 1

Итератор класса `Xrange` должен генерировать последовательность членов арифметической прогрессии от `start` до `end`, включая `start` и не включая `end`, с шагом `step`, а затем возбуждать исключение `StopIteration`.

**Примечание 1.** При сдаче решения создавать объекты итератора `Xrange` не нужно.

Тестовые данные доступны по ссылке - https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.4/Module_10.4.17<br>
Ссылка на задачу на площадке - https://stepik.org/lesson/669733/step/17?unit=667881

## Решение
```
class Xrange:
    def __init__(self, start, end, step=1):
        self.start = start-step
        self.end = end
        self.step = step
        self.value = start
        
    def __iter__(self):
        return self
        
    def __next__(self):
        self.start += self.step
        if self.start >= self.end and self.value < self.end or self.start <= self.end and self.value > self.end:
            raise StopIteration
        return self.start
```