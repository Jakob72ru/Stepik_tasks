from copy import copy

class FieldTracker:
    fields = ()
    counter = 0
    def __init__(self, *args, **kwargs):
        self.attrs = copy(self.__dict__)

    def __setattr__(self, attr, value):
        self.__dict__[attr] = value

        if self.__class__.counter >= len(self.__class__.fields):
            if attr not in self.attrs:
                self.attrs[attr] = value
        self.__class__.counter += 1

    def base(self, attrname):
        return self.attrs[attrname]

    def has_changed(self, attrname):
        return self.__dict__[attrname] != self.attrs[attrname]

    def changed(self):
        d = {key: value for key, value in self.attrs.items() if self.has_changed(key)}
        return d

    def save(self):
        self.attrs = copy(self.__dict__)
        del self.attrs['attrs']