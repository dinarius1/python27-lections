'''
Задание 15

    Напишите класса Person, который будет хранить информацию о пользователе. У объекта будут следующие атрибуты экземпляра класса: имя(name), фамилия(last_name), возраст(age), почта (email).
    При инициализации объекта, передавать аргументы классу не нужно, все его атрибуты по умолчанию будут равны None и также все они будут приватными.
    Поэтому реализуйте для каждого атрибута методы доступа get и set не используя декораторы property и setter. У вас будут такие методы: get_name, set_name, get_last_name, set_last_name, get_age, set_age, get_email, set_email.
    Создайте экземпляр john класса Person выедите все его атрибуты, затем измените их как показано ниже и после снова выведите на экран.

Пример:

john = Person()
print(john.get_name()) # None
print(john.get_last_name()) # None
print(john.get_age()) # None
print(john.get_email()) # None
john.set_name('John')
john.set_last_name('Snow')
john.set_age(30)
john.set_email('johnsnow@gmail.com')
print(john.get_name()) # John
print(john.get_last_name()) # Snow
print(john.get_age()) # 30
print(john.get_email()) # johnsnow@gmail.com
'''

class Person:
    def __init__(self):
        self.__name = None
        self.__last_name = None
        self.__age = None
        self.__email = None

    def get_name(self):
        return self.__name 
    
    def set_name(self, new):
        self.__name  = new
    
    def get_last_name(self):
        return self.__last_name  
    
    def set_last_name(self, new):
        self.__last_name  = new
    
    def get_age(self):
        return self.__age 
    
    def set_age(self, new):
        self.__age  = new
    
    def get_email(self):
        return self.__email
    
    def set_email(self, new):
        self.__email  = new

    
john = Person()
print(john.get_name()) # None
print(john.get_last_name()) # None
print(john.get_age()) # None
print(john.get_email()) # None
john.set_name('John')
john.set_last_name('Snow')
john.set_age(30)
john.set_email('johnsnow@gmail.com')
print(john.get_name()) # John
print(john.get_last_name()) # Snow
print(john.get_age()) # 30
print(john.get_email()) # johnsnow@gmail.com
