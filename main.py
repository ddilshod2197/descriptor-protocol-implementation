class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Person:
    age = Descriptor("age")

    def __init__(self, age):
        self.age = age


p = Person(30)
print(p.age)  # 30

p.age = 31
print(p.age)  # 31

p.age = "thirty-one"  # TypeError: age must be an integer
try:
    p.age = "thirty-one"
except TypeError as e:
    print(e)  # age must be an integer

del p.age  # KeyError: age
try:
    del p.age
except KeyError as e:
    print(e)  # age
