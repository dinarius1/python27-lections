## Задание 1

Создайте класс A и объявите в нём 3 метода:

    публичный(public) (возвращает строку 'Public method'),
    защищённый(protected) (возвращает строку 'Protected method')
    приватный(private) (возвращает строку 'Private method')

Затем создайте экземпляр в переменной obj1 данного класса и вызовите (с выводом в терминал) по очереди каждый из методов. Не забудьте, что нужно вызвать приватный метод так, чтобы ошибка не выводилась

```py
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
```
> чтобы вытащить приватный метод, то можно сослаться на класс и вытащить оттуда его метод

> print(obj1._A__private()) - _A__private() - это такой синтаксис, который мы используем чтобы вытащить приватный метод у класса

??мы переименовали метод __private() на _A__private(), то есть программи видит, что наш экземпляр явл классом А, видит что нужно вытащить из класса А какой то метод, понимает, что это приватный метод, поэтому переименовывает его на _A__private()

## Задание 2

Определите класс A, в нём объявите метод method1, который печатает строку "Hello World".

Затем, создайте класс B, который будет наследоваться от класса A.

Создайте экземпляр в переменной b1 от класса B, и через него вызовите метод method1.

```py
class A:
    def method1(self):
        print("Hello World")
class B(A):
    pass

b1 = B()
b1.method1()
```

## Задание 3

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

```py
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
```

## Задание 4

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

```py
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
```
> чтобы декораторы работали корректно, оба метода и setter и getter должны иметь одно название, так как если это не сделать, то будет выдаваться ошибка

> причина этому заключается в том, что в декораторе проперти есть метод сеттер, и грубо говоря, когда мы используем декоратор сеттер, то мы перезаписываем этот метод у проперти на то, что мы напишем а данном декораторе

## Задание 5

    Создайте класс Person и объявите в нем 3 атрибута класса: name (public), phone_number(protected) и сard_number(private),
    Атрибуты класса будут равны следующим значениям: "John", "+996 557 55 17 57" и "9999 9999 9999 9999".
    Создайте объект 'john' класса Person и выведите на экран все атрибуты класса.

```py
class Person:
    name =  "John"
    _phone_number = "+996 557 55 17 57"
    __сard_number = "9999 9999 9999 9999"
    @property
    def сard_number(self):
        return self.__card_number
        # return Person.__сard_number  #почему такой ответ не принимает платформа 
john = Person()
print(john.name)
print(john._phone_number)
print(john.сard_number)
```
> когда мы используем экземпляр класса, то нужно ссылаться на атрибут экземпляра соответсвенно, а не на атрибут класса

## Задание 6

    Создайте класс Person у которого будут следующие атрибуты экземпляра класса: name (public), phone_number(protected) и сard_number(private).
    Создайте экземпляр "john" класса Person со значениями ("John", "+996 557 55 17 57" и "9999 9999 9999 9999") и выведите на экран все его атрибуты.

```py
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

```

## Задание 7

    Снова создайте класс Person и объявите в нем 3 атрибута: name (public), phone_number(protected) и сard_number(private), атрибуты класса будут равны следующим значениям: "John", "+996 557 55 17 57" и "9999 9999 9999 9999".
    Создайте объект "john" класса Person и измените все атрибуты экземпляра класса на значение None после выведите все атрибуты этого экземпляра класса.
```py
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
```
> чтобы поменять атрибуты экземпляра, которые можно вытащить, то просто после создания объекта от класса меняем их значения на то, что нам надо

> однако с приватными ланными такое нельзя сделать, поэтомы мы оборачиваем его в деоратор сеттер

## Задание 8

    Продолжая изменять логику предыдущего задания создайте класс Person у которого будут следующие атрибуты экземпляра класса: name (public), phone_number(protected) и сard_number(private).
    При инициализации объекта проверяйте введенные имя. Для этого напишите приватный метод validate_name для валидации имени: данный метод будет проверять длину имени, если длина имени меньше двух то возвращайте имя по дефолту John,
    Если же введенное пользователем имя больше двух, то необходимо возвращать имя с заглавной буквы (JOHN -> John, john -> John и тд).
    Создайте экземпляр sam класса Person со значениями ("SAM", "+996 557 55 17 57" и "9999 9999 9999 9999") и выведите на экран все его атрибуты

```py
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
```
>  атрибут может иметь знаечение метода (в значение входит return метода)

## Задание 9

    На этот раз заказчик передумал и попросил вас переписать предыдущий класс, теперь его интересует только валидация номера телефона и номера карты.

    Создайте класс Person у которого будут следующие атрибуты экземпляра класса: name (public), phone_number(protected) и сard_number(private). При инициализации объекта проверяйте введенный номер телефона и номер карты.

    Для этого напишите защищенный метод validate_phone_number и приватный метод validate_card_number.

    Метод validate_phone_number в первую очередь проверяет на то что бы номер был объектом от класса int иначе возвращаем None, 
    во вторую - начинался с 996 
    
    *Метод validate_card_number в первую очередь также проверяет на то что бы номер карты был объектом от класса int иначе возвращаем None, далее нужно также проверять чтобы количество цифр в номере карт было ровно 16 иначе также возвращаем None.
    Создайте экземпляр tolik класса Person c правильными данными и выведите на экран все его атрибуты

```py
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
```
> self.__card_number = self.__validate_card_number(card_number) надо именно так писать, чтобы метод принимал видимую переменную. Так как если так напишем 
self.__card_number = self.__validate_card_number(__card_number), то выйдет ошибка, ибо приватные атрибуты не видяться программой

## Задание 10

    Необходимо написать класс Game у которого есть приватный атрибут класса "level" который равен нулю и атрибут экземпляра класса name (ваше имя).
    Класс Game должен иметь методы для увеличения уровня игры (play) и получения текущего уровня (get_level).
    Метод play принимает в себя переменную hours и проверяет если значение этой переменной больше двух то уровень игры увеличивается на единицу иначе ничего не происходит. Так как атрибут класса "level" приватный и поэтому недоступен извне, необходимо реализовать метод "get_level" который возвращает значение атрибута "level".
    Создайте экземпляр "game" класса Game. Выведите на экран значение атрибута "level" затем два раза используйте метод play чтобы уровень игры поднялся на два, после снова выведите на экран значение атрибута "level".
```py
class Game:
    __level = 0
    def __init__(self, name):
        self.name = name

    def play(self, hours):
        if hours > 2:
            self.__level += 1   #обязательно так пишем, а не Game.__level - так как это означает,что мы работаем с атрибутом класса, когда как нам нужно работать с экземпляром класса, и с его атрибутом, который он унаследовал от класса
        else:
            return None
    
    def get_level(self):
        return self.__level

game = Game('Mario')
print(game.get_level())
game.play(3)
game.play(5)
print(game.get_level())
```


## Задание 11

    Необходимо написать класс Game у которого есть приватный атрибут класса "level" который равен нулю и атрибут экземпляра класса name (ваше имя).

    Класс Game должен иметь два метода: "set_level" и приватный метод "validate_name".
    При инициализации экземпляра класса вызывается приватный метод validate_name который возвращает имя в котором первая буква в верхнем регистре, а остальные в нижнем (JOHN -> John).
    Также в классе необходимо реализовать метод "set_level" который принимает в себя переменную "level" и увеличивает значение приватного атрибута класса "level" на значение этой переменной которую передали только в том случае если имя объекта (который сейчас играет в эту игру) "Tolik", иначе выведите на экран

"имя_объекта" ты не Tolik!'.

    Создайте сначала экземпляр класса "game" и передайте ему имя Raychel в качестве аргумента. Далее вызовите метод set_level и передайте ему значение 5. После выведите в терминал значение атрибута "level" (так как у нас не реализован метод get_level, выведите это "нелегальным" способом). Теперь создайте экземпляр класса game2 и передайте ему имя "TOLIK" в качестве аргумента. Далее вызовите метод set_level и передайте ему значение 5. После выведите в терминал значение атрибута "level" (так как у нас не реализован метод get_level, выведите это "нелегальным" способом).

Ожидаемый вывод:

Raychel ты не Tolik!
0
5

```py
class Game:
    __level = 0
    def __init__(self, name):
        self.name = self.__validate_name(name)    #в знаечние переменной входит значение метода (то есть то,что записано у метода в return)
        #внутри метода прописываем параметр name, чтобы мы могли его исопльзовать в методе

    def __validate_name(self, name):
        return name.title()       # пишем просто name, без ничего, так как мы работаем с параметром name, который мы передали в ините

    def set_level(self, new):
        if self.name == 'Tolik':
            self.__level = new
        else:
            print(f'{self.name} ты не Tolik!')

game = Game('Rachel')
game.set_level(5)
print(game._Game__level)

game2 = Game('TOLIK')
game2.set_level(5)
print(game2._Game__level)
```

## Задание 12

    Необходимо написать класс Game у которого есть приватный атрибут класса level который равен нулю и атрибут экземпляра класса name (ваше имя).
    Так как атрибут класса level приватный и поэтому недоступен извне, необходимо реализовать два метода для работы с ним: get_level и set_level. Где get_level возвращает значение атрибута level и set_level принимает значение и присваивает его атрибуту level.
    Создайте экземпляр game класса Game. Выведите на экран значение атрибута level затем присвойте ему значение 10 и выведите его на экран.
```py
class Game:
    __level = 0
    def __init__(self, name):
        self.name = name
    
    def get_level(self):
        return self.__level
    
    def set_level(self, new):
       self.__level = new

game = Game('R')
print(game.get_level())
game.set_level(10)
print(game.get_level())
```


## Задание 13

    Необходимо написать класс Game у которого есть приватный атрибут класса level который равен нулю. Напишите метод level с использование декоратора @property для предоставления доступа к атрибуту level.
    Создайте экземпляр game класса Game. Выведите на экран значение атрибута level.

```py
class Game:
    __level = 0

    @property
    def level(self):
        return  self.__level

game = Game()
print(game.level)
```

## Задание 14

    Необходимо написать класс Game у которого есть приватный атрибут класса level который равен нулю. Напишите метод level с использованием декоратора @setter для того чтобы вы имели право на изменение приватного атрибута класса level вне класса Game. Но обратите внимание что вы не сможете написать этот метод без метода level у которого используется декоратор @property, поэтому также создайте этот метод.
    Создайте экземпляр game класса Game. Выведите на экран значение атрибута level, после 'легально' измените значение level на 10 и снова выведите это значение на экран.

```py
class Game:
    __level = 0

    @property
    def level(self):
        return  self.__level
    
    @level.setter
    def level(self, new):
        self.__level = new

game = Game()
print(game.level)
game.level = 10
print(game.level)
```

