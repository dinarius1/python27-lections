"==================================Ассоциация==================================="
# Ассоциация - принцип ООП, в котором два класса друг с другом связаны
# ассоциация делится на 2 принципа:
# 1 - агрегация (более слабая связь)
# 2 - композиция (более сильная связь)

class Battery:
    power = 100

    def charge(self):
        if self.power <100:
            self.power = 100

class Iphone:
    def __init__(self,color):
        self.color = color
        self.battery = Battery()  #self.battery - теперь тоже явл объектом класса Battery()
        # когда мы создаем объект от другого класса прям внутри другого класса - композиция
        # в данном случае у нас композиция, где свяь более сильная, так как телефон не может быть без батарейки



iphone = Iphone('золотой')
print(iphone.battery)
#<__main__.Battery object at 0x7fde75b57b80> - выходит сам класс
print(iphone.battery.power)   #100
#через точку обратились к атрибуту класса

del iphone #уже не можем отдельно вытащить батарейку
#объект батарейки удаляется вместе с объектом iphone

class Nokia:
    def __init__(self, color, battery):
        self.color = color
        self.battery = battery
        # когда мы принимаем уже созданный вне класса объект - агрегация, более слаюая связь

battery = Battery()

nokia = Nokia('черный', battery= battery)  # 1 battery - это локальная переменная, является параметром из инита, 2 battery - это переменная из глобального пространства, т.е вот это battery = Battery()

print(nokia.battery.power)   #100

del nokia
#удаляется только объект nokia, но объект батарейки существует

print(battery.power)  #батарейка может существовать без телефона, ведь battery = Battery() - также самостоятельная переменная 


