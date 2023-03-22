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

## Задание 5

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

```py
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
```

## Задание 6

Создайте класс Language, экземпляры которого имеют такие свойства как level и type. Наследуйте от данного класса два других класса - Python и JavaScript. И у Python, и у JavaScript должно быть два метода:

    write_function, принимает такие аргументы как func_name и arg
    create_variable, с аргументами var_name, value

Создайте экземпляр от класса Python в переменной py.

Затем, примените методы к экземпляру класса Python:

print(py.write_function('get_code', 'a')) 
print(py.create_variable('name', 'John'))

вывод должен быть такой:

def get_code(a):    
name = 'John'

Создайте экземпляр от класса JavaScript в переменной js.

Примените метод следующим образом:

print(js.write_function('validate', 'form')) print(js.create_variable('password', 'john@123'))

Вывод должен быть таким:

function validate(form) {     }; 
let password = 'john@123'

```py
class Language:
    def __init__(self, level, type):
        self.level = level
        self.type = type

class Python(Language):
    def write_function(self, func_name, arg):
        return f'def {func_name}({arg}):'
    def create_variable(self, var_name, value):
        if isinstance(value, str) == False:
            return f"{var_name} = {value}"
        return f"{var_name} = '{value}'"

class JavaScript(Language):
    def write_function(self, func_name, arg):
        return f'function {func_name}({arg}) ' + "{     };"
    def create_variable(self, var_name, value):
        if isinstance(value, str) == False:
            return f"let {var_name} = {value};"
        return f"let {var_name} = '{value}';"
    
# function validate(form) {     }; 
# let password = 'john@123'

py = Python(1,2)
js = JavaScript(1,3)

print(py.write_function('get_code', 'a')) 
print(py.create_variable('name', [1, 2, 3, 4]))

print(js.write_function('validate', 'form')) 
print(js.create_variable('password', [1, 2, 3, 4]))
```
> if isinstance(value, str) == False: - тут как раз мы проверяем , если наш объект явл экземпляром от класса str, то пусть будет такой вывод.

> Мы можем использовать isinstance даже со встроенными классами (как str, list и тп)

> При использовании ключа форматирования, нельзя чтобы было много пропусков(пробеллов/пустоты), а также нельзя использовтаь {} - так как он в данной конструкции по особоенному работает, поэтому надо писать так:
> 327 - return f'function {func_name}({arg}) ' + "{     };" - нужно именно так


## Таск 7

Создайте класс Money, объекты которого имеют аттрибуты country и symbol. Наследуйте от него классы Dollar и Euro. У данных методов должна быть переменная класса rate, курс к сому, Dollar - 84.80, Euro - 98.40. Добавьте к этим классам метод exchange, который принимает количество которое нужно обменять в переменную amount и возвращает такую строку:

$100 равен 8480.0 сомам
€80 равен 7872.0 сомам

```py
class Money:
    def __init__(self,country,symbol):
        self.country = country
        self.symbol = symbol
class Dollar(Money):
    rate = 84.80
    def exchange(self, amount):
        return f"$ {amount} равен {Dollar.rate * amount} сомам" 

class Euro(Money):
    rate = 98.40
    def exchange(self, amount): 
        return f"€ {amount} равен {Euro.rate * amount} сомам" 
dol = Dollar('Alaska', '$') 
eu = Euro('France', '€') 

print(dol.exchange(100)) 
print(eu.exchange(80))
```
> Чтобы ссылаться на атрибуты (+ методы) класса, то нужно так писать:
Dollar.rate * amount, а не Dollar()

> мы пишем Dollar() - только когда обявляеям экземпляр класса

## Таск 8

Создайте классы Mercury, Venus, Jupiter, которые наследуют метод __init__ от родительского класса Planet. У объектов данного класса должен быть аттрибут orbit, орбита в классе Venus состовляет 225 земных дней, Mercury 88 земных дней, а на Jupiter 12 дней. У всех этих классов должен быть метод get_age, принимающий возраст в переменную earth_age и расчитывающий ваш возраст на данной планете.

Метод должен возвращать возраст на Mercury в годах, на Venus в днях и на Jupiter в часах. Например, если возраст earth_age равен 20:

на Венере ваш возраст составляет 11842 дней
на Юпитере ваш возраст составляет 5326080 часов
на Меркурии ваш возраст составляет 82 лет

```py
class Planet: 
    def __init__(self, orbit): 
        self.orbit = orbit 

class Mercury(Planet): 
    def get_age(self, earth_age): 
        return f'на Меркурии ваш возраст составляет {int(earth_age * 365 /self.orbit)} лет' 

class Venus(Planet): 
    def get_age(self, earth_age): 
        return f'на Венере ваш возраст составляет {round(earth_age * 365 / self.orbit * 365)} дней' 

class Jupiter(Planet): 
    def get_age(self, earth_age): 
        return f'на Юпитере ваш возраст составляет {round(earth_age * 365 // self.orbit * 365 * 24)} часов' 

mercury = Mercury(88) 
venus = Venus(225) 
jupiter = Jupiter(12) 
print(venus.get_age(20)) 
print(jupiter.get_age(20))
print(mercury.get_age(20))
```
> Один орбитальный оборот, так называемый сидерический год. Орбитальный оборот Земли продолжается 365,256 суток. А у Venus состовляет 225 земных дней,у Mercury 88 земных дней, а на Jupiter 12 дней. Поэтому и мы все время делили на 365