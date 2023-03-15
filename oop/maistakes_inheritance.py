# Task 3
class MyString(str):
    def __init__(self, name):
        self.name = name
    def append(self, word):
        self.word = word
        self.name = self.name + self.word
        return self.name
    def pop(self):
        char = self.name[-1]
        self.name = self.name[:-1]
        return char
    def __str__(self):
        return self.name


example  =  MyString('String') 
print(example.append('hello'))
print(example.pop()) 
print(example)