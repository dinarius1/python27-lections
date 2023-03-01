# list1 = [1,2,3,1,4,1,5]
# for i in list1:
#     if i != 1:
#         print(i)

# list1 = [1,2,3,1,4,1,5]
# for i in list1:
#     list1.remove(1)
#     break  
# print(list1)


# list1 = [1,2,3,1,4,1,5]
# for i in list1:
#     if i == 1:
#         list1.remove(i) 
# print(list1)


# Задание 4:
# name_of_list = ["ковш"]
# if len(name_of_list[0]) % 2 != 0:
    
# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in nums:
#     while i < 5:
#         print(i)

#Задание 6
# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# res = filter(lambda x: x < 5, nums)
# print(res)


# num = input()
# list_ = list(num)
# tuple_ = tuple(num)
# for i in list_:
#     list_.remove(',')    #уточнить насчет этого. выводиться ошибка: ValueError: list.remove(x): x not in list
# print(list_)
# print(tuple_)

#                       7 task
# num = input()
# list_ = list(num)
# tuple_ = list_
# i = ','
# while i == ',' in list_:
#     list_.remove(',')
# while i == ',' in tuple_:
#     tuple_.remove(',')
# tuple_ = tuple(list_)
# print(list_)
# print(tuple_)

# list_ =  [1, 2, 3, 4, 5]
# new_list = []
# for i in list_:
#     new_list.append(str(i))
# print(new_list)

# 12 задание
# list1 = [11, 23, 45, 7, 9] 
# list2 = [21, 4, 16, 8, 10] 
# res = 0
# list1.extend(list2)
# for i in list1:
#     res += i
# print(res)

# Задание 14
# list_ = [1, 1, 3]
# for i in list_:
#     if i == list_[0]:
#         print('yes')
#     elif i == list_[1]:
#         print('yes')
#     elif i == list_[2]:
#         print('yes')
#     else:
#         print('ERROR')

#Задание 17
# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# cleared_tuples = tuples
# for i in tuples:
#     if i == ():
#         tuples.remove(i)
# print(cleared_tuples)

# dict1 = {'a' : 1, 'b' : 2, 'c' : 3} 
# res = {}
# for key, value in dict1.items():
#     res[value] = key
# print(res)

# dictionary = {'a': 1, 'b': 2, 'c': 3}
# print(iter(dictionary))


# list1 = ['world', 'hello']
# list2 = [1,2,3]
# # a = (reversed(list1))
# print(dict(zip(list1,list2)))

# print(a)



# dict1 = {'a': 1, 'b': 2, 'c':3}

# # for k,v in dict1.copy().items():
# #     if v%2:
#         del dict1[k]

# print(dict1)
    
# string = 'I love cake'
# print(string.split())

string = 'Hello WorlD'
res = [i for i in string if i.islower()]
print(res)

# comprehensions = (i for i in range(1,11))
# print(list(comprehensions))  
# print(list(comprehensions))

# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # []
