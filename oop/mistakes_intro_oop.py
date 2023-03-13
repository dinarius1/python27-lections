#Task 1
class Song:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def show_title(self):
        return(f'Название этой песни {self.title}')

    def show_author(self):
        return(f'Автор этой песни{self.author}')

    def show_year(self):
        return(f'Эта песня вышла в {self.year} году')

song =Song("Happier than ever", "Billie Elish", 2021)
print(song.show_title())
print(song.show_author())
print(song.show_year())

#Task 2
class Circle:
    color = 'Синий'
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        res = Circle.pi * (self.radius) ** 2
        return res
circle = Circle(2)
circle.color = 'красный'
print(circle.color)
print(circle.get_area())

#Task 3

class BankAccount:
    def __init__(self): 
       self.balance = 0 
    def withdraw(self, amount):
        self.balance -= amount
        print(f'Ваш баланс: {self.balance} сом')
    def deposit(self, amount):
        self.balance += amount
        print(f'Ваш баланс: {self.balance} сом')
account = BankAccount()
account.deposit(1000)
account.withdraw(500)

#Task 4
class Taxi:
    def __init__(self, name, cost, cost_km):
        self.name = name
        self.cost = cost
        self.cost_km = cost_km
    def get_total_cost(self, km):
        self.all_cost = self.cost + (self.cost_km * km)
        return f'Такси {self.name}, стоимость поездки: {self.all_cost} сом'
taxi1 = Taxi('Namba', 79, 10)
taxi2 = Taxi('Yandex', 27, 5)
taxi3 = Taxi('Jorgo', 138, 15)

print(taxi1.get_total_cost(10)) 
print(taxi2.get_total_cost(6)) 
print(taxi3.get_total_cost(14))

#Task 5
class Phone:
    def __init__(self, name, last_name, phone):
        self.name = name
        self.last_name = last_name
        self.phone = phone
    def get_info(self):
        print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')
contact = Phone('John', 'Snow', '996707707707')
contact.get_info()

#Task 6
class Salary:
    percent = 8
    def __init__(self, salary, experience):
        self.salary = salary 
        self.experience = experience 
    def count_percent(self):
        res = ((self.salary  * self.percent) / 100) * self.experience
        return res
obj = Salary(10000, 10)
print(obj.count_percent()) 

#Task 7
import datetime
now = datetime.datetime.now()
now2 = str(now).split()[0].split('-')[0]
date_now = int(now2)

class Nobel:
    def __init__(self, category, year, winner):
        self.category = category 
        self.year = year
        self.winner = winner
    def get_year(self):
        return f'выиграл {date_now - self.year} лет назад'
winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
print(winner1.category, winner1.year, winner1.winner) 
print(winner1.get_year())

  
winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
print(winner2.category, winner2.year, winner2.winner) 
print(winner2.get_year())

'''
Задание 8

Создайте класс Password, экземеплярами класса являются пароли в виде строк. У класса должен быть метод validate для валидации пароля:

    В начале, проверьте, что пароль состоит из минимум 8 символов, но меньше 15, если условие не соблюдено, должны выйти ошибка с текстом:

Password should be longer than 8, and less than 15

    Вторая проверка должна проверять что пароль содержит цифры, и в случае отсутствия цифр, выводить ошибку с текстом:

Password should contain numbers too

    Третья проверка, проверяет содержит ли пароль буквы и в случае не совпадения, выводит ошибку с текстом:

Password should contain letters as well

    В конце проверьте, содержит ли пароль хотя бы один из символов: '@', '#', '&', '$', '%', '!', '~', '*', если условие не выполнено выводите ошибку с текстом:

Your password should have some symbols

если одно из условий не выполнено, выводите соответствующее исключение, если же все условия выполнены метод validate должен возвращать строку:

Ваш пароль сохранен.

Также переопределите метод __str__, чтобы при попытке распечатать сам пароль, вам выдавалась строка из звездочек количество которых равно длине пароля.

К примеру, если пароль joe@123456, при попытке распечатать пароль, в терминал должно выводиться: **********

    пишите код для проверки пароля в указанном порядке

'''

class Password:
    def __init__(self, password):
        self.password = password

    def validate(self):
        res = 15 > len(self.password) > 8
        res2 = [el for el in list(self.password) if el.isdigit()]
        res3 = [el for el in list(self.password) if el.isalpha()]
        list_symbols = ['@', '#', '&', '$', '%', '!', '~', '*',]
        res4 = [s for s in list_symbols if s in self.password]

        if bool(res) == False:
            print('Password should be longer than 8, and less than 15')
        
        elif len(res2) == 0:
            print('Password should contain numbers too')
        
        elif len(res3) == 0:
            print('Password should contain letters as well')
    
        elif len(res4) == 0:
            print('Your password should have some symbols')
        else:
            return 'Ваш пароль сохранен.'
    def __str__(self):
        res5 = ''
        for el in self.password:
            res5 = res5 + '*' 
        return res5

p = Password('12345678q!#')
print(p.validate())
print(p)

# self = 'kasdkjas@#'
# list_symbols = ['@', '#', '&', '$', '%', '!', '~', '*',]
# # el for el in list(self) 

# print(res4)
# if '@'or '#' or '&'or '$' or '%' or '!' or '~' or '*' not in self:
#     print('Your password should have some symbols')
# self = 'kasdkjas'
# r = list(self)
# rr = []
# for el in r:
#     if el.isdigit():
#         rr.append(el)
# print(len(rr))


# res2 = [el for el in self if int(el) == type(1)]
# print(res2)

# self = 10
# res = 15 > self > 8
# res = self > 8 and self < 15


