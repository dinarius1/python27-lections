# Инкапсуляция
> принцип ООП, у которого есть 2 трактовки
1. все, что нужно для работы класса - лежит в классе
2. сокрытие данных (ограничение доступа к атрибутам)

## Виды доступа
1. public (публичный)
2. protected (защищенный) - один андерскор в начале названия атрибута (метод и свойство)
3. private (приватные) - два андерскора в начале названия (метод и свойство)

> В Питоне инкапсуляция реализована на уровне соглашения
```py
class A:
    attr1 = 'public'
    _attr2 = "protected"  #означает, что лучше его не менять
    __attr3 = 'private'   #означает, что вы не можете вывести данные данного атрибута
 
print(A.attr1)
print(A._attr2)
# print(A.__attr3)
# public
# protected
# AttributeError: type object 'A' has no attribute '__attr3'. Did you mean: '_A__attr3'?
print(A._A__attr3)
```

# Getters / Setters
> методы, с помощью которых мы указываем каким образом мы можем получать и изменять какие то атрибуты
```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def get_age(self):
        return  self.__age
    
    def set_age(self, new_age):
        if new_age > 0 and new_age < 120:
            self.__age = new_age
        else:
            raise Exception('Invalid age')
obj = Person('Nasty', 12)
print(obj.name)
print(obj.get_age()) #через метод можно вытащить приватный атрибут
# Nasty
# 12
obj.set_age(45)
print(obj.get_age())
# 45
obj.set_age(125)
print(obj.get_age())
# Exception: Invalid age - так как возраст больше 120
```

## Property
> декоратор, который превращает метод в атрибут с декораторами getter, setter, deleter

> setter - будет вызываться, когда мы записываем в атрибут новое значение
> deleter - будет вызываться, когда мы удаляем атрибут через del