## Задание 1

Объявите 3 переменные - a, b и c.

В а запишите строку, в b - список и в с сохраните словарь. Затем запишите все три переменные в список, пройдитесь по нему циклом и распечатайте длину каждого из объектов.

Например:

a = '12342342345' 
b = [1,['a',5,6],2,3,4,5] 
c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'} 

Вывод:

11 
6 
3 

```py
a = 'a'
b = [1,2,3]
c = {1: True, 2: False}
res = [i for i in (a,b,c)]
for i in res:
    print(len(i))
```

## Задание 2

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

```py
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
```
> isinstance(animal, Dog) - в этом выражении animal - это именно параметр, не наш аргумент, поэтому необходимо ввести аругмент при выводе этой функции
> и аргументами буудт экземпляры наших классов. Т.е это выражение означает, что мы по факту подставляем вместо animal наш barsik или rex -> 
> if isinstance(barsik, Dog) - то есть здесь мы проверяем на принадлежность элмента к классу
> чтобы вызввать метод класса, то вот используем такую конструкцию:  Dog().voice() - обязательно 2 ()

## Задание 3

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

```py
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
```
>  мы используем на строке 114 (и в похожих строках) метод супер, чтобы унаследовать атрибуты от родительского класса. Несмотря на то,что мы унаследовали их, при обявлении экземпляра от дочернего класса (Emploee) нужно снова передавать аргументы от параметров name, last_name. Это нужно для того, что если  у нас вдруг будет новое имя или фамилия  у объекта от Emploee, которое отличается от имен и фамилий обхекта от Person.

> когда мы используем метод  супер - мы унаследовали именно не аргументы атрибутов, а их параметры!! -> т.е не 'Азамат', 'Айталиев', а констурукцию:
def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


## Задание 4

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
```py
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
```