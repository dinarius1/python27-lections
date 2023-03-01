# def get_type(x,z):
#        return type(x,z)
# print(get_type(1,'5'))

#Task 7
# def is_palindrome(x):
#     if x[:].lower() == x[::-1].lower():
#         return True
#     else:
#         return False
# print(is_palindrome('Mom'))

# #Task 8
# def max_num(x,z):
#     res = [x,z]
#     return max(res)
# print(max_num(10,22))


# # #Task 9
# def multiply_list(x):
#     count = 1
#     for i in x:
#         count *= i
#     return count
# print(multiply_list([1, 2, 3, 4, 5, 6])) 

# def sum_digits(x):
#     res = list(str(x))
#     total = 0
#     for i in res:
#         el = int(i)
#         total += el
#     return total
# print(sum_digits(105))


# res = list(str(105))
# print(res)
# total = 0
# for i in res:
#     el = int(i)
#     total += el
#     print(total)

# def func12(list1, b):
#     a = []
#     for i in list1:
#         if i == 'lower':
#             a.append(i.lower())
#         elif i == 'upper':
#             a.append(i.upper())
#     return a
# print(func12(["hEllo", "wORld"], "lower"))

# def func12(list1, b): 
#     a = [] 
#     for i in list1: 
#         if b == 'lower': 
#             a.append(i.lower()) 
#         elif b == 'upper': 
#             a.append(i.upper()) 
#     return (a) 
# print(func12(["hEllo", "wORld"], 'upper'))

# def func12(list1, b):
#     a = []
#     for i in list1:
#         if b == 'lower':
#             a.append(i.lower())
#         elif b == 'upper':
#             a.append(i.upper())
#     return a
# print(func12(["hEllo", "wORld"], "lower"))

#Task 13
# def func13(x):
#     keys = list(x)    #создаем переменную keys, где будет храниться каждая буква параметра "x"
#     values = []
#     for i in x:
#         res = x.count(i)
#         values.append(res)
#     dict_ = dict(zip(keys, values))
#     return dict_
# print(func13('Hello'))

#Task 14

#Так можно, но платформа нашу вложенную функцию не может найти, так что можно сделать как расписано во 2 способе:
# def calc(one,two,oper):
#     def add_(one,two):
#         res = one + two
#         return res
#     def sub_(one,two):
#         res = one - two
#         return res
#     def div_(one,two):
#         res = one / two
#         return res
#     def mult_(one,two):
#         res = one * two
#         return res
#     if oper == '+':
#         print(add_(one,two))
#     elif oper == '-':
#         print(sub_(one,two))
#     elif oper == '/':
#         print(div_(one,two))
#     elif oper == '*':
#         print(mult_(one,two))
# print(calc(5,2, "+"))

# def calc(one,two,oper):
#     if oper == '+':
#         return add_(one,two)
#     elif oper == '-':
#         return sub_(one,two)
#     elif oper == '/':
#         return div_(one,two)
#     elif oper == '*':
#         return mult_(one,two)
# def add_(one,two):
#     res = one + two
#     return res
# def sub_(one,two):
#     res = one - two
#     return res
# def div_(one,two):
#     res = one / two
#     return res
# def mult_(one,two):
#     res = one * two
#     return res
# print(calc(4,7, "+"))

# print(calc)


# string = 'Hello'
# keys = list(string)
# values = []
# for i in string:
#     res = string.count(i)
#     values.append(res)
# print(values)
# dict_ = dict(zip(keys, values))

# l = [1, 2, 3, 4, 5, 6]

# def func(lst):
#     res = 1

#     for num in lst:
#         res*=num

#     return res

# print(func([1,2,3,4,5,6]))

# users = [
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
# ]
# res = []
# def func15():
#     for i in users:
#         for v in i.values():
#             print(v)
#             if type(v) == type(' '):
#                 res.append(v)
#                 for inner in res:
#                     print(res)
#                     if inner.startswith("IT"):
#                         print(inner)
#                         return f"{i['name']}, скидки в магазине компьютерной техники!"
# print(func15())
# def func15():
#   for user in users:
#       if user['work'].startswith("IT"):
#           res.append(f"{user['name']}, скидки в магазине компьютерной техники!")
#   return ('\n'.join(res)) 
# print(func15())

#Task 15
# users = [ { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer'}, { 'name': 'Helen', 'age': 35, 'work': 'Nurse'}, { 'name': 'Bob', 'age': 35, 'work': 'Driver'}, { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer'}, { 'name': 'Helga', 'age': 35, 'work': 'IT-HR'} ] 
# def func15(): 
#     r=[] 
#     for i in users: 
#         if i['work'].startswith('IT'): 
#             r.append(f"{i['name']}, скидки в магазине компьютерной техники!") 
#     for inner in r:
#         print(inner)   #return inner - почему когда вместо принт пишу return выходит только одно имя, а не все имена, которые работяют в сфере айти?
# print(func15())



# #Task 16
# def func16(km, v): 
#     return f'На 100км было расходовано {round(100*v/km)}л горючего'
# print(func16(50,8))

# #Task 17
# employees = [
#   {'name': 'Jack', 'salary': 10000, 'overTime': 4},
#   {'name': 'Tom', 'salary': 15000, 'overTime': 3},
#   {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
#   {'name': 'Helen', 'salary': 25000, 'overTime': 2},
#   {'name': 'Peter', 'salary': 30000, 'overTime': 7}
# ] 
# def func17(employees):
#     for i in employees:
#         i['salary'] += i['overTime'] * 200
#         i.popitem()
#     return employees
# print(func17(employees))

# #Task 18
# def func18(list1):
#     res = []
#     res2 = []
#     for i in list1:
#         if type(i) == type(4):
#             res.append(i)
#         else:  
#             res2.append(i)
#     return res, res2
# print(func18([4, 'dfs', '', 234, 'sdsda', 7, 'sdf']))


# #Task 19 - как решить?
# students = [
#   {'student': 'Jack', 'marks': 43},
#   {'student': 'Tom', 'marks': 92}, 
#   {'student': 'Helen', 'marks': 85}, 
#   {'student': 'Peter', 'marks': 58},
#   {'student': 'Jessica', 'marks': 78}
# ]
# def func19(students):
#   res = []
#   for i in students:
#     res.append(i['marks'])
#   res.sort(reverse = True)
#   dict_ = []
#   for number in res:
#       for i in students:
#           if i['marks'] == number:
#               dict_.append(i)
#   return dict_
# print(func19(students))

              

# #Task 20 - тут все правильно по идее, но на платформе выходит ошибка экстра тест
# products = [
#   {
#     'title': 'Samsung S10', 
#     'price': 800, 
#     'count': 6, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 13 Pro', 
#     'price': 1200, 
#     'count': 9, 
#     'category': 'apple'},
#   {
#     'title': 'Xiaomi Mi 10', 
#     'price': 500, 
#     'count': 2, 
#     'category': 'xiaomi'},
#   {
#     'title': 'Samsung S9', 
#     'price': 600, 
#     'count': 4, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 11', 
#     'price': 850, 
#     'count': 1, 
#     'category': 'apple'}
# ]

# def func20(products,name):
#     for i in products:
#         res = i['title']
#         if name.lower() in res.lower():
#             print(res)  #как можно вывести все словари, если в этой строки написать return i, а не print(res)
#     return i
# print(func20(products,'i'))

#Правильное решение:  - то есть если мы используем цикл for с командой иф, и нам нужно вернуть какое то значение из данной кострукции, то надо лучше вести новую переменную?

# def func20(products,name):
#     res2 = []
#     for i in products:
#         title = i['title']
#         if name.lower() in title.lower():
#             res2.append(i)
#     return res2
# print(func20(products,'i'))

#Task21 - условия из 20 го
# def func20(products,name):
#     res2 = []
#     for i in products:
#         category = i['category']
#         if name.lower() == category.lower():
#             res2.append(i)
#     return res2
# print(func20(products,'samsung'))


#Task22
balance = 22

def spent(name,price,balance):
    if balance > price:
        balance = balance - price
        dict_ = {'target' : name, 'spend' : price}
        return dict_, balance
    return 'Недостаточно средств'
def deposit(summary, balance):
    balance = balance + summary
    return balance
print(spent('Products', 200, balance))
print(deposit(400,balance))




#Task23
database = [{'title': 'black tea', 'price': 70, 'category': 'tea'}, {'title': 'latte', 'price': 200, 'category': 'cofee'}]

def create(database, title, price, category):
  dict_ = dict([('title',title), ('price', price), ('category',category)])
  database.append(dict_)
  return database

def read(database):
  return database

def update(database, index, title, price, category):
  database[index]['title'] = title
  database[index]['price'] = price
  database[index]['category'] = category
  return database
def delete(database, index):
  database.pop(index)
  return database
print(create(database,'Lipton', 89, 'ice drink'))
print(read(database))
print(update(database,0,'black tea', 89, 'tea'))
print(delete(database,1))




# def CRUD(oper, database, index, title, price, category):
  
#   if oper == 'create':
#     return create(database, title, price, category)
#   elif oper == 'read':
#     return read(database)
#   elif oper == 'update':
#     return update(database, index, title, price, category)
#   elif oper == 'delete':
#     return delete(database, index)
# print(CRUD('create', database, 1, 'samsung 10', 15000, 'phones' ))
      


# database = []
# def CRUD(oper):
#   def create(database, title, price, category):
#       dict_ = dict([('title',title), ('price', price), ('category',category)])
#       database.append(dict_)
#       return database

#   def read(database):
#       return database

#   def update(database, index, title, price, category):
#       dict_ = dict([('title',title), ('price', price), ('category',category)])
#       database.append(dict_)
#       for index in database:
#           database['title'] = title
#       return database
#   if oper == 'create':
#     return create(database, title, price, category)
#   elif oper == 'read':
#     return read(database)
#   elif oper == 'update':
#     return update(database, index, title, price, category)
#   elif oper == 'delete':
#     return delete(database, index)
# # {title: 'str', price: num, category: 'str'}
# print(CRUD)

def a():
  a = 5
  b = 9
  return a,b
print(locals())
      