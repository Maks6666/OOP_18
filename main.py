# Створіть метаклас, який автоматично додає певні
# атрибути до всіх класів, що використовують його.

class NewMetaClass(type):
    def __new__(cls, name, bases, dct):
        dct['new_attribute'] = "New attribute"
        print(dct)
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=NewMetaClass):
    pass

obj = MyClass()
print(obj.new_attribute)



