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
    def __init__(self):
        self.__speed = 0
    def set_speed(self, new_speed):
        self.__speed = new_speed
    def show_speed(self):
        return self.__speed
car1 = Car() 
print(car1.show_speed()) 
car1.set_speed(20) 
print(car1.show_speed()) 

'''
Задание 4

Перепишите класс Car из предыдущего задания.

Перепишите метод set_speed() с использование декоратора @speed.setter, а метод show_speed() с использованием декоратора @property.

Создайте обьект car1 класса Car.

Ввод:

car1 = Car() 
print(car1.speed) 
car1.speed = 20 
print(car1.speed) 

Вывод:

0 
20 
'''
class Car:
    def __init__(self):
        self.__speed = 0
    @property
    def show_speed(self):
        return self.__speed
    
    @show_speed.setter
    def speed(self, new_speed):
        self.__speed = new_speed
    
car1 = Car() 
print(car1.show_speed)

car1.speed = 20
print(car1.show_speed)

'''
Задание 5

    Создайте класс Person и объявите в нем 3 атрибута класса: name (public), phone_number(protected) и сard_number(private),
    Атрибуты класса будут равны следующим значениям: "John", "+996 557 55 17 57" и "9999 9999 9999 9999".
    Создайте объект 'john' класса Person и выведите на экран все атрибуты класса.

'''

class Person:
    name =  "John"
    _phone_number = "+996 557 55 17 57"
    __сard_number = "9999 9999 9999 9999"
    @property
    def сard_number(self):
        return Person.__сard_number  #почему такой ответ не принимает платформа 
john = Person()
print(john.name)
print(john._phone_number)
print(john.сard_number)

#правильное решение

# class Person: 
#     name = "John" 
#     _phone_number = "+996 557 55 17 57" 
#     __card_number = "9999 9999 9999 9999"
#     @property 
#     def number(self): 
#         return self.__card_number  
# john = Person() 
# print(john.name) 
# print(john._phone_number) 
# print(john.number)

'''
Задание 6

    Создайте класс Person у которого будут следующие атрибуты экземпляра класса: name (public), phone_number(protected) и сard_number(private).
    Создайте экземпляр "john" класса Person со значениями ("John", "+996 557 55 17 57" и "9999 9999 9999 9999") и выведите на экран все его атрибуты.

'''
class Person: 
    def __init__(self, name, _phone_number, __card_number):
        self.name = name 
        self._phone_number = _phone_number
        self.__card_number = __card_number
    @property 
    def number(self): 
        return self.__card_number  
john = Person("John", "+996 557 55 17 57","9999 9999 9999 9999") 
print(john.name) 
print(john._phone_number) 
print(john.number)
