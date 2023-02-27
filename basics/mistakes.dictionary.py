#Задание 9
# a = {'a': 1, 'b': 4, 'c': 12, 'd': 5, 'e': 6}
# b = a.copy()
# for k, v in b.items():
#     if v % 4 == 0:      
#         b[k] = 2     #если нам нужно заменить значение у ключа, то мы должны сослаться в первую очередь на ключ и затем присвоить ему новую переменную
# print(b)


# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# for k, v in list(a.items()):
#     if a[k] == None:
#         a.pop(k)
#         a.update()
# print(a)

#Задание 23
# dict1 = {25: 'apple', 26: 'orange', 27: 'banana'} 
# dict2 = {}
# for k in list(dict1.keys()):
#     dict2 = 

#Задание 25
# dict_ = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}
# res = []
# for k,v in list(dict_.items()):
#     res.append(dict_[k])
#     for n in res:
#         if n == max(res):
#             print(k)

# dict1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
# dict2 = {}
# res1 = []
# for k, v in dict1.items():
#     k = v ** 3
#     res1.append(k)
#     dict2[k]

# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# for k,v in dict_.items():
#     for v2 in v.values():
#         dict_[k] = v2
# print(dict_)

# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}} # dict_ = {k:(v[v1]) for k,v in dict_.items()} # print(dict_) for k,v in list(dict_.items()): for v2 in v.values(): dict_[k] = v2 print(dict_)

# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}} 
# for k,v in list(dict_.items()): 
#     for v2 in v.values(): dict_[k] = v2 print(dict_)

        
# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}
# res = []
# step = 2
# for k,v in dict1.items():
#     for v2 in v.values():
#         for v2 in range(dict1[k],  step):
#             res.append([])
# print(res)

#Задание 28 - НЕ ПОНЯЛА!!!!!!
# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}} 
# dict2 = {} 
# for k,v in list(dict1.items()): 
#     res = 1 
#     for j in v.values(): 
#         res = res * j 
#         dict2[k] = res 
#         print(dict2[k])
# print(dict2)

#Мое решение:
# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}
# res = []
# for k,v in dict1.items():
#     for v2 in v.values():
#         res.append(v2)
# for i in res:
#     for i range(1,10,2):
#         i = i * res[i + 1]
#         print(i)

#Задание 29
# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
# list2 = []
# list3 = []
# for i in list_:
#     if type(i) == type(''):
#         list2.append(i)
#     else:
#         list3.append(i)

# dict_ = dict(zip(list2, list3))
# print(dict_)

#Задание 30
dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0} 
sorted_values = sorted(dict_.values()) 
print(sorted_values)
sorted_dict = {} 
for i in sorted_values: 
    for k in dict_.keys():  #- можете обяснить как работуют тут циклы for. в цикеле с i и k. и как тут работает команла иф снизу
        if dict_[k] == i: 
            sorted_dict[k] = dict_[k]  # и мы тут рассмотриваем именно значения двух словарей, да? не их ключей? или так как сортед дикт = дикт, то и ключи также перемещаются в сортед дикт? как вообще появились ключи в сортед дикт?
print(sorted_dict)


#Задание 32
# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 
# key = int(input())
# if key in dict_.keys(): 
#     print("Key is present in the dictionary") 
# else:
#     print("Key is not present in the dictionary")      

#Задание 35
# dict_ = {
#     'math': {
#         'sum': sum
#     },
#     'vars': {
#         'a': 5,
#         'b': 20,
#         'c': 50
#     }
# }
# res = []
# for k,v in list(dict_.items()):
#     for v2 in v.values():
#         res.append(v2)
# n = dict_['math']['sum']
# poped = res.pop(0)

# print(n(res))

#Задание 26
# Правильный вариант:
# dict1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
# list1 = []
# list2 = []
# list3 = []
# for k in dict1.keys():
#     list1.append(k)
# for v in dict1.values():
#     list2.append(v)
# for i in list2:
#     total = i ** 3
#     list3.append(total)   
# print(list3)
# dict2 = dict(zip(list1, list3))
# print(dict2)

#Задание 26
# Неравильный вариант. ПОЧЕМУ ТУТ ОШИБКА?
# dict1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
# list1 = []
# list2 = []
# for k in dict1.keys():
#     list1.append(k)
# for v in dict1.values():
#     list2.append(v)
# for i in list2:
#     total = i ** 3  
#     list2.append(total)   # почемы тотал не добавляется
# print(list2)

#Множества.
#Задание 13
robert = {5, 7, 11, 10, 28} 
kail = {1, 5, 14, 8, 22} 
merri = {19, 20, 3, 11, 10}
if robert & merri:
    if robert & kail:
        print('kail merri')
elif robert & kail:
    print('kail')
elif robert & merri:
    print('merri')
else:
    print('no one')

#Задание 15
ingredients = {"cыр чеддар","грибы", "соус","шпинат"} 
ingredients.add('помидоры')
ingredients.remove('колбаса')
ingredients.remove("шпинат")
ingredients.rep