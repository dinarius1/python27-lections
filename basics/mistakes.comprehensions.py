
# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {k : list(range(1,v + 1)) for k, v in a.items()}
# print(dict_)

# #Задание 12
# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# a = {k:('odd' if v % 2 != 0 else 'even') for k, v in dict_.items()} #почему нельзя писть else k:'even' - почемц выдает синтаксическая ошибка
# print(a)
# # а когда пишем так, то все правильно:
# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# a = {k:'odd' if v % 2 != 0 else 'even' for k, v in dict_.items()} print(a)

# #Задание 13
# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# s = string_.split()
# list_ = [i for i in s if i.isdigit()]
# print(list_)

#Задание 14
# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
# 'Olga': {'history': 92, 'math': 96, 'literature': 81}, 
# 'Nik': {'history': 84, 'math': 85, 'literature': 87}}
# new_dict = {k : k2 for k,v in dict_.items() for k2, v2 in v.items() if v2 == max(v.values())}
# print(new_dict)  

# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
# 'Olga': {'history': 92, 'math': 96, 'literature': 81}, 
# 'Nik': {'history': 84, 'math': 85, 'literature': 87}}
# new_dict = {v : v for k,v in dict_.items() for k2, v2 in v.items() if v['history'] == 90}
# print(new_dict)  


#Задание 15
my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
dict_ = {k : v2 for k,v in my_dict.items() for v2 in v.values()}
print(dict_)

#{'first': 1, 'second': 2}

# #Задание 18
# list1 = [1, 2, 'hello', 3, 'world', 4, 5, 'book', 'code', 6, 'Makers', 7, 8, 9, 10]
# list2 = [i for i in list1 if i.isalpha()]
# print(list2)

# string = "happy birthday!"
# list_ = [i for i in string if i != "!" and i != " "]
# print(list_)

# #Задание 27
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# dict_ = {i : (len(i) ** 2) for i in list_name if len(i) > 4}
# print(dict_)

# #Задание 28
# dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# r = list(range(200, 5001))
# list1 = [k.upper() : k.count('i') for k,v in dict_.items() if v in r and k.isupper()]
# print(list1)

# dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# r = list(range(200, 5001))
# list1 = [k.upper() for k,v in dict_.items() if 200 < v < 5001]
# print(list1)

# #Задание 29
# dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# dict2 = {k.replace('i',''): k.count('i') for k,v in dict1.items()}
# print(dict2)

# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]
# readers = [x[0] for x in SPL_Patrons if x[1] > 100] 
# print(readers)

# readers = [inner for i in SPL_Patrons for inner in i if type(inner) == type(1) and  > 100]
# print(readers)

# prairie_pirates = [
# ['Tractor Jack', 1000, True],
# ['Plowshare Pete', 950, False],
# ['Prairie Lily', 245, True],
# ['Red River Rosie', 350, True],
# ['Mad Athabasca McArthur', 842, False],
# ['Assiniboine Sally', 620, True],
# ['Thresher Tom', 150, True],
# ['Cranky Canola Carl', 499, False]]
# list_ = [[i[0],i[1] * 42] for i in prairie_pirates if i[2] == True]
# print(list_)

#Задание 34
# dict_ = {
#     'Sasha': {
#         'likes': 23,
#         'comments': 2,
#         'rating': 4
#     },
#     'Aliya': {
#         'likes': 34,
#         'comments': 5,
#         'rating': 5
#     },
#     'Dasha': {
#         'likes': 15,
#         'comments': 3,
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': 2,
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': 7,
#         'rating': 2
#     }
# }
# list_ = [sum(k2['likes']) for k, v in dict_.items() for k2, v2 in v.items() if k2['rating'] > 3]
# list_ = {k['likes'] for k, v in dict_.items() for k2, v2 in v.items()}
# print(list_)

# ПРавильное решение:
# list_ = [v['likes'] for v in dict_.values() if v['rating']>3] 
# print(sum(list_))

# set1 = {1,2,345,5,3,4}
# set2 = {3,4,5,6,7}
# set1.update(set2)
# full_set = set1
# print(full_set)

# set1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# set2 = {8, 9, 10, 11, 12, 13, 14, 15, 16, 17}
# full = set1.update(set2)
# full_set = {f'В этом сете было {set1.intersection(set2)} повторения, его длина составляет {len(set1)}' if len(set1) < 20 for i in s

#Задание 35
# dict_ = {
#     'Dasha': {
#         'likes': 15,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#         ],
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#         ],
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#             {'id': 4, 'text': 'some text'},
#             {'id': 5, 'text': 'some text'},
#             {'id': 6, 'text': 'some text'},
#         ],
#         'rating': 2
#     }
# }
# # res = [v2['id'] for v in dict_.values() for v2 in v['comments'] if len(v['comments']) > 3]
# print(res)

# res = [value2['id'] for value in dict_.values() for value2 in value['comments'] if len(value['comments']) > 3]
# print(res)

#Задание 38
# set1 = {x for x in range(1,11)}
# set2 = {x for x in range(11, 21)}
# full_set = set1.union(set2)
# if len(full_set) < 20:
#     print(f'В этом сете было {20 - len(full_set)} повторения, его длина составляет {len(full_set)}')
# elif len(full_set) == 20:
#    print('Ваш объединенный сет полностью уникальный!')

# set1 = {x for x in range(1,11)}
# set2 = {x for x in range(11,21)}
# full_set = set1.union(set2)
# if len(full_set) < 20:
#     print(f"В этом сете было {20 - len(full_set)} повторения, его длина составляет {len(full_set)}")
# elif len(full_set) == 20:
#     print(f"Ваш объединенный сет полностью уникальный!")