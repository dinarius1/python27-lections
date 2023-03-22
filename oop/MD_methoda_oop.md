# class/static/instance methods
> **instance methods** - методы, которые первым аргументом принимают объект от классов (instance, self), используются для работы с объектом и его атрибутами
- нужен для работы с объектом

```py
class A:
    def instance_method(self):
        print('метод объекта')
        print('self', self)

obj = A()
obj.instance_method()
```

> **class methods** - методы, которые первым аргументом принимают класс (class). Используются для работы с классом и его атрибутами
- нужен для созданият объекта по шаблону

```py
class A:
    @classmethod    # необходимо обязательно задекодировать нашу функцию class_method
    def class_method(cls):
        print('метод класса')
        print('cls', cls)

A.class_method()
# метод класса
# cls <class '__main__.A'>

obj = A()
obj.class_method()
# метод класса
# cls <class '__main__.A'>
```

> для создания class метода, нужно использовать декоратор "classmethod"

> **static methods** - методы, которые не взаимодействуют с объектом и классом, но находятся внутри класса (по принципу инкапсуляции (все, что нужно для работы класса лежат внутри класса))

```py
class A:
    @staticmethod
    def static_method():
        print('статик метод')

obj = A()
obj.static_method()  
# статик метод 

#мы не ссылаемся на класса или объекта, но все равно моэем запринтить наш результат 

class Cylinder:
    def __init__(self, diameter, height):
        self.di = diameter
        self.h = height
        self.area = self.get_area(diameter, height)
    
    @staticmethod
    def get_area(di, h):
        from math import pi
        circle_area = pi * di ** 2 /4 #окружность сверху у цилиндра
        side_area = pi * di * h  #бокая сторона
        return circle_area * 2 + side_area

cylinder1 = Cylinder(4,10) 
print(cylinder1.area)  #когда нужен объект

print(Cylinder.get_area(4,10))  
```
> Нужна статика, когда не нужен объект, и не будем взаимодействовать с каким то данными в классе то мы можем просто провести ресчеты с помощью статика

> нужна статика, когда хотим чтобы какие то данные были внутри класса, хотя мы не будем их использовать. Это позволяет не захломлять наше глобальное пространство
