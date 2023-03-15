# Абстракция
> Абстракция - это принцип ООП, в котором создается класс-пустышка, в котором указываются названия методов, которые обязательно нужно реализовать при создании дочернего класса

> Чтобы реализовать абстракцию, нужно испортировать abc и наследовать от класса ABC, и нужные методы декорируем в abstractmethod
```py
from abc import ABC, abstractmethod

class AbstractAnimal(ABC):  #лучше называть Абстракцию при создании абстрактного класса лучше писать Abstract
    @abstractmethod  #декоратор, который вызывает ошибку, если мы непреопределили метод из Абстрактного класса
    def speak(self):
        pass
class Dog(AbstractAnimal):
    pass

obj = Dog()
# TypeError: Can't instantiate abstract class Dog with abstract method speak

class Dog(AbstractAnimal):
    def speak(self):
        print('гав-гав')
```