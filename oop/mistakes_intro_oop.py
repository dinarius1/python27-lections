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