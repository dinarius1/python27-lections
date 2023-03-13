class A:
    def method(self):
        print('Метод в классе А')

obj_a = A()
obj_a.method() # Метод в классе А

class B(A): #все что было в классе А, копируется в класс В
    pass

obj_b = B()
obj_b.method() # Метод в классе А

class C(A):
    def method(self):
        print('Метод в классе C') 

obj_c = C()
obj_c.method()  # Метод в классе C - потому что мы перезаписали метод в классе С, который взяли из класса А

class A:
    def method(self):
        print('Метод в классе А')
        return "AAA"
    
class B(A):
    def method(self):
        print("Метод в классе B")
        return_from_super = super().method()
        print('super().method() вернул', return_from_super)
        return "BBB"
    

obj_a = A()
res_a = obj_a.method()
print('A.метод вернул', res_a)  
# Результат:
# Метод в классе А
# A.метод вернул AAA

obj_b = B()
res_b = obj_b.method()
print('B.метод вернул', res_b)
# Результат:
# Метод в классе B -    из print("Метод в классе B") - 28 стр
# Метод в классе А -    из return_from_super = super().method() - заработал super().method(), но значение в return сохранилось в return_from_super
# super().method() вернул AAA     - значение из return_from_super
# B.метод вернул BBB  

class Range:
    def create(self,n):
        ''' Принимает число и возвращает список чисел от 0 до данного числа включительно'''
        return list(range(n+1))

class Range10(Range):
    def create(self):
        '''Возвращает список чисел от 0 до 10 включительно '''
        return super().create(10)
range_obj = Range()
res = range_obj.create(5)  
print(res)  #[0, 1, 2, 3, 4, 5]

range10_obj = Range10()
res = range10_obj.create()
print(res)  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#Виды наследования
class A:
    attr1 = 'a'
    def method(self):
        print('Метод в классе А')

class B:
    attr2 = 'b'
    def method(self):
        print('Метод в классе B') 

class C(A,B): #тут важен порядок классов родителей, то что стоит первее, то он главнее. Поэтому в резултате выведяться метод класса А, а не класса В. Также так было бы с атрибутами, если обо атрибута имели одинаковое имя
    pass

obj_c = C()
print(obj_c.attr1)
print(obj_c.attr2)
obj_c.method()
'''
В obj_c происходит поиск классов - это значит, что сначала он ищет значение, которое внутри самого класса С, так как наш объект в первую очередь объект класса С, затем он ищет в родительском классе, а потом уже в классе Obj

...
'''
print(C.mro())  
# mro() - метод, который записывает 
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

# Перекрестное наследование
class A:
    pass
class B:
    pass
class C(A,B):
    pass
class D(B,A):
    pass
class E(C,D): #Cannot create consistent method ordering
    pass
#TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, B