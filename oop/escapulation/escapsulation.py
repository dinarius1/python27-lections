class A:
    attr1 = 'public'
    _attr2 = "protected"
    __attr3 = 'private'

print(A.attr1)
print(A._attr2)
# print(A.__attr3)
# public
# protected
# AttributeError: type object 'A' has no attribute '__attr3'. Did you mean: '_A__attr3'?
print(A._A__attr3)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def get_age(self):
        return  self.__age
    
    def set_age(self, new_age):
        if new_age > 0 and new_age < 120:
            self.__age = new_age
        else:
            raise Exception('Invalid age')

obj = Person('Nasty', 12)
print(obj.name)
print(obj.get_age()) #через метод можно вытащить приватный атрибут
# Nasty
# 12
obj.set_age(45)
print(obj.get_age())
# 45
# obj.set_age(125)
# print(obj.get_age())
# Exception: Invalid age - так как возраст больше 120

class A:
    @property #делает какой то метод в атрибут-свойстве.
    # вот так выглядит наш код:?? - obj.hello() = property(obj.hello())
    def hello(self):
        return 5
    
    #property.setter - работает когла мы пишем obj.attr = ...
    #setter -устанваливает новое значение атрибута, который до этого явл методом 
    @hello.setter
    def hello(self, new_value):  #new_value - параметр, который вбирает в себе новое значение при вызове атрибута obj.hello. new_value = 'new value'
        print('setter')

    # property.deleter работает когда мы пишем del obj.attr
    @hello.deleter
    def hello(self):
        print("deleter")
#ДОПИСАТЬ ИЗ ГИТА


obj = A()
# print(obj.hello)
obj.hello = 'new value'  #отрабатывается декоратор setter, так как мы передали новое значение у атрибута obj.hello


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        if new_age > 0 and new_age < 120:
            self.__age = new_age
        else:
            raise Exception("Invalid age")
    
    @age.deleter
    def age(self):
        if self.__age < 100:
            raise Exception("Cannot delete age")
        del self.__age

obj = Person('Ann', 12)
print(obj.age)
obj.age = 34
del obj.age  #Exception: Cannot delete age, так как obj.age меньше 100
print(obj.age)
# obj.age = 115

