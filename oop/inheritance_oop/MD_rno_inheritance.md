# Принципы ООП. Наследование.

## Задание 1

Создайте класс Class1 с 2 методами - first и second.

Создайте второй класс Class2, который наследуется от Class1, и определите в новом классе Class2 ещё 2 метода - third и fourth.

Создайте экземпляр obj от класса Class2 и вызовите у него все четыре метода.

    внутри методов прописывать и возвращать ничего не нужно, можно просто оставить ключевое слово pass. pass говорит Python что функция пока ничего не выполняет, но в будущем возможно вы вернетесь и допишите туда код.
```py
class Class1:
    def first(self):
        pass
    def second(self):
        pass
class Class2(Class1):
    def third(self):
        pass
    def fourth(self):
        pass

obj = Class2()
print(obj.first()) 
print(obj.second()) 
print(obj.third()) 
print(obj.fourth()) 
```
> Чтобы obj нашел методы 1 и 2, то не нужо просто сослаться на родителя класса до этого как в строке 18. Теперь если во время print(obj.first()) 
print(obj.second()), наш код если не нашел данные методы в классе Class2(), то он идет в его род. класс

## Задание 2

Создайте класс A и определите в нём метод method1, который будет печатать строку

Основной функционал

Затем создайте второй класс B, который наследуется от класса A.

Внутри класса B переопределите method1 таким образом, чтобы он помимо строки "Основной функционал", также печатал строку

Дополнительный функционал

Объявите экземпляр класса B в переменной obj и вызовите метод method1. Результат в терминале должен быть:

Основной функционал 
Дополнительный функционал 

```py
class A:
    def method1(self):
        print('Основной функционал')
class B(A):
    def method1(self):
        super().method1()
        print('Дополнительный функционал')

obj = B()
obj.method1()
```
> Возможно добавление род. метода в дочерний метод, сохраняя оба метода


## Задание 3

Создайте класс MyString, который будет наследоваться от str.

Определите 2 своих метода:

    append, который будет принимать строку и добавлять её в конец исходной

    pop, который удаляет из строки последний элемент и возвращает его.

Затем, создайте экземпляр example от класса MyString со значением String. Добавьте к example строку 'hello' методом append, затем примените метод pop.

Пример:

example = MyString('String') 
example.append('hello') 
print(example) 

Вывод в терминал будет:

Stringhello 

Применим метод pop() к объекту example:

print(example.pop()) 
print(example) 

cам метод возвратит нам удаленную строку, в терминале получим:

o 
Stringhell 

```py
class MyString(str):
    def __init__(self, name):
        self.name = name
    def append(self, word):
        self.word = word
        self.name = self.name + self.word
        return self.name
    def pop(self):
        char = self.name[-1]
        self.name = self.name[:-1]
        return char
    def __str__(self):
        return self.name


example  =  MyString('String') 
print(example.append('hello'))
print(example.pop()) 
print(example)
```
> ОЧ ВАЖНАЯ ЗАДАЧКА

## Задание 4

Создайте класс MyDict который будет наследоваться от встроенного класса dict. Переопределите метод get() таким образом, чтобы при попытке получения несуществующего ключа, по умолчанию он возвращал, вместо None, строку:

Are you kidding?

Создайте экземпляр класса в переменной 'obj_dict' и попробуйте получить несуществующий ключ методом get().

Например:

obj_dict = MyDict({'some_title': 2}) 
print(obj_dict.get('some')) 

Ключа 'some' в нашем словаре нет, есть только 'some_title', в терминале получим:

Are you kidding? 

    Метод get имеет такой синтаксис: словарь.get(ключ, значение), в значение передается то что вы хотите возвратить если такого ключа не существует. По умолчанию, если второе значение не передано, метод возвращает None. Для переопределения метода унаследуйте метод от родителя и передайте в метод свое значение.

```py
class MyDict(dict):
    def __init__(self, dict_):
        self.dict_ = dict_
    def get(self, key):
        if self.dict_.get(key) == None:
            return 'Are you kidding?'
        return self.dict_.get(key)

obj_dict = MyDict({'some_title': 2}) 
print(obj_dict.get('some')) 
```
> 1. в инит нужно обязательно указать параметр dict_, так как при создании объекта мы создаем словарь
> 2. в def get(self, key) нужно обязательно написать key, так как сам метод словаря - get используется обязательно с ключом
> 3. self.dict_.get(key) - пишем именно так. Так как наш объект явл экземпляром класса MyDict, а также класса dict (ибо наш MyDict явл дочерним его классом) --> а это значит, что мы можем ссылаться на метода словаря и через self.dict_ и вытащить метод словаря get
> 4. затем мы создаем условие, где если наш метод get возарщает None, то возвращаем  'Are you kidding?', в ином случае значения существующего ключа

## Задание 5

Создайте класс Person который будет описывать человека, а точнее его имя - name и возраст - age. Добавьте к классу метод display(), который будет выводить данные об этом человеке.

Создайте второй класс Student, который будет наследоваться от класса Person.

Объекты от класса Student должны иметь все атрибуты, которые были определены в родительском классе и еще один дополнительный атрибут - faculty, который будет описывать факультет, где учится студент.

Создайте метод display_student(), который будет выводить данные об этом студенте.

Создайте от класса Student объект в перемнной obj_student, и выведите данные о нём, как о человеке, затем как о студенте.

Например, применим методы к объекту obj_student:

obj_student.display() 
obj_student.display_student() 

допустим, у нашего объекта в атрибуте name хранится значение Rick, в age - 21, а в faculty значение science, вывод в терминал должен быть:

name:Rick, age:21 
name:Rick, age:21, faculty:science 
```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f'name:{self.name}, age:{self.age}')
    
class Student(Person):
    def __init__(self, name, age, faculty):
        super().__init__(name, age)
        self.faculty = faculty 

    def display_student(self):
        print(f'name:{self.name}, age:{self.age}, faculty:{self.faculty}')
obj_student = Student('Rick', 21, 'science')
obj_student.display() 
obj_student.display_student() 
```

## Задание 7

Создайте класс SmartPhones, экземпляры класса должны иметь такие свойства:

    name - название
    color - цвет
    memory - память
    battery - процент заряда батареи

Значение battery по умолчанию должно быть 0.

Переопредилите метод str так чтобы при распечатке он выдавал строку с названием и памятью смартфона.

У данного класса также должен быть метод charge, который увеличивает значение батареи на указанную величину.

Создайте два дочерних класса от Smartphones:

    Iphone - с дополнительным аттрибутом экземпляра - ios и методом send_imessage(принимает в аргументы строку и возвращает эту строку и от какого телефона сообщение было выслано в таком формате - sending 'ваша строка' from 'название объекта-телефона')

    Samsung - с дополнительным аттрибутом android и методом show_time(который показывает текущее время)

Создайте объекты phone, iphone7, samsung21 от классов SmartPhones, Iphone, Samsung и примените все методы.

Для правильной работы тестов, проделайте все следующие операции:

создайте объект от класса SmartPhones:

phone = SmartPhones('generic', 'blue', '128GB') 
print(phone) 

вывод:

generic 128GB

распечатайте свойство батарейки,затем примените метод charge(), зарядив телефон до 20%:

print(phone.battery) 
phone.charge(20) 
print(phone.battery) 

получим в терминале:

0 
20 

создайте объект от класс Iphone, распечатайте этот объект, и примените метод send_imessage:

iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
print(iphone7)
print(iphone7.send_imessage('hello')) 

вывод будет:

Iphone 7 128gb 
sending hello from Iphone 7 128gb 

создайте объект от Samsung и примените метод show_time():

samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
print(samsung21.show_time()) 

вывод будет:

18:37:02.712036 

```py
import datetime

class SmartPhones:
    battery = 0
    def __init__(self, name, color, memory):
        self.name = name
        self.color = color
        self.memory = memory

    def charge(self, num):
        self.battery += num
        return self.battery

    def __str__(self):
        return f"{self.name} {self.memory}"
class Iphone(SmartPhones):
    def __init__(self, name, color, memory, ios):
        super().__init__(name, color, memory)
        self.ios = ios
    def send_imessage(self, message):
        self.message = message
        name = self.name + ' ' + self.memory
        return f"sending {self.message} from {name}"

class Samsung(SmartPhones):
    def __init__(self, name, color, memory, android):
        super().__init__(name, color, memory)
        self.android = android
    def show_time(self):
        now = datetime.datetime.now()
        now2 = str(now).split()[-1]
        return now2

phone = SmartPhones('generic', 'blue', '128GB') 
print(phone)
print(phone.battery) 
phone.charge(20) 
print(phone.battery) 

iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
print(iphone7)
print(iphone7.send_imessage('hello')) 

samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
print(samsung21.show_time()) 
```


