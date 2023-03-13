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

# song =Song("Happier than ever", "Billie Elish", 2021)
# print(song.show_title())
# print(song.show_author())
# print(song.show_year())

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


