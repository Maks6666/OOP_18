# Метаклас, що може змінювати ім'я класу залежно
# від певних умов або параметрів.

class NameMetaClass(type):
    def __new__(cls, name, bases, dct):
        if 'original_name' in dct:
            name = dct['original_name']
            print(dct)
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=NameMetaClass):
    ...

print(MyClass.__name__)

class NewClass(metaclass=NameMetaClass):
    original_name = "New_Class"

print(NewClass.__name__)




