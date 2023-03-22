class A:
    def instance_method(self):
        print('метод объекта')
        print('self', self)

obj = A()
obj.instance_method()
#метод объекта
# self <__main__.A object at 0x7fa522b5bb80>

# когла мы вызываем метод у объекта, то нам не нужно передавать его в self, он пердается автоматически

A.instance_method(obj) 
# метод объекта
# self <__main__.A object at 0x7f4b2cb57b80>

#когда вызываем какой то метод у самого класса, то необходимо передавать объект  в методе, так как мы вызываем метод не от объекта, а от класса


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

#Все равно откуда вы будете вызывать class_method (от объекта или от класса), то все равно будет выходить метод от класса



# примеры
class C:
    counter = 0

    def __init__(self):  #new - это больше метод класса, его ттоже можно было использовать
        #объект создается
        # C.counter += 1    #так не надо делать, так как лучше вообще напрямую не ссылаться на сам класс, лучше обходные пути исопльзовать
        self._inc_counter()

    def __del__(self):
        #объект удаляется
        # C.counter -= 1
        self._dec_counter()

    @classmethod
    def _inc_counter(cls):
        # cls - это класс С
        # увеличиваем атрибут класса counter на один
        cls.counter += 1
    
    @classmethod
    def _dec_counter(cls):
        cls.counter -= 1

obj1 = C()   #отрабатывается автоматически метод __init__
obj2 = C()
obj3 = C()
obj4 = C()
print(C.counter)  #4 - таким образом мы подсчитали кол во объекта

del obj1  #отрабатывается автоматически метод __del__
print(C.counter)  #3


class Pizza:
    def __init__(self, radius, *ingredients):
        self.r = radius
        self.ingredients = ingredients

    def cook(self):
        print(f'Пицца размером {self.r * 2}')
        print(f'Ингридиенты {self.ingredients}')
    
    @classmethod
    def four_cheeze(cls,radius):  #создаем метод от класса, который позволит каждый раз не расписывать иргридиенты пиццы
        pizza = cls(radius, "1 сыр", "2 сыр", "3 сыр", "4 сыр")
        #pizza = Pizza(10, "1 сыр", "2 сыр", "3 сыр", "4 сыр")
        return pizza

pizza1 = Pizza(15, 'Сыр', "Колбаски", "Помидоры")
pizza1.cook()
# Пицца размером 30
# Ингридиенты ('Сыр', 'Колбаски', 'Помидоры')

pizza2 = Pizza(10, "1 сыр", "2 сыр", "3 сыр", "4 сыр")
pizza2.cook()
# Пицца размером 20
# Ингридиенты ('1 сыр', '2 сыр', '3 сыр', '4 сыр')


pizza3 = Pizza(15, "1 сыр", "2 сыр", "3 сыр", "4 сыр")
pizza3.cook()

pizza4 = Pizza.four_cheeze(10)
pizza4.cook()
#Пицца размером 20
# Ингридиенты ('1 сыр', '2 сыр', '3 сыр', '4 сыр')

pizza5 = Pizza.four_cheeze(15)
pizza5.cook()
# Пицца размером 30
# Ингридиенты ('1 сыр', '2 сыр', '3 сыр', '4 сыр')

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
#когда не нужен объект, и не будем взаимодействовать с каким то данными в классе то мы можем просто провести ресчеты с помощью статика

#нужна статика, когда хотим чтобы какие то данные были внутри класса, хотя мы не будем их использовать. Это позволяет не захломлять наше глобальное пространство

