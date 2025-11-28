# Класс MultiKeyDict

Реализуйте класс `MultiKeyDict`, который практически во всем повторяет класс `dict`. Создание экземпляра класса `MultiKeyDict` должно происходить аналогично созданию экземпляра класса `dict`:

```
multikeydict1 = MultiKeyDict(x=1, y=2, z=3)
multikeydict2 = MultiKeyDict([('x', 1), ('y', 2), ('z', 3)])

print(multikeydict1['x'])        # 1
print(multikeydict2['z'])        # 3
```

                  
Особенностью класса `MultiKeyDict` должен являться метод `alias()`, который должен позволять давать имеющимся ключам псевдонимы. Обращение по созданному псевдониму не должно ничем отличаться от обращения по оригинальному ключу, то есть с момента создания псевдонима у значения становится два ключа (или больше, если псевдонимов несколько):

```
multikeydict = MultiKeyDict(x=100, y=[10, 20])

multikeydict.alias('x', 'z')     # добавление ключу 'x' псевдонима 'z'
multikeydict.alias('x', 't')     # добавление ключу 'x' псевдонима 't'
print(multikeydict['z'])         # 100
multikeydict['t'] += 1
print(multikeydict['x'])         # 101

multikeydict.alias('y', 'z')     # теперь 'z' становится псевдонимом ключа 'y'
multikeydict['z'] += [30]
print(multikeydict['y'])         # [10, 20, 30]
```
                  
Значение должно оставаться доступным по псевдониму даже в том случае, если оригинальный ключ был удален:

```
multikeydict = MultiKeyDict(x=100)

multikeydict.alias('x', 'z')
del multikeydict['x']
print(multikeydict['z'])         # 100
```
                  
Ключи должны иметь приоритет над псевдонимами. Если некоторые ключ и псевдоним совпадают, то все операции при обращении к ним должны выполняться именно с ключом:

```
multikeydict = MultiKeyDict(x=100, y=[10, 20])

multikeydict.alias('x', 'y')
print(multikeydict['y'])         # [10, 20]
```
                  
**Примечание 1.** Гарантируется, что все ключи имеют строковый тип данных.

**Примечание 2.** Псевдонимы не должны влиять на длину словаря. Например, если ключ имеет один или несколько псевдонимов, то длина словаря не должна увеличиваться на количество псевдонимов. При удалении ключа, имеющего псевдонимы, длина словаря должна уменьшиться на единицу.

Тестовые данные доступны по ссылке - https://github.com/python-generation/OOP/tree/main/Module_9/Module_9.1/Module_9.1.13<br>
Ссылка на задачу на площадке - https://stepik.org/lesson/864077/step/13?unit=923013

## Решение
```
from collections import UserDict

class MultiKeyDict(UserDict):
    def __init__(self, *args, **kwargs):
        self.alt = {}
        super().__init__(*args, **kwargs)

    def __getitem__(self, key):
        if key not in self.data:
            return self.data[self.alt[key]]
        return self.data[key]

    def __setitem__(self, key, value):
        if key in self.alt:
            self.data[self.alt[key]] = value
        else:
            self.data[key] = value

    def __delitem__(self, key):
        new_key = None
        value = self.data[key]
        for i in self.alt:
            if self.alt[i] == key:
                new_key = i
                self.data[new_key] = value
                break
        del self.data[key]
        if new_key:
            del self.alt[new_key]
        for i in self.alt:
            if self.alt[i] == key:
                self.alt[i] = new_key

    def alias(self, key, alias):
        self.alt[alias] = key

    def __str__(self):
        return f'{self.data}'
```