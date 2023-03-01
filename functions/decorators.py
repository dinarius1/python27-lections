"=============================Декоратор============================="
# Декоратор - это функция высшего порядка, которая нужна чтобы расширять функционал другой функции, не меняя её

# ДОПИСАТЬ КОД ИЗ ГИТА
def decorator(func):
    def wrapper():  #создали вложенную функцию
        print('Функции началась')
        func()
        print('Функции завершилась')
    return wrapper

def func():
    print('hello')

res = decorator(func)   #чтобы сохдать функцию необязательно оборачивать её в def, можно и просто еее приравнять к функции какой то
print(res)
#<function decorator.<locals>.wrapper at 0x7fd325e123b0>

"=======================Синтаксический сахар======================="
def decorator(func):
    def wrapper():  #создали вложенную функцию
        print('Функции началась')
        func()
        print('Функции завершилась')
    return wrapper
@decorator  # func = decorator(func)  -
# @ - возвращает функцию, которая была написана до этого, и переносит эту функцию в функцию, которая будет после @
#в @ пишем название функции, которую хотим обернуть в новую функцию, это может быть любая функция
def func():
    print('hello')

def decorator(func):
    def wrapper(*args, **kwargs):  #здесь мы создаем параметры  #*args - tuple
        func(*args, **kwargs)   #распаковывыем *args, **kwargs, благодаря звездочкам
    return wrapper 

import datetime import datetime
def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        print(f"Функция отработала за {end - start}")
    return wrapper
from functools import cache
@timer
@cache    #cache - кеш - позволяет за более быстрое время вывести значение, кторое было до этого уже запринтено
def func(count):
    for i in range(count):
        print(i)
print(func())


def bold(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return f'<b>{res}</b>'
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return f'<i>{res}</i>'
    return wrapper

@bold     #это будет итогом
@italic
def func(string):
    return f'Hello {string}'
# func = bold(italic(func))

print(func('Makers'))

