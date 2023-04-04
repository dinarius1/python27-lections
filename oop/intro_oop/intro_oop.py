class Person:
    arms = 2
    legs = 2
    name = 'Nasty'

    def __init__(self, name) -> None:  #мы взяли init из самого класса object, и перезаписали его значение.

        #__init__ - dunder (двойные __) метод, который добавляет в объект self атрибуты, которые отличаются у разных объектов
        self.name = name  #атрибут обекта класса, все остальное, это атрибут класса

    def walk(self):  
        #self - это ссылка на объект, у которого мы вызываем данный метод
        
        #self - его нужно всегда писать и только так, это негласное правило
        print(self)
        print('я хожу')

# person1 = Person()
# print(person1)   #<__main__.Person object at 0x7f98b375bca0>

# print(type(person1))  #<class '__main__.Person'> - main - название файла, мы его оттуда  взяли наш класс 

# print(__name__)  #__main__ - название этого файла в программе - но почему main, а не intro.py?   ????????

# print(dir(person1)) # ['arms', 'legs', 'walk'] - показывает какие есть методы у person1


# print(person1.walk())  #так не стоит писать, так как тогда вернеться какой то обект

# Person.walk(person1)  
# person1.walk()   #я хожу - так проще писать

# p1 = Person()
# p2 = Person()
# p3 = Person()
# print(p1.name, p2.name, p3.name)
# print()

person1 = Person('Nasty')  #когда отрабатывается метод, то сразу отрабатывается init , а потом уже все остальное
person2 = Person('Nurkamilla')
print(person1.name, person2.name)


# Атрибуты класса и атрибуты объекта класса

class A:
    var1 = 'переменные класса'

    def __init__(self):
        self.var2 = 'переменные объекта'  #var2 - это метод


# print(dir(A))  #['var1'] - это атрибуты класса

obj = A() #obj это объект класса А
# print(dir(obj))  #['var1', 'var2'] - это атрибуты объекта, поэтому он берет атрибуты сначала класса А, и атрибуты своего объекта

class B:
    # def __init__(self) -> None:
    #     pass
    pass

f = B()
print(f)