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

