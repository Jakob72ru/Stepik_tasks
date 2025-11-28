# Классы Lecture и Conference 

Реализуйте класс ```Lecture```, описывающий некоторое выступление. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

- ```topic``` — тема выступления
- ```start_time``` — время начала выступления в виде строки в формате ```HH:MM```
- ```duration``` — длительность выступления в виде строки в формате ```HH:MM```

Также реализуйте класс ```Conference```, описывающий конференцию, протяженностью в один день. Конференция представляет собой набор последовательных выступлений. При создании экземпляра класс не должен принимать никаких аргументов.

Класс ```Conference``` должен иметь четыре метода экземпляра:

- ```add()``` — метод, принимающий в качестве аргумента выступление и добавляющий его в конференцию. Если выступление пересекается по времени с другими выступлениями, должно быть возбуждено исключение ```ValueError``` с текстом:

```Провести выступление в это время невозможно```

- ```total()``` — метод, возвращающий суммарную длительность всех выступлений в конференции в виде строки в формате ```HH:MM```
- ```longest_lecture()``` — метод, возвращающий длительность самого долгого выступления в конференции в виде строки в формате ```HH:MM```
- ```longest_break()``` — метод, возвращающий длительность самого долгого перерыва между выступлениями в конференции в виде строки в формате ```HH:MM```

**Примечание 1.** Перерыв между выступлениями может быть нулевым. Другими словами, одно выступление может заканчиваться, например, в 12:00, а другое начинаться в 12:00.

**Примечание 2.** Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.

**Примечание 3.** Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.

Тестовые данные доступны по ссылке - https://github.com/python-generation/OOP/tree/main/Module_7/Module_7.8/Module_7.8.13/

Ссылка на задачу на площадке - https://stepik.org/lesson/804638/step/13?unit=807762

## Решение
```
from datetime import time
from itertools import pairwise

class Lecture:
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = time(*(int(i) for i in start_time.split(':')))
        self.duration = time(*(int(i) for i in duration.split(':')))
        self.end_time = time(self.start_time.hour + self.duration.hour + (self.start_time.minute + self.duration.minute)//60, (self.start_time.minute + self.duration.minute)%60)
    
    def get_time_range(self):
        time_range = range(*(i.hour * 60 + i.minute for i in (self.start_time, self.end_time)))
        return time_range
    


class Conference:
    def __init__(self):
        self.d = {}
        
    def add(self,lecture):
        if all(len(set(lecture.get_time_range()) & set(i.get_time_range())) == 0 for i in self.d.values()):
            self.d[lecture.topic] = lecture
        else:
            raise ValueError('Провести выступление в это время невозможно')
            
    def total(self):
        res = sum(i.duration.hour * 60 + i.duration.minute for i in self.d.values())
        return f'{res//60:02d}:{res%60:02d}'
        
    def longest_lecture(self):
        res = max((i.duration.hour * 60 + i.duration.minute) for i in self.d.values())
        return f'{res//60:02d}:{res%60:02d}'
        
    def longest_break(self):
        l = list(pairwise([i.get_time_range() for i in sorted(self.d.values(), key=lambda x: x.start_time)]))
        if l:
            res = max(min(b) - max(a) for a, b in l) - 1
            return f'{res//60:02d}:{res%60:02d}'
        return '00:00'
```    
       


