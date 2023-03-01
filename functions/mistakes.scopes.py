# #Task 1
# def foo():
#     var = 'переменная foo'
#     print('переменная в foo: ', var)
#     def bar():
#         nonlocal var
#         var = 'переменная bar'
#     bar()
#     return var
# print('переменная в foo: ', foo())

# # переменная в foo:  переменная foo
# # переменная в foo:  переменная bar

#Task 2
# x = 'Я глобальная переменная!'
# def my_func():
#     global x
#     x = "Я могу изменяться"
#     return x
# print(x)
# print(my_func())
# print(globals())

#Task 4
balance = 0
def get_salary(amount):
    global balance
    balance = balance + amount
def pay_bills(amount, log_name):
    global balance
    balance = balance - amount
    print(f"Вы заплатили {amount} сом за {log_name}")
def get_balance():
    global balance
    print(f'У вас на счету {balance} сом')
get_salary(1000)
get_balance()
pay_bills(400, 'кабельное тв')
get_balance()


# Task 6
a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}

for k,v in a.items():
    if v >= 17:
        print(f'{k}, Вы можете войти в клуб')
    else:
        print(f'{k}< извините, Вы не проходите по age-control')


# 2 способ
# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}

# def age():
#     global a
#     for k,v in a.items():
#         if v >= 17:
#             print(f'{k}, Вы можете войти в клуб')
#         else:
#             print(f'{k}< извините, Вы не проходите по age-control')
# age()


# Task 7
# a = ['pipi', 'papa', 'mama']
# def string():
#     global a
#     b = []
#     for i in a:
#         b.append(i.title())
#     return b
# print(string())

# #2 способ
# a = ['pipi', 'papa', 'mama'] 
# b = [] 
# for i in a: 
#     b.append(i.capitalize()) 
#     print(b)

# Task 8
def count_symbols(string):
    glas = 0
    soglas = 0
    ostal = 0
    for i in string:
        if i.isalpha():
            if i.lower() in 'аяуюоеёэиы':
                glas += 1
            else:
                soglas += 1
        else:
            ostal += 1
    return f'Количество гласных: {glas}, согласных: {soglas}, остальных символов: {ostal}'
print(count_symbols('Мурат супер!'))

# def count_symbols(words): 
#     glasnue = 0 
#     soglasnue = 0 
#     symbol = 0 
#     for i in words: 
#         if i.isalpha(): 
#             if i.lower() in 'яиюэёоаыуе': 
#                 glasnue += 1 
#             else: soglasnue += 1 
#         else: symbol += 1 
#     return (f'Количество гласных: {glasnue}, согласных: {soglasnue}, остальных символов: {symbol}') 
# print(count_symbols('Мурат супер!'))

# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
# for i in a:
#     if i > 7:
#         a.remove(i)
# print(a)
# def lower_7():
#     global a
#     for i in a:
#         if i > 7:
#             a
#     return a
# print(lower_7())

# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
# def lower_7():
#     global a
#     res = []
#     for i in a:
#         if i < 7:
#             res.append(i)
#     return res
# print(lower_7())