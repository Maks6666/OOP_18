# Метаклас, який вносить додаткові перевірки/логіку
# до певних методів у всіх класах.

class NewMetaClass(type):
    methods = ["add"]

    def __new__(cls, name, bases, dct):
        for method in cls.methods:
            if method in dct:
                original_method = dct[method]
                def new_method(self, x, y):
                    if y == 0:
                        raise ZeroDivisionError("Y cannot be 0!")
                    return original_method(self, x, y)
                dct[method] = new_method
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=NewMetaClass):
    def divide(self, x, y):
        return x / y

obj = MyClass()
print(obj.divide(3, 1))



