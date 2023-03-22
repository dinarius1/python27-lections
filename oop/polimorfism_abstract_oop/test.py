'''
Таск 8

Создайте классы Mercury, Venus, Jupiter, которые наследуют метод __init__ от родительского класса Planet. У объектов данного класса должен быть аттрибут orbit, орбита в классе Venus состовляет 225 земных дней, Mercury 88 земных дней, а на Jupiter 12 дней. У всех этих классов должен быть метод get_age, принимающий возраст в переменную earth_age и расчитывающий ваш возраст на данной планете.

Метод должен возвращать возраст на Mercury в годах, на Venus в днях и на Jupiter в часах. Например, если возраст earth_age равен 20:

на Венере ваш возраст составляет 11842 дней
на Юпитере ваш возраст составляет 5326080 часов
на Меркурии ваш возраст составляет 82 лет
'''
class Planet: 
    def __init__(self, orbit): 
        self.orbit = orbit 

class Mercury(Planet): 
    def get_age(self, earth_age): 
        return f'на Меркурии ваш возраст составляет {int(earth_age * 365 /self.orbit)} лет' 

class Venus(Planet): 
    def get_age(self, earth_age): 
        return f'на Венере ваш возраст составляет {round(earth_age * 365 / self.orbit * 365)} дней' 

class Jupiter(Planet): 
    def get_age(self, earth_age): 
        return f'на Юпитере ваш возраст составляет {round(earth_age * 365 // self.orbit * 365 * 24)} часов' 

mercury = Mercury(88) 
venus = Venus(225) 
jupiter = Jupiter(12) 
print(venus.get_age(20)) 
print(jupiter.get_age(20))
print(mercury.get_age(20))