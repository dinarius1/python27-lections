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

class Person: 
    name = "John" 
    _phone_number = "+996 557 55 17 57" 
    __card_number = "9999 9999 9999 9999"
    @property 
    def number(self): 
        return self.__card_number  
john = Person() 
print(john.name) 
print(john._phone_number) 
print(john.number)

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

'''
Задание 7

    Снова создайте класс Person и объявите в нем 3 атрибута: name (public), phone_number(protected) и сard_number(private), атрибуты класса будут равны следующим значениям: "John", "+996 557 55 17 57" и "9999 9999 9999 9999".
    Создайте объект "john" класса Person и измените все атрибуты экземпляра класса на значение None после выведите все атрибуты этого экземпляра класса.

'''
class Person: 
    name = "John" 
    _phone_number = "+996 557 55 17 57" 
    __card_number = "9999 9999 9999 9999"
    @property 
    def number(self): 
        return self.__card_number  
    @number.setter
    def number(self, new): 
        self.__card_number = new
    
john = Person() 
john.name = None
john._phone_number = None
john.number = None
print(john.name) 
print(john._phone_number) 
print(john.number)

'''
Задание 8

    Продолжая изменять логику предыдущего задания создайте класс Person у которого будут следующие атрибуты экземпляра класса: name (public), phone_number(protected) и сard_number(private).
    При инициализации объекта проверяйте введенные имя. Для этого напишите приватный метод validate_name для валидации имени: данный метод будет проверять длину имени, если длина имени меньше двух то возвращайте имя по дефолту John,
    Если же введенное пользователем имя больше двух, то необходимо возвращать имя с заглавной буквы (JOHN -> John, john -> John и тд).
    Создайте экземпляр sam класса Person со значениями ("SAM", "+996 557 55 17 57" и "9999 9999 9999 9999") и выведите на экран все его атрибуты

'''

class Person: 
    def __init__(self, name, phone_number, card_number): 
        self.name = self.__validate_name(name)  #атрибут может иметь знаечение метода? 
        self._phone_number = phone_number 
        self.__card_number = card_number 
    def __validate_name(self, name): 
        if len(name) < 2: 
            return "John" 
        return name.title() 
    def get_card_number(self): 
        return self.__card_number 
    def set_card_number(self, card_number): 
        self.__card_number = card_number 

sam = Person("SAM", "+996 557 55 17 57", "9999 9999 9999 9999") 
print(sam.name) 
print(sam._phone_number) 
print(sam.get_card_number())

'''
Задание 9

    На этот раз заказчик передумал и попросил вас переписать предыдущий класс, теперь его интересует только валидация номера телефона и номера карты.

    Создайте класс Person у которого будут следующие атрибуты экземпляра класса: name (public), phone_number(protected) и сard_number(private). При инициализации объекта проверяйте введенный номер телефона и номер карты.

    Для этого напишите защищенный метод validate_phone_number и приватный метод validate_card_number.

    Метод validate_phone_number в первую очередь проверяет на то что бы номер был объектом от класса int иначе возвращаем None, 
    во вторую - начинался с 996 
    
    *Метод validate_card_number в первую очередь также проверяет на то что бы номер карты был объектом от класса int иначе возвращаем None, далее нужно также проверять чтобы количество цифр в номере карт было ровно 16 иначе также возвращаем None.
    Создайте экземпляр tolik класса Person c правильными данными и выведите на экран все его атрибуты

'''
#мое 1 решение
class Person: 
    def __init__(self, name, _phone_number, __card_number): 
        self.name = name
        self._phone_number = self._validate_phone_number(_phone_number)
        self.__card_number = self.__validate_card_number(__card_number)
         
    def _validate_phone_number(self,_phone_number):
        if isinstance(_phone_number, int) != True:
            return None
        elif str(_phone_number).startswith('996') == True:
            return _phone_number
        
    def __validate_card_number(self,__card_number):
        if isinstance(__card_number, int) != True:
            return None
        elif len(str(__card_number)) == 16:
            return __card_number
        else:
            return None

# 2 решение - правильное, ЕСТЬ ВОПРОСЫ
tolik = Person("tolik", 996557551757 , 9999999999999999)
print(tolik.name)
print(tolik._phone_number)
print(tolik._Person__card_number)

class Person: 
    def __init__(self, name, phone_number, card_number): 
        self.name = name 
        self._phone_number = self._validate_phone_number(phone_number) 
        self.__card_number = self.__validate_card_number(card_number)  #ПОЧЕМУ В ИНИТЕ ПРОСТО card_number, а в присваивании атрибута self.__card_number?
    
    def _validate_phone_number(self, phone_number): 
        if isinstance(phone_number, int) and str(phone_number).startswith('996'): #т.е не надо прописывать что каждое условие должно быть верным, да???
            return phone_number
        return None 
    def __validate_card_number(self, card_number): 
        if isinstance(card_number, int) and len(str(card_number)) == 16: 
            return card_number 
        return None 
tolik = Person('Sam', 996557551757, 9999999999999999) 
print(tolik.name) 
print(tolik._phone_number) 
print(tolik._Person__card_number)