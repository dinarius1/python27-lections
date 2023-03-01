"=============================Exceptions============================="
# Исключения (ошибки) - обьекты, которые обрывают работу кода, если не были обработаны

SyntaxError
# исключение, которое выходит если допущена синтаксическая ошибка
""" 
(

SyntaxError: '(' was never closed
"""
# если используем ключевые слова не правильно
"""
break

SyntaxError: 'break' outside loop
"""
"""
if = 5

SyntaxError: invalid syntax
"""
TypeError
# исключение, которое выходит когда мы делаем что-то не свойственное данному типу данных
""" 
1 + '1'

TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

"""
for i in 123456789:
    ...
TypeError: 'int' object is not iterable
"""
TypeError
#когда мы передаем в функцию метода больше или меньше аргументоа, чем она требует. ТУТ ОШИБКА С МЕТОДАМИ ТИПОВ ДАННЫХ
"""
list1 = []
list1.pop(1,2,3,4)

TypeError: pop expected at most 1 argument, got 4

list1 = []
list1.append()

TypeError: list.append() takes exactly one argument (0 given)
"""

KeyError
#когда мы обращаемся к несуществующему ключу
"""
dict_ = {'a' : 1}
dict_['c']

KeyError: 'c'

dict_ = {'a' : 1}
dict_.pop('c')

KeyError: 'c'
"""

NameError
#когда мы обращаемся к переменной или функции, которые не существуют
"""
print(c)
NameError: name 'c' is not defined

a = 5
if a == 6:
    b = 7  #переменная создается только тогда, когда условие верное
print(b)
NameError: name b is not defined
"""
ValueError
#когда мы передаем в функцию то, что она не может корректно обрабботать
#когда у нас что то не так со значением
"""
int('10a')
ValueError: invalid literal for int() with base 10: '10a'
"""
#когда мы пытаемся распаковать не такое же кол-во элементов в несколько переменных

"""
a,b = 1,2,3
a,b,c = 1,2
a,b,c = 1,2,3,4
ValueError: too many values to unpack (expected 2)
"""

AttributeError
#когда пытаемся обратиться к несуществующему методу в каком то типе дпнных
"""
list_ = []
list_.lower()
AttributeError: 'list' object has no attribute 'lower'
"""
IndexError
#когда мы обращаемся по несуществующему индексу
"""
list_ = [1,2,3]
list_[100]
IndexError: list index out of range

list_ = []
list_.pop()
IndexError: pop from empty list
"""

ModuleNotFoundError
#когда пытаемся обратиться к несуществующей библиотеки
"""
import django
ModuleNotFoundError: No module named 'django'
"""
ZeroDivisionError
#когда делим на 0
"""
10/0
ZeroDivisionError: division by zero
"""

IndentationError
#когда мы не соблюдаем отступы
"""
 v = 1
IndentationError: unexpected indent

if True:
print('hello')
IndentationError: expected an indented block after 'if' statement on line 95
"""

Exception
#исключение, которое создали, чтобы его вызывать

#чтобы вызвать исключение, используем raise
#raise Exception('Hello')

"========================Обрабтка исключений========================"
#чтобы наш код не ломался, мы можем использовать конструкцию try-except и обработать исключение

#минимальная конструкция состоит из try-except или try-finally
#Поэтому необязательно все ключи использовать, можно использовать конструкцию из 2 элементов, из 3 элимементов или из 4 элементов

#можно использовать несколько except


try:
    #код который возможно вызовет ошибку
    num = int(input('Введите число'))
except ValueError:
    # код, который отработает только если в блоке try вызвалась ошибка ValueError
    print("Вы ввели не число")
else:
    #код, который отработает только если в блоке try ни одна ошибка не вызвалась
    print('Введенное число', num)
finally:
    #код, который отрабатывается вообще в любом случае
    #хоть вызвалась ошибка, хоть не вызвалась
    print('До свидания')

try:
    num1 = int(input('Введите первое число'))
    num2 = int(input('Введите второе число'))
    print(num1//num2)
except ValueError:
    print("Вы ввели не число")
except ZeroDivisionError:
    print("На ноль нельзя делить")

try:
    num1 = int(input('Введите первое число'))
    num2 = int(input('Введите второе число'))
    print(num1//num2)
except (ValueError, ZeroDivisionError):
    print("Вы ввели некорректные данные")

#можно отловить любые исключения,  используя просто except. Он будет ловить все возможные ошибки
#НО нам нужно часто бывает отлавливать только определенные ошибки, поэтому мы и определяем ошибку после except
try:
    1 + '1'
except:
    print('Любая ошибка')

#ОЧЕНЬ ВАЖНОЕ ПРИМЕЧАНИЕ!!!!
# РАССМОТРИ ЗАДАЧУ СНИЗУ:
try:
    print(1+'1') # TypeError
except TypeError:
    print(int('10a')) # ValueError
    print("первый except")
except ValueError:
    print("второй except")
finally:
    print("все")

1. сначала выходит ошибка TypeError, поэтому по идее мы должны вывести  print(int('10a'))
2. однако int('10a') содержит в себе ошибку (точнее ошибку ValueError), поэтомц мы ее не принтим и не принтим print("первый except"), так как до него уже была ошибка
3. except ValueError НЕ ВЫВОДИТЬСЯ, так как он берет значения из TRY, а не except TypeError - (int('10a')
4. поэтому вывдиться только из тело finally - print("все") c  

# Тут уже видоизмененная задача:
try:
    print(1+'1') # TypeError
except TypeError:
    try:
        print(int('10a')) # ValueError
        print("первый except")
    except ValueError:
        print("вложенный except")
except ValueError:
    print("второй except")
finally:
    print("все")

Выводы:
- каждый except мы смотрим только с телом try, не с другими except. 
- мы можем в except писать еще одну конструкцию try-except (просто еще один except без try нельзя!!!)




