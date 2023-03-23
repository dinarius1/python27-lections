'''
1 task
'''
class A:
    def public(self):
        return 'Public method'

    def _protected(self):
        return 'Protected method'

    def __private(self):
        return 'Private method'

obj1 = A()
print(obj1.public())
print(obj1._protected())
print(obj1._A__private())

'''
Задание 2

Определите класс A, в нём объявите метод method1, который печатает строку "Hello World".

Затем, создайте класс B, который будет наследоваться от класса A.

Создайте экземпляр в переменной b1 от класса B, и через него вызовите метод method1.
'''
class A:
    def method1(self):
        print("Hello World")
class B(A):
    pass

b1 = B()
b1.method1()

'''
Задание 3

Объявите класс Car, в котором будет приватный атрибут экземпляра класса speed.

Затем, определите метод set_speed, который будет устанавливать значение скорости и метод show_speed, который возвращает значение скорости.

Создайте экземпляр в переменной car1 класса Car и вызовите все методы.

Ввод:

car1 = Car() 
print(car1.show_speed()) 
car1.set_speed(20) 
print(car1.show_speed()) 

Вывод:

0 
20 
'''
class Car:
    def __init__(self, speed):
        self.__speed = speed
    def set_speed(self, new_speed):
        self.__speed = new_speed
    def show_speed(self):
        return self.__speed
car1 = Car(0) 
print(car1.show_speed()) 
car1.set_speed(20) 
print(car1.show_speed()) 
