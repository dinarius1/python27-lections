# Task 3
class MyString(str):
    def __init__(self, name):
        self.name = name
        self.name = name
    def append(self, word):
        self.word = word
        self.name = self.name + self.word
        return self.name
    def pop(self):
        char = self.name[-1]
        self.name = self.name[:-1]
        return char
    def __str__(self):
        return self.name


example  =  MyString('String') 
print(example.append('hello'))
print(example.pop()) 
print(example)

# Task 4
class MyDict(dict):
    def __init__(self, dict_):
        self.dict_ = dict_
    def get(self, key):
        if self.dict_.get(key) == None:
            return 'Are you kidding?'
        return self.dict_.get(key)

obj_dict = MyDict({'some_title': 2}) 
print(obj_dict.get('some')) 

# Task 5
'''
Создайте класс Person который будет описывать человека, а точнее его имя - name и возраст - age. Добавьте к классу метод display(), который будет выводить данные об этом человеке.

Создайте второй класс Student, который будет наследоваться от класса Person.

Объекты от класса Student должны иметь все атрибуты, которые были определены в родительском классе и еще один дополнительный атрибут - faculty, который будет описывать факультет, где учится студент.

Создайте метод display_student(), который будет выводить данные об этом студенте.

Создайте от класса Student объект в перемнной obj_student, и выведите данные о нём, как о человеке, затем как о студенте.

Например, применим методы к объекту obj_student:

obj_student.display() 
obj_student.display_student() 

допустим, у нашего объекта в атрибуте name хранится значение Rick, в age - 21, а в faculty значение science, вывод в терминал должен быть:

name:Rick, age:21 
name:Rick, age:21, faculty:science 

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f'name:{self.name}, age:{self.age}')
    
class Student(Person):
    def __init__(self, name, age, faculty):
        super().__init__(name, age)
        self.faculty = faculty 

    def display_student(self):
        print(f'name:{self.name}, age:{self.age}, faculty:{self.faculty}')
obj_student = Student('Rick', 21, 'science')
obj_student.display() 
obj_student.display_student() 