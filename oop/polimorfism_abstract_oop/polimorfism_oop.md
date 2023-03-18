# Полиморфизм
> принцип ООП, в котором методы в разных классах называются олинаково. (один интерфейс - разная реализация)
```py
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
```