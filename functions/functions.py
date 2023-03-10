"==============================Функции=============================="
# Функция - это именованный блок кода, который принимает аргументы и возвращает результат

func = lambda num1, num2: num1 + num2
res = func(5,10)
print(res) # 15
# lambda - это ключеве слово, для создания анонимной функции. испоьзуем ее когда она нужна 1 раз. она пишется в одну строку. она анонимгая, не имеет название

def my_sum2(num1,num2):   #с помощью def можно сохдать любую функцию
    return num1 + num2
print(my_sum2)
res = my_sum2(13,45)
print(res) # 58

def calc(num1,num2,oper):
    """            # - это документация для функции, то есть это в сое роде подскажки для программиста 
    oper - строка с операцией для вычислений
    "+" - сложение
    "-" - вычитание и тп
    """
    if oper == "+":
        return num1 + num2
    if oper == '-':
        return num1 - num2
    if oper == '*':
        return num1 * num2
    if oper == '/':
        return num1 / num2
print(calc(10,12,'+'))
print(calc(10,8,'-'))
print(calc(10,12,'*'))
print(calc(10,1,'/'))

print(calc(10,12,'2'))  #такого оператора нет, поэтому он возвращает None

def my_len(obj):
    'Возвращает длину объекта'
    count = 0
    for i in obj:
        count += 1
    return count
print(my_len([1,2,3,4])) # длина 4
print(my_len('sdadqwd')) # длина 7
print(my_len({'a' : 1, 'b' : 2})) # длина 2 - так как вохрващает ток значения ключей

def super_len(obj):
    try:
        #мы тут импользуем прошлую функцию my_len()
        return my_len(obj)
    except TypeError: 
        #если не можем, то будем итерировать его в виде строки
        return my_len(str(obj))
print(super_len([1,2,3,4])) #4
print(super_len([123456)  #6
print(super_len(None))   #4 - "None" - string

"================================DRY================================"
#DRY - dont repeat yourself (не повторяйся)

"=======================Аргументы и параметры======================="
# параметры - это локальные переменные, значения которым мы задаем при вызове функции
# аргументы - это значения, которые мы задаем параметрам при вызове функции
# drf func():

#функция может быть пустой и пожтому не оьзятаельео что то возвращать

def func(parameter):
    local_var = 5
    print(locals())
    # {'parameter': 6, 'local_var': 5}

func(6)
# print(local_var) NameError
# print(parameter) NameError

"==========================Виды параметров=========================="
#ОЧЕНЬ ВАЖЕН ПОРЯДОК как тут. Обязательно нужно сначала указать все обязательные параметры, потом уже необязательные и тоже по нижеуказанному порядку 
# 1. обязательные
# 2. необязательные
# 2.1 с дефолтным значениям (по умолчанию)
# 2.2 args (arguments) - ЕГО ТОК 1 РАЗ МОЖНО ПИСАТЬ
# 2.3 kwargs (key word arguments) - ЕГО ТОК 1 РАЗ МОЖНО ПИСАТЬ

#1. обязательные
def func(a):
    print(a)
func()
# TypeError: func() missing 1 required positional argument: 'a'

# 2.1 с дефолтным значениям (по умолчанию)
def func(a,b = 'default'):
    print(a,b)
func('hello') #'hello' 'default'
func('hello', 100) #'hello' 100

# 2.2 args (arguments)
def func(a,b = 'default', *args):  # *args - позволяет вывести в отслаьные параметры в виде кортежа
    print(a,b, args)
func('hello', 'default', 100,4,654,6)  #'hello','default', ( 100,4,654,6)

# 2.3 kwargs (key word arguments)
def func(a,b = 'default', *args, **kwargs):
    print(a,b, args, kwargs)
    #args - tuples, куда попадут все позиционные аргументы, которые не попали по позиции
    #kwargs - dict, куда попадут все именнованные аргументы, которые не попали по имени
func('hello', 'default', 100,4,654,6, key1 = 'value1' )
#'hello', 'default', (100,4,654,6), {key1 : 'value1'}


"=========================Виды аргументов========================="
# позицаонные (по порядку параметров)
# имннованные (по имени парамтров)

def func2(a, b):
    print(f"a={a}, b={b}")

func2(10, 20) # позиционно -  обязательно нужно вывести сначала значение 1 го аргумента
# a=10, b=20

func2(a = 30, b = 40) # именованно - по имени обращаемся
# a=30, b=40

'=============================Звездочки============================='
list_ = [1,2,3,4]
list2 = [*list1]  #распаковка переменной list1
print(list2) #[1,2,3,4]
# * - распаковка из перемнной, типо итерирует
dict1 = {'a' : 1, 'b' : 2}
dict2 = [*dict1]  #['a', 'b']
# ** - это распаковка на ключ-значения, т.е в словарь

