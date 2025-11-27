# Декоратор @limiter

Реализуйте декоратор `@limiter` для декорирования класса, с помощью которого можно ограничивать количество создаваемых декорируемым классом экземпляров до определенного числа. Декоратор должен принимать три аргумента в следующем порядке:

`limit` — количество экземпляров, которое может создать декорируемый класс

`unique` — имя атрибута экземпляра декорируемого класса, значение которого является его идентификатором. Два экземпляра с одинаковыми идентификаторами существовать не могут. Если происходит попытка создать экземпляр, идентификатор которого совпадает с идентификатором одного из ранее созданных экземпляров, должен быть возвращен этот ранее созданный экземпляр

`lookup` — определяет, какой объект должен быть возвращен, если превышено ограничение limit, а значение атрибута unique ранее не использовалось. При значении FIRST возвращается самый первый созданный экземпляр, при значении LAST — самый последний созданный экземпляр

**Примечание 1.** Гарантируется, что экземпляры декорируемого класса всегда имеют атрибут, который содержит их
идентификатор.

```from functools import wraps

def limiter(limit, unique, lookup):
    def decorator(cls):
        old_init = cls.__init__
        old_new = cls.__new__
        cls.counter = 0
        cls.selfies = {}

        @wraps(old_init)
        def new_init(self, *args, **kwargs):
            if cls.counter <= limit:
                if self not in cls.selfies.values():
                    old_init(self, *args, **kwargs)
                    cls.selfies[self.__dict__[unique]] = self
                    cls.counter += 1
            else:
                pass
        cls.__init__ = new_init

        @wraps(old_new)
        def new_new(cls, *args, **kwargs):
            if args[0] in cls.selfies:
                return cls.selfies[args[0]]
            if args[1] in cls.selfies:
                return cls.selfies[args[1]]
            if cls.counter >= limit:
                if lookup == 'FIRST':
                    return cls.selfies[list(cls.selfies.keys())[0]]
                elif lookup == 'LAST':
                    return cls.selfies[list(cls.selfies.keys())[-1]]
            instance = object.__new__(cls)
            return instance

        cls.__new__ = new_new
        return cls
    return decorator
```