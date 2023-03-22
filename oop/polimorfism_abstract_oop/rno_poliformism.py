'''
Задание 2

Создайте классы Dog и Cat с одинаковым методом voice.

Для собак он должен печатать "Гав", для кошек "Мяу".

Объявите для каждого из классов по экземпляру, для класса Cat экземпляр в переменной barsik, а для Dog экземпляр rex.

Затем, вне класса объявить функцию to_pet(), которая будет принимать животное и вызывать у него метод voice().

Ввод:

to_pet(barsik) 
to_pet(rex) 

Вывод:

Мяу 
Гав 
'''

class Dog:
    def voice(self):
        print('Гав')
class Cat:
    def voice(self):
        print('Мяу')

def to_pet(animal):
    if isinstance(animal, Dog):
        Dog().voice()
    else:
        Cat().voice()
    
rex = Dog()
barsik = Cat()
to_pet(barsik) 
to_pet(rex) 

'''
3 таск

Создайте 3 класса: Person с параметрами name и last_name, Employee с work и status, Student c university и course, при этом Employee и Student должны наследоваться от Person.

Определите во всех трёх классах метод get_info():

    для класса Person он должен возвращать следующее: “Привет, меня зовут Иван Петров”.

    для класса Employee он должен возвращать: “Привет, меня зовут Иван Петров, я работаю в компании Рога и копыта на должности директор.

    для класса Student должно возвращаться: “Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе”.

Вне класса, определите функцию get_human_info(), которая будет принимать объект одного из трёх классов и вызывать у него метод get_info и распечатывать результат этой функции.

Создайте для каждого класса по экземпляру, для Person экземпляр person, для Employee экземпляр employee и student для класса Student.

Вызовите метод get_human_info у каждого экземпляра печатать результат.

Ввод должен быть:

get_human_info(employee) 
get_human_info(student) 
get_human_info(person) 

Вывод:

Привет, меня зовут Иван Петров, я работаю в компании Рога и Копыта на должности директор 
Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе 
Привет, меня зовут Иван Иванов 

'''

class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
    
    def get_info(self):
        print(f'Привет, меня зовут {self.name} {self.last_name}')


class Employee(Person):
    def __init__(self, name, last_name, work, status):
        super().__init__(name, last_name)
        # В ЧЕМ СМЫСЛ ИСПОЛЬЗОВАТЬ МЕТОД СУПЕР, ЕСЛИ НАМ ВСЕ РАВНО НУЖНО БУДЕТ ВЕСТИ ДАННУЮ ПЕРЕМЕННУЮ В АРГУМЕНТ ОБЕКТА КАК НА СТРОКЕ 111??

        self.work = work
        self.status = status

    def get_info(self):
        print(f'Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}')

class Student(Person):
    def __init__(self, name, last_name, university, course):
        super().__init__(name, last_name)
        self.university = university
        self.course = course
    
    def get_info(self):
        print(f'Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе')

def get_human_info(human):
    if isinstance(human, Employee):
        human.get_info()
    elif isinstance(human, Student):
        human.get_info()
    elif isinstance(human, Person):
       human.get_info()


person = Person('Азамат', 'Айталиев')
employee = Employee('Азамат', 'Айталиев', 'The Most', 'официант')
student = Student('Азамат', 'Айталиев', 'КГЮА', 1)
get_human_info(person)
get_human_info(employee)
get_human_info(student)

'''
4 таск

Объявите абстрактный класс геометрических фигур Shape и определите в нём абстрактный метод get_area() для расчёта площади фигуры, которые необходимо переопределить в дочерних классах.

Затем, наследуйте от Shape три класса: Triangle, Square и Circle.

    треугольник создаётся с заданными основанием base и высотой height

    квадрат создаётся с заданной длиной стороны length

    круг создаётся с заданным радиусом radius

Переопределите в каждом из классов метод get_area() таким образом, чтобы он рассчитывал площадь для конкретной фигуры.

Затем, создайте от каждого из трёх классов по экземпляру, и вызовите у каждого метод get_area()

    Подсказка: для создания абстрактных классов воспользуйтесь модулем abc - https://docs.python.org/3/library/abc.html

Ввод должен быть:

print(triangle.get_area()) 
print(square.get_area()) 
print(circle.get_area()) 

Вывод:

12.5 
25 
314.1592653589793 
'''

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def get_area(self):
        return 1/2 * self.base * self.height

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def get_area(self):
        return self.length * self.length

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        from math import pi
        return pi * self.radius ** 2
    
triangle = Triangle(1,2)
square = Square(564)
circle = Circle(2)

print(triangle.get_area()) 
print(square.get_area()) 
print(circle.get_area()) 

'''
Задание 5

Создайте класс OS, экземпляры которого имеют аттрибут version - версия системы. От OS наследуйте три класса - Windows, MacOS, Linux.

У всех трех классов должен быть метод copy который принимает в аргументы text и возвращает соответствующую строку.

Создайте экземпляры класса, от Windows - в переменной win, от MacOS - mac, а от Linux в переменной lin.

Примените к каждому объекту метод copy, следующим образом:

Ввод должен быть:

print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
 
print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах')) 
 
print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))

Вывод должен быть:

скопирован текст "Полиморфизм — одна из основных парадигм ООП" горячими клавишами CTRL + C
 

скопирован текст "Полиморфизм - разное поведение одного и того же метода в разных классах" горячими клавишами COMMAND + C
 

скопирован текст "На самом деле одинаковым является только имя метода, его исходный код зависит от класса" горячими клавишами CTRL + SHIFT + C
'''

class OS:
    def __init__(self, version):
        self.version = version

class  Windows(OS):
    def copy(self, text):
        return f'скопирован текст "{text}" горячими клавишами CTRL + C'
    
class MacOS(OS):
    def copy(self, text):
        return f'скопирован текст "{text}" горячими клавишами COMMAND + C'
    
class Linux(OS):
    def copy(self, text):
        return f'скопирован текст "{text}" горячими клавишами CTRL + SHIFT + C'

win = Windows(1)
mac = MacOS(2)
lin = Linux(3)

print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
 
print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах')) 
 
print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))