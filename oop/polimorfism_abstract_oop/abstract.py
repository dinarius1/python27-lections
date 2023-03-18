from abc import ABC, abstractmethod

class AbstractAnimal(ABC):  #лучше называть Абстракцию при создании абстрактного класса лучше писать Abstract
    @abstractmethod  #декоратор, который вызывает ошибку, если мы непреопределили метод из Абстрактного класса в новый класс при его создании
    def speak(self):
        pass
class Dog(AbstractAnimal):
    pass

# obj = Dog()
# TypeError: Can't instantiate abstract class Dog with abstract method speak

class Dog(AbstractAnimal):
    def speak(self):
        print('гав-гав')

obj = Dog()
obj.speak()
# гав-гав