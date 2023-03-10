"================================JSON================================"
#JavaScript Ogject Notation - единый формат, в котором могут храниться только те типы данных, которые есть во всех яп поддерживающие json

#Типы данных, которые поддерживаются в JSON
# 1. числа (float, integer)
# 2. строки
# 3. списки
# 4. словари
# 5. булевые значения
# 6. nonetype

import json


# сериализация - перевод из python в json
# dump - функция, которая переводит python обьект в json строку и записывает в файл
# dumps - функция, которая переводит python обьект в json строку

# десерализация - перевод из json в python
# load - функция, которая переводит json строку в python обьект и записывает в файл
# loads - функция, которая переводит json строку в python обьект
 
python_list = [1,2,3]
json_list = json.dumps(python_list)
print(type(python_list))
print(type(json_list))

print(python_list)  #[1,2,3]
print(json_list)    #'[1,2,3]'

json_dict = '{"a":1, "b" : 2}'
python_dict = json.loads(json_dict)

print(type(python_dict))  #str
print(type(json_dict))   #dict - автоматически понимает, что это словарь благодаря своей встроенной система 

list_ = [
    1,2,3,
    4.5,
    (1,2,4),
    {"A" : 1},
    'hello',
    True, False, None
    # {1,2} - сеты не поддерживаются в json
]

with open('test.json', 'w') as file:
    json.dump(list_, file)   #в скобках мы пишем, 1.что записать, и 2.куда записать

with open('test.json', 'r') as file:
    res = json.load(file)
print(res)
# [1, 2, 3, 4.5, [1, 2, 4], {'A': 1}, 'hello', True, False, None]
