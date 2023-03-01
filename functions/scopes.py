"===============ОБЛАСТИ ВИДИМОСТИ / ПРОСТРАНСТВО ИМЕН==============="
# LEGB - (local, enclosed, global, build-in)

#build-in это встроеннная пространство (например: print, input, int, str, sum)

#global - глобальное пространство это наш текуший файл  (например )

#Функции: globals(), locals()
# Функция locals() обновляет и возвращает словарь с переменными и их значениями из текущей локальной области видимости.

# Функция globals() возвращает словарь со значениями переменных, представляющий текущую глобальную область видимости. чтобы посмотреть все глобальные переменные у нас есть функция globals()
#например
a = 5
b = 9
print(globals())

#enclosed - замкнутое пространство (находится между двумя пространствами)
#локальное пространство, внутри которого есть еще одно локальное пространство

# var = 'глобальная'

# def func():
#     var = 'замкнутое'
#     def inner func():
#         var = 'локальное'
#         print(var)
#     print(var)
# print(var)

# var = 'глобальная'
# def func():
#     var = 'замкнутая'
#     def inner_func():
#         var = 'локальная'
#         def inner_inner_func():
#             var = 'супер локальная переменная'
#             print(var)
#         inner_inner_func()
#         print(var)
#     inner_func()
#     print(var)
# func()
# print(var)

#local  - локальное пространство (внутри функции)
a = 'hello'
def func(a,b):
    print('GLOBALS', globals())  #GLOBALS... 'a': 'hello', 'func': <function func at 0x7f181dc67d90>}
    print('LOCAL', locals())  #LOCAL {'a': 10, 'b': 50}
func(10,50)

#Пример 1
num1 = 10

def func():
    print(num1) # 10 - тут выводиться 10, так как вывзывать переменную из глобального пространства можно

func()

#Пример 2
counter = 0

def increase_counter():
    counter =  counter + 1 #без ключевого слова global нельзя вывести counter += 1, так как он не видит, что мы ссылаемся на  counter из глобального пространства, поэтому он создает новую локальную counter, но он не видит, чему равна изначально переменная counter
    print(counter)

def increase_counter():
    global counter        #ключевое слова global позволяет как раз выести counter из глобального пространства в локальную
    counter += 1
    print(counter)

increase_counter() # 1
increase_counter() # 2
increase_counter() # 3
increase_counter() # 4

def count(i):
    counter = 0

    def increse_counter():
        nonlocal counter    #nonlocal ("нелокальный")- это  ключевое слово, которое позволяет вытащить переменную из любого локального пространства, но не своего локального пространства 
        counter += 1
        print(counter)
    for _ in range(i):
        increase_counter()
count(10)
count(10)

def func():
    a = 10
    def inner_func():
        def inner_inner_func():
            nonlocal a
            a += 1
        inner_inner_func()
        print(a)
    inner_func()
func()  #11, так как nonlocal ищет пременную из всего локального пространства
