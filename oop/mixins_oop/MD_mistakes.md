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

#или можно так
from datetime import datetime
class Clock:
    def current_time(self):
        print(datetime.now().strftime('%H:%M:%S'))
c = Clock()
print(c.current_time())
```
> strftime('%H:%M:%S') - это специальная конструкция, которая позволяет вытаскивать время в правильном формате

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
## Задание 6

Создайте класс ToDo, с аттрибутом класса, в виде словаря todos = {}.

У класса должен быть один метод set_deadline, который принимает дату дедлайна (в виде "31/12/2021") и возвращает количество дней оставшихся до дедлайна.

Также, класс ToDo должен наследоваться от четырех миксинов: CreateMixin, DeleteMixin, UpdateMixin, ReadMixin:

    в классе CreateMixin определите метод create, который принимет в себя задачу todo и ключ key по которому нужно добавить задачу в словарь todos, если ключ уже существует верните "Задача под таким ключом уже существует".

    класс DeleteMixin должен содержать метод delete, который удаляет задачу по ключу key, который передается как аргумент, и возвращает сообщение 'удалили название задачу', где вместо слова название должно быть название задачи.

    класс UpdateMixin должен содержать метод update, который принимает в себя ключ key и новое значение new_value и заменяет задачу под данным ключом на новое значение.

    класс ReadMixin должен содержать метод read, который возвращает отсортированный список задач.

```py
import datetime
now_1 = datetime.date.today()
# print(now_1)

class CreateMixin:
    def create(self, key, todo):
        model = self.__class__   #теперь в model - класс ProductCrud
        obj = model()
        obj.todo = todo
        if key not in model.todos.keys():
            model.todos[key] = obj.todo
            return model.todos
        return "Задача под таким ключом уже существует"

class DeleteMixin:
    def delete(self, key):
        model = self.__class__   #теперь в model - класс ProductCrud
        obj = model()
        popped = model.todos.pop(key)
        return popped
        # return f"удалили {popped}"
    
class UpdateMixin:
    def update(self, key, new_value):
        model = self.__class__   #теперь в model - класс ProductCrud
        obj = model()
        obj.new_value = new_value
        model.todos[key] = new_value
        return model.todos
    
class ReadMixin:
    def read(self):
        model = self.__class__   #теперь в model - класс ProductCrud
        obj = model()
        return sorted(model.todos.items())


class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
    todos = {}
    def set_deadline(self,date):
        res2 = date.split('/')
        res2 = list(reversed(res2))
        #мы просим, чтобы нам вышел результат в обратном порядке (res2 - имеет тип даных - список), поэтомы он просто считывает ее задом наперед
        res2 = [int(i) for i in res2]
        res3 = datetime.date(res2[0], res2[1], res2[2])
        #вытаскиваем именно дату, и задаем каждый элемент какое то место в дате
        tdelta = now_1 - res3 
        #у тип данных datetime мы можем найти интервал между датами через tdelta, даже не импортируя timedelta, так как к ним можно использовать оператор "-"
        return tdelta.days
      
task = ToDo()

print(task.create(1, 'Do housework'))
print(task.create(1, 'Do housework'))
print(task.create(2, 'Go for a walk'))
print(task.update(1, 'Do homework'))
print(task.delete(2))
print(task.read())
print(task.set_deadline('31/12/2021')) #выходит все время 443, а не -443, как хочет платформа
print(task.todos)
```
> now_1 = datetime.date.today() - здесь мы пытаемся вытащить именно сегодняшний день с помощью встроенного метода date, у которого есть метод today()

> используем переменную model = self.__class__ , чтобы в model был класс ProductCrud. Т.е мы говорим, что нам нужно найти класс от обекта c помощью магического метода __class__

> в Миксине ридинг return sorted(model.todos.items()) - 296 строка, к словарям мы можем использовать функцию sorted(), он будет сортировать наш словарь по ключам. А чтобы выходил и ключ и значение элементов, то нужно использовать items, который возвращает кортеж

> посмотри комментарии в последнем блоке кода

## Задание 7

Напишите класс Game, с помощью которого можно создать объекты-игры, у объектов должны быть атрибуты:

    type_ - тип игры
    name - название игры,
    extensions соответсвующий пустому списку - [].

У класса должны быть методы:

    get_description, который принимает строку и возвращает описание к игре в виде названия игры и переданной строки:

Minecraft это инди-игра в жанре песочницы с элементами выживания и открытым миром. 

Где Minecraft - это название игры, берется из атрибута name объекта.

    get_extensions, который возвращает все подключенные расширения в виде строки разделенной пробелами, если же список extensions пуст, возвращайте сообщение:

Нет подключенных расширений   

Также напишите миксин ExtensionMixin, чтобы к игре можно было подключать расширения.

У миксина должно быть два метода:

    add_extension, принимающий строку-название и добавляющий ее в список игры, также должен возвратить сообщение:

Добавлено новое расширение Multiverse-Core для игры Minecraft. 

где Multiverse-Core это строка - название расширения

    remove_extension, удаляющий расширение по названию, и возращающий строку в формате:

Multiverse-Core был отключен от Minecraft. 

Если же такого расширения нет в списке должна возвращаться строка:

Такого расширения нет в списке.

```py
class ExtensionMixin: 
    def add_extension(self, extension): 
        self.extensions.append(extension) 
        return f'Добавлено новое расширение {extension} для игры {self.name}.'
    
    # как мы смогли сослаться на self.extensions, если наш класс не наследуется от класса Game? Разве не надо было использовать module как с CRUD? 

    def remove_extension(self, deleted_game):
        if deleted_game in self.extensions:
            self.extensions.remove(deleted_game)
            return f'{deleted_game} был отключен от {self.name}'
        return 'Такого расширения нет в списке.'
    
class Game(ExtensionMixin): 
    def __init__(self, type, name): 
        self.type = type 
        self.name = name 
        self.extensions = [] 
        
    def get_description(self):
        description = f'{self.type} в жанре песочницы с элементами выживания и открытым миром'
        return f"{self.name} это {description}"
    
    def get_extensions(self): 
        res = ' '.join(self.extensions)
        if len(res) == 0:
           return 'Нет подключенных расширений'
        return res

g = Game('инди игра', "Minecraft")
print(g.get_description())
print(g.add_extension('Tekken'))
print(g.add_extension('Mario'))
print(g.get_extensions())
print(g.remove_extension('Tekken'))
print(g.get_extensions())
```
> в Миксинах мы можем ссылаться на объект дочернего класса, так как объект от дочерних классов явл экземпляром не толлько от дочернего класса, но также и от класса-миксина, поэтому фактически в нашем блоке класса Game лежит весь блок ExtensionMixin

> Возможен и такое форматирование description = f'{self.type} в жанре песочницы с элементами выживания и открытым миром'

## Таск 8

Создайте класс WalkMixin с методом walk, который будет выводить "я могу ходить"

Создайте класс FlyMixin с методом fly, который будет выводить "я могу летать"

Создайте класс SwimMixin с методом swim, который будет выводить "я могу плавать"

    Создайте класс Human, который будет наследоваться от миксинов WalkMixin и SwimMixin
    Создайте класс Fish, который будет наследоваться от миксина SwimMixin
    Создайте класс Exocoetidae, который будет наследоваться от миксинов FlyMixin и SwimMixin
    Создайте класс Duck, который будет наследоваться от всех 3 миксинов

Создайте обьекты от классов Human, Fish, Exocoetidae, Duck и вызовите методы, которые у них есть от миксинов

```py
class WalkMixin:
    def walk(self):
        print("я могу ходить")

class FlyMixin:
    def fly(self):
        print("я могу летать")

class SwimMixin:
    def swim(self):
        print("я могу плавать")

class Human(WalkMixin, SwimMixin):
    pass

class Fish(SwimMixin):
    pass

class Exocoetidae(FlyMixin, SwimMixin):
    pass

class Duck(WalkMixin, SwimMixin, FlyMixin):
    pass

human = Human()
human.walk()
human.swim()

fish = Fish()
print(fish.swim())

fly_fish = Exocoetidae()
fly_fish.swim()
fly_fish.fly()

duck = Duck()
duck.swim()
duck.fly()
duck.walk()
```