## Задание 1

Создайте класс для песен Song. Каждая песня имеет название - title, автора - author и год выпуска - year.

Добавьте три метода:

    show_author

    show_title

    show_year

выводящие утверждения о каждом атрибуте экземпляра класса Song.

Создайте экземпляр song класса Song с вашей любимой песней и примените все методы.

Например:

song.show_title()
song.show_author()
song.show_year()

Вывод:

Название этой песни Happy
Автор этой песни Pharrell Williams
Эта песня вышла в 2013 году
```py
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
```

## Задание 2

Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, в переменной color, и число Пи(3.14) - в переменной pi.

Экземпляры класса Circle в свою очередь должны иметь обязательное свойство - радиус, в переменной radius.

К примеру, создадим объект с радиусом 2:

circle = Circle(2) 

Также, класс должен иметь метод расчета площади круга - get_area():

circle.get_area() 

Возвращает:

12.56 

    формула расчета площади: число Пи умножить на радиус в квадрате

    cоздайте экземпляр класса,
    переопределите цвет экземпляра и
    примените метод get_area().

Распечатывать результат не нужно, методы должны возвращать результат ключевым словом return.

```py
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
```
## Задание 3

Создайте класс BankAccount, у объектов данного класса есть аттрибут balance со значением по умолчанию 0: balance = 0.

Определите метод withdraw с параметром amount, который будет отнимать сумму от баланса и распечатывать текущий баланс.

Добавьте еще один метод deposit, который также имеет параметр amount и соответсвенно добавляет сумму к балансу и распечатывает баланс.

Например:

account.deposit(1000) 
account.withdraw(500) 

Получим такой вывод:

Ваш баланс: 1000 сом 
Ваш баланс: 500 сом 

в начале, увеличили переменную balance на 1000, затем уменьшили на 500, и получили в итоге 500.

```py
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
```
Введение в ООП.
## Задание 4

Создайте класс Taxi, объекты которого имеют такие атрибуты как название компании - name, стоимость посадки - cost, стоимость за каждый пройденный километр - cost_km.

Добавьте к классу метод get_total_cost, принимающий параметр km - сколько километров составила поездка и возвращающий стоимость поездки.

Создайте три экземпляра класса Taxi для трех разных компаний Namba, Yandex и Jorgo и расчитайте стоимость поездки на каждой из них.

Например:

print(taxi1.get_total_cost(10)) 
print(taxi2.get_total_cost(6)) 
print(taxi3.get_total_cost(14))  

Вывод:

Такси Namba, стоимость поездки: 179 сом 
Такси Yandex, стоимость поездки: 127 сом 
Такси Jorgo, стоимость поездки: 238 сом  

```py
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
```
## Задание 5

Создайте класс телефонной книги Phone. У контактов должны быть такие аттрибуты:

    name - имена
    last_name - фамилии
    phone - телефонные номера

Добавьте метод get_info, который выводит информацию о контакте в следующем виде:

contact.get_info()

Вывод в терминал:

Контакт: John Snow, телефон: +996707707707

Затем, создайте объект от класса Phone в переменной contact и примените метод get_info

```py
class Phone:
    def __init__(self, name, last_name, phone):
        self.name = name
        self.last_name = last_name
        self.phone = phone
    def get_info(self):
        print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')
contact = Phone('John', 'Snow', '996707707707')
contact.get_info()
```
## Задание 6

Напишите класс Salary для расчета налогов на заработную плату. У класса должна быть обязательная переменная класса - percent = 8, обозначающий процент налога на ежемесячную зарплату - 8%.

Объекты класса должны иметь, в качестве атрибутов сумму зарплаты salary и стаж работы в месяцах - experience.

Также у класса должен быть метод count_percent, расчитывающий сумму налога заплаченного за весь стаж работы.

Создайте экземпляр класса obj и посчитайте сумму вашего налога.

К примеру, если у вашего объекта salary имеет значение 10000, а experience равен 10, то:

print(obj.count_percent()) 

Выдаст вам такой результат в терминале:

8000.0 

Каждый месяц с зарплаты в 10000 сомов снимается 8% на налоги, т.е 800 сом, за 10 месяцев трудового стажа эта сумма будет 8000.0 сом

```py
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
```

## Задание 7

Вам дан такой код:

winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
print(winner1.category, winner1.year, winner1.winner) 
print(winner1.get_year())

  
winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
print(winner2.category, winner2.year, winner2.winner) 
print(winner2.get_year())

который выводит в терминал такие значения:

Литература 1971 Пабло Неруда
выиграл 51 лет назад 
Литература 1994 Кэндзабуро Оэ 
выиграл 28 лет назад

Напишите класс Nobel, который будет принимать аттрибуты category, yearи winner. Создайте метод get_year(), который будет выводить сколько лет назад была получена премия в виде 'выиграл {кол-во лет} лет назад'.

    Дату сколько лет назад была получена премия в методе get_year() не вписывать вручную, а высчитывать используя datetime

```py
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
```

## Задание 8

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

```py
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
```

## Задание 9

Создайте класс Math, у экземпляра которого должно быть свойство number. У классa Math должно быть 3 метода:

    get_factorial - возвращает факториал числа(перемножить все составные числа до самого числа)

    get_sum - возвращает сумму цифр числа

    get_mul_table - возвращает таблицу умножения для числа до 10 в формате:

5x1=5
5x2=10
5x3=15
5x4=20
5x5=25
5x6=30
5x7=35
5x8=40
5x9=45
5x10=50

Создайте экземпляр класса и примените к нему все методы.

Например, если экземпляром класса Math является число 11,

вызов get_factorial возвратит такой результат:

39916800 

т.к 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 x 9 x 10 x 11 = 39916800

метод get_sum, возвратит:

2 

т.к число 11 состоит из двух цифр 1 и 1, сумма 1 + 1 = 2

метод get_mul_table возвратит:

11 x 1 = 11 
11 x 2 = 22 
11 x 3 = 33 
11 x 4 = 44 
11 x 5 = 55 
11 x 6 = 66 
11 x 7 = 77 
11 x 8 = 88 
11 x 9 = 99 
11 x 10 = 110 

    результат методов возвращайте ключевым словом return, print() использовать не надо.

> Тут хорошо показано, как возможно включать элементы в строку, сохраняя прошлый результат и все в рамках функции!!! - весьма интересный вариант
```py
class Math:
    def __init__(self, number):
        self.number = number

    def get_factorial(self):
        res = 1
        for i in range(1, int(self.number) + 1):
            res *= i
        return res
    
    def get_sum(self):
        if len(str(self.number)) == 3:
            one = int(self.number) // 100
            two = int(self.number) // 10 % 10
            three = int(self.number) % 100 % 10
            summary = one + two + three
            return summary
        else:
            one = int(self.number) // 10
            two = int(self.number) % 10
            summary = one + two
            return summary
    
    def get_mul_table(self):
        table = ''
        for i in range(1,11):
            res = int(self.number) * i
            table = table + f'{self.number} x {i} = {res}' + '\n'
        return table

n = Math(106)
print(n.get_factorial())
print(n.get_sum())
print(n.get_mul_table())
```

> НО! Это наилучший вариант, если можно использовать print при вызове метода!!! Тут мы именно будем по порядку вызывать каждую нашу строку из таблицы умножения, и это выглядит красиво и лаконично
```py
    def get_mul_table(self):
        table = []
        for i in range(1,11):
            res = int(self.number) * i
            print(f'{self.number} x {i} = {res}')
```