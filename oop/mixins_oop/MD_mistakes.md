## Задание 1

Создайте класс Auto в нем реализуйте метод ride который выводит сообщение 'Riding on a ground'.

Создайте класс Boat реализуйте метод swim, который выводит 'Floating on water'.

Создайте класс Amphibian который наследуется от класса Auto и Boat.

Создайте от него объект obj и вызовите все методы.

Ввод:

obj = Amphibian() 
obj.ride() 
obj.swim() 

Вывод:

Riding on a ground 
Floating on water 

```py
class Auto:
    def ride(self):
        print('Riding on a ground')
class Boat:
    def swim(self):
        print('Floating on water')
class Amphibian(Auto,Boat):
    pass
obj = Amphibian() 
obj.ride() 
obj.swim() 
```

## Задание 2

Создайте класс-миксин RadioMixin, и реализуйте в нем метод для проигрывания музыки play_music, который принимает в переменную title название песни.

Метод должен печатать строку "Песня называется title", где вместо title должно быть переданное название песни.

Создайте класс Auto, Boat, Amphibian и расширьте функционал этих классов при помощи миксина. Класс Amphibian также как в предыдущем задании должен наследоваться от классов Auto и Boat. Создайте экземпляры auto, boat и obj от трех классов и примените метод play_music.
```py
class RadioMixin:
    def play_music(self, title):
        title
        print(f"Песня называется {title}")

class Auto(RadioMixin):
    def ride(self):
        print('Riding on a ground')
class Boat(RadioMixin):
    def swim(self):
        print('Floating on water')
class Amphibian(Auto,Boat): #это гидросамолет, то есть тоже транспорт
    pass

auto = Auto()
boat = Boat()
obj = Amphibian()
auto.play_music('1')
boat.play_music('2')
obj.play_music('3')
```

## Задание 3

Будильник. Создайте класс Clock, у которого будет метод current_time показывающий текущее время и класс Alarm, с методами on и off для включения и выключения будильника.

Далее, создайте класс AlarmClock, который наследуется от двух предыдущих классов.

Добавьте к нему метод alarm_on для установки будильника, при вызове которого должен включатся будильник.

Создайте экземпляр clock класса AlarmClock и примените к ниму методы current_time и alarm_on.

Ввод должен быть:

clock.current_time() 
clock.alarm_on() 

С выводом:

17:10:41 
Будильник включен 

```py
import datetime
t = str(datetime.datetime.now()).split()[1].split('.')[0]
print(t)
class Clock:
    def current_time(self):
        print(t)
class Alarm:
    def on(self):
        print('Будильник включен')
    def off(self):
        print('Будильник выключен')
class AlarmClock(Clock, Alarm):
    def alarm_on(self):
        super().on()
clock = AlarmClock()
clock.current_time
clock.alarm_on() 
```

## Задание 4

Напишите абстрактный класс Coder с атрибутом класса count_code_time = 0 и абстрактными методами get_info и coding.

Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder.

Класс Backend должен принимать дополнительно параметры experience и languages_backend, а Frontend такие параметры как — experience и languages_frontend соответственно.

Переопределите в обоих классах методы get_info и coding так, чтобы он принимал количество часов кодинга и при каждом вызове этого метода добавлял это значение к count_code_time.

Также бывают Fullstack разработчики, поэтому создайте данный класс так чтобы у него были атрибуты и методы предыдущих классов. При этом нее определяйте никаких методов и атрибутов в данном классе он должен наследовать их от родительских классов.

Создайте экземпляры a, b, c от классов Backend, Frontend, Fullstack соответственно и вызовите их методы.

Ввод должен быть:

a.coding(12) 
b.coding(45) 
c.coding(17) 
print(a.get_info()) 
print(b.get_info()) 
print(c.get_info()) 

Вывод:

Python разработчик, уровень: Junior, потрачено 12 часов на программирование

Javascript разработчик, уровень: Middle, потрачено 45 часов на программирование

Python and JS разработчик, уровень: Senior, потрачено 17 часов на программирование 

```py
from abc import ABC, abstractmethod
class AbstractCoder(ABC):
    count_code_time = 0
    @abstractmethod
    def get_info():
        pass

    @abstractmethod
    def coding():
        pass

class Backend(AbstractCoder):
    def __init__(self, languages_backend, experience):
        self.experience = experience
        self.languages_backend = languages_backend
        
    def coding(self, count_code_time):
        self.count_code_time += count_code_time
        return self.count_code_time
    def get_info(self):
        return f'{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'

class Frontend(AbstractCoder):
    def __init__(self, languages_frontend, experience):
        self.experience = experience
        self.languages_frontend = languages_frontend 
    
    def coding(self, count_code_time):
        self.count_code_time += count_code_time
        return self.count_code_time
    
    def get_info(self):
        return f'{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'

class Fullstack(Frontend, Backend):
    def __init__(self, languages_frontend, experience):
        super().__init__(languages_frontend, experience)
    
    def coding(self, count_code_time):
        return super().coding(count_code_time)
    
a = Backend('Python', 'Junior')
b = Frontend('Javascript', 'Middle')
c = Fullstack('Python and JS разработчик', 'Senior')

a.coding(12) 
b.coding(45) 
c.coding(17) 
print(a.get_info()) 
print(b.get_info()) 
print(c.get_info()) 
```
> когд в задании пишут, что надо создать абстрактный класс, то имеется в виду надо создать некий класс-пустышку, от которого нельзя будет создавать экземпляры, но можно булет наследоваться. А САМОЕ ГЛАВНОЕ, что данный класс требует от дочерних от него классов создавать методы, которые были прописаны в этом классе-пустышки

> однако для этого надо будет импортировать метод abstractmethod и потом его задекорировать

## Задание 5

Создайте два класса: Square и Triangle.

Класс Square должен иметь атрибуты: side - длина стороны квадрата.

Класс Triangle должен иметь аттрибуты: height - высота, base - длина.

У каждого из вышеуказанных классов должен быть метод get_area, который высчитывает и возвращает площадь - результатом должно быть целое число.

Создайте третий класс Pyramid который наследуется от первых двух классов, init унаследуйте от Triangle, дополнительные аттрибуты присваивать нельзя.

Добавьте метод get_volume для расчета объема пирамиды(формула: 1/3 x основание^2 x высоту), метод должен возвращать целое число.

```py
class Square:
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side 

class Triangle:
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def get_area(self):
        return 1/2 * self.base * self.height

class Pyramid(Triangle, Square):
    def __init__(self,height, base):
        super().__init__(height, base)
    
    def get_volume(self):
        
        return int(1/3 * self.base **2 * self.height)

p = Pyramid(10,10)
print(p.get_volume())

```