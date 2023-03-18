gen = (x for x in range(10))
print(gen)
# <generator object <genexpr> at 0x7f16570d2420> - так как это генератор, то необходимо обязательно его оборачивать либо в список/словарь/сет, а у нас кортеж, поэтомы выводиться такая запись

def generator(n):
    for i in range(1, n+1):
        yield i**2   
        # yield - это что то под типа return, но он используется только с генераторами
        # yield - он возвращает каждый элемент из цикла созданного нами генератора, но он явл ленивым ключивым словом, он возварщ



        # [ i**2 for i in range(1, n+1)]

print(generator(10))
# <generator object generator at 0x7ff7bc65e490>

gen = generator(10)
print(next(gen)) # 1
print(next(gen)) # 4
print(next(gen)) # 9
print(list(gen)) # [16, 25, 36, 49, 64, 81, 100]

for i in generator(5):
    print(i)
# 1
# 4
# 9
# 16
# 25

gen = generator(15)
while True:
    try:
        print(next(gen))
    except StopIteration:
        break
# 1 4 9 16 25 36 49 64 81 100 121 144 169 196 225

class IterInt(int):
    def __iter__(self):
        for i in str(self):
            yield int(i)

    def __len__(self):
        return len([i for i in self])

    def __getitem__(self, index):
        return [i for i in self][index]


a = IterInt(1234567)

for i in a:
    print(i)

print(8 in a)
print(5 in a)
# print(len(a))
# print(a[-1])
print(a[1:4])



# string1 = 'abcefasd'
# string2 = 'gasd'
# print(string1 > string2)  #мы используем таблицу Аскель, и сравниваем первые буквы из string1 и string2

# class MyStr:
#     def __init__(self, string):
#         self.string = string
    
#     def __len__(self):
#         return len(self.string)
    
#     def __eq__(self, other):
#         return len(self) == len(other)
    
#     def __ge__(self, other):
#         return len(self) >= len(other)
    
#     def __gt__(self, other):
#         return len(self) > len(other)
    
#     def __le__(self, other):
#         return len(self) <= len(other)
    
#     def __lt__(self, other):
#         return len(self) < len(other)

# string1 = MyStr('hello')
# string2 = MyStr('skdls')

# print(len(string1)) #вызывается ошибка, так как мы получаес генератор, мы не используем string1.string. Это до того, как мы переопределили методы le, eq и тп

# print(len(string1)) #после преопредедения
# print(string1 == string2) #True

# # __eq__ ==
# # __ge__ >=
# # __gt__ >
# # __le__ <=
# # __lt__ <
# # __ne__ !=
# # __add__ +
# # __sub__ -
# # __floordiv__ /
# # __truediv__ //

class A:
    attr1 = 'aaa'

    def __getattribute__(self, name): #ищет атрибут у объекта, который мы задали в name
        print('__getattribute__', name)
        return super().__getattribute__(name)
    
    def __setattr__(self, name, value):
        print('__setattr__', name, value)
        return super().__setattr__(name, value)
    
    def __delattr__(self, name):
        print('__delattr__', name)
        return super().__delattr__(name)

obj = A()
obj.attr1  #obj.__getattribute__('attr1') 
# __getattribute__ attr1

obj.attr1 = 'bbb'  #obj.__setattr__('attr1', 'bbb')
# __setattr__ attr1 bbb

del obj.attr1 #__delattr__ attr1 -вывелся результат принт, но не вернулось значение, так как мы использовали же как раз удалили

print(A.__dict__) 
# внизу это методы и атрибуты класса A, по факту это dir, но он кроме названия атрибута он возвращает значения всех этих атрибутов. И показывает только то, что мы создали новое в классе А, т.е он не показывает все атрибуты класса

# {'__module__': '__main__', 'attr1': 'aaa', '__getattribute__': <function A.__getattribute__ at 0x7f8b4b38e560>, '__setattr__': <function A.__setattr__ at 0x7f8b4b38e5f0>, '__delattr__': <function A.__delattr__ at 0x7f8b4b38e680>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}

#Это не только методы, но еще и функции. Вот так можно еще выводить данные методы
getattr(obj, 'attr1') #__getattribute__ attr1 - выходит такой результат, так как мы до этого их перезаписали
setattr(obj, 'new_attr', '1')  #__setattr__ new_attr 1
delattr(obj, 'new_attr') #__delattr__ new_attr

#Солид - прочитать про него

