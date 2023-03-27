'''
Задание 10

    Необходимо написать класс Game у которого есть приватный атрибут класса "level" который равен нулю и атрибут экземпляра класса name (ваше имя).
    Класс Game должен иметь методы для увеличения уровня игры (play) и получения текущего уровня (get_level).
    Метод play принимает в себя переменную hours и проверяет если значение этой переменной больше двух то уровень игры увеличивается на единицу иначе ничего не происходит. Так как атрибут класса "level" приватный и поэтому недоступен извне, необходимо реализовать метод "get_level" который возвращает значение атрибута "level".
    Создайте экземпляр "game" класса Game. Выведите на экран значение атрибута "level" затем два раза используйте метод play чтобы уровень игры поднялся на два, после снова выведите на экран значение атрибута "level".

'''
class Game:
    __level = 0
    def __init__(self, name):
        self.name = name

    def play(self, hours):
        if hours > 2:
            self.__level += 1
        else:
            return None
    
    def get_level(self):
        return self.__level

game = Game('Mario')
print(game.get_level())
game.play(3)
game.play(5)
print(game.get_level())

class Game: 
    __level = 0
    def __init__(self,name): 
        self.name = name 
    
    def play(self,hours): 
        if hours > 2: 
            self.__class__.__level += 1 #почему надо пистаь так??
    
    def get_level(self): 
        return self.__class__.__level 
    
game = Game("Juan") 
print("Initial level:", game.get_level()) 
game.play(3) 
game.play(5) 
print("Final level:", game.get_level())