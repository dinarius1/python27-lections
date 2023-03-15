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

# Task 4
class MyDict(dict):
    def __init__(self, dict_):
        self.dict_ = dict_
    def get(self, key):
        if self.dict_.get(key) == None:
            return 'Are you kidding?'
        return self.dict_.get(key)

obj_dict = MyDict({'some_title': 2}) 
print(obj_dict.get('some')) 
