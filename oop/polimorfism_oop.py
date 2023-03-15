class Dog:
    def speak(self):
        print('гав-гав')

class Cat:
    def speak(self):
        print('мяу-мяу')

class Frog:
    def speak(self):
        print('ква-ква')
#в animals содержится множества объектов всех классов, которые мы указали в списке
animals = [Cat(), Frog(), Dog(), Cat(), Frog(), Dog()]
for animal in animals:  #т.е перчвый animal - это объект класса Cat, во 2 цикле - это объект класса Frog и так далее
    animal.speak()

list1 = [1,2,3,4,5]
dict1 = {'a' : 1, 'b' : 2}

list1.pop(0)   #удаление по индексу
dict1.pop('a')   #удаление по ключу

1 + 3
'a' + 'b'

# __add__
a = 4
b = 5
print(a+b)              #9
print(a.__add__(b))    #9
#вот что находится под копотом в символе "+", т.е данный символ вызывает метод __add__, который либо соединяет, либо суммирует значние 2 и более элементов

a = [1,2,3]
b = [4,5,6]
print(a+b)
print(a.__add__(b)) 
# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 6]

# __len__
a = 'abc'
print(len(a))       #3
print(a.__len__())  #3

b = [1,2,3,[4,5,6]]
print(len(b))  #4
print(b.__len__())  #4