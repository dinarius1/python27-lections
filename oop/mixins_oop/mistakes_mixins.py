'''
Задание 2
Создайте класс-миксин RadioMixin, и реализуйте в нем метод для проигрывания музыки play_music, который принимает в переменную title название песни.

Метод должен печатать строку "Песня называется title", где вместо title должно быть переданное название песни.

Создайте класс Auto, Boat, Amphibian и расширьте функционал этих классов при помощи миксина. Класс Amphibian также как в предыдущем задании должен наследоваться от классов Auto и Boat. Создайте экземпляры auto, boat и obj от трех классов и примените метод play_music.
'''
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

'''
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

'''
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