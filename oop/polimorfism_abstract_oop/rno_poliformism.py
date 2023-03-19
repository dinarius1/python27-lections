'''
Задание 2

Создайте классы Dog и Cat с одинаковым методом voice.

Для собак он должен печатать "Гав", для кошек "Мяу".

Объявите для каждого из классов по экземпляру, для класса Cat экземпляр в переменной barsik, а для Dog экземпляр rex.

Затем, вне класса объявить функцию to_pet(), которая будет принимать животное и вызывать у него метод voice().

Ввод:

to_pet(barsik) 
to_pet(rex) 

Вывод:

Мяу 
Гав 
'''

class Dog:
    def voice(self):
        print('Гав')
class Cat:
    def voice(self):
        print('Мяу')

def to_pet(animal):
    if isinstance(animal, Dog):
        Dog().voice()
    else:
        Cat().voice()
    
rex = Dog()
barsik = Cat()
to_pet(barsik) 
to_pet(rex) 

'''
Создайте 3 класса: Person с параметрами name и last_name, Employee с work и status, Student c university и course, при этом Employee и Student должны наследоваться от Person.

Определите во всех трёх классах метод get_info():

    для класса Person он должен возвращать следующее: “Привет, меня зовут Иван Петров”.

    для класса Employee он должен возвращать: “Привет, меня зовут Иван Петров, я работаю в компании Рога и копыта на должности директор.

    для класса Student должно возвращаться: “Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе”.

Вне класса, определите функцию get_human_info(), которая будет принимать объект одного из трёх классов и вызывать у него метод get_info и распечатывать результат этой функции.

Создайте для каждого класса по экземпляру, для Person экземпляр person, для Employee экземпляр employee и student для класса Student.

Вызовите метод get_human_info у каждого экземпляра печатать результат.

Ввод должен быть:

get_human_info(employee) 
get_human_info(student) 
get_human_info(person) 

Вывод:

Привет, меня зовут Иван Петров, я работаю в компании Рога и Копыта на должности директор 
Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе 
Привет, меня зовут Иван Иванов 

'''

class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
    
    def get_info(self):
        print(f'Привет, меня зовут {self.name} {self.last_name}')


class Employee(Person):
    def __init__(self, name, last_name, work, status):
        super().__init__(name, last_name)
        self.work = work
        self.status = status

    def get_info(self):
        print(f'Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}')

class Student(Person):
    def __init__(self, name, last_name, university, course):
        super().__init__(name, last_name)
        self.university = university
        self.course = course
    
    def get_info(self):
        print(f'Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе')

def get_human_info(human):
    if isinstance(human, Employee):
        human.get_info()
    elif isinstance(human, Student):
        human.get_info()
    elif isinstance(human, Person):
       human.get_info()


person = Person('Азамат', 'Айталиев')
employee = Employee('Азамат', 'Айталиев', 'The Most', 'официант')
student = Student('Азамат', 'Айталиев', 'КГЮА', 1)
get_human_info(person)
get_human_info(employee)
get_human_info(student)