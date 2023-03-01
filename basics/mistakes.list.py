

# res = sorted([a,b,c])
# print(*res)
# # for i in res:
# #     print(i)

# num = input()
# list_ = list(num)
# i = ','
# while i in list_:
#     list_.remove(i)
# print(list_)

# tuple = list_


#Задание 3
name_of_list = ['Helloworld!'] 
string = name_of_list[0]

len_ = len(string)

if len_ % 2 == 0:
    one = string[:len_ // 2]
    sec = string[len_ // 2:]
else:
    one = string[:(len_ // 2) + 1]
    sec = string[(len_ // 2) + 1:]

new_list = list(sec) + list(one)
print(new_list)

# Задание 13
# x = input()
# list_ = x.split(',') - мы с запятыми выведем список, 
# list_.sort()  - сортируем по 1 буквам из списка, каждая строка из числа имеет свое значение в виде цифры.
# print(list_)

# Задание 14
list_ = [1,2,3]
new_list = sorted(list_)
if new_list[0] == new_list[1] or new_list[-1] == new_list[-2]:
    print('yes')
else:
    print('ERROR')



#Задание 16
# list_ = [20, 10, 20, 1, 100]
# list_.sort()
# print(list_[0])

# Задание 17 - пустые кортежи имеют длину 0, а не None!!!
# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# cleared_tuples = []
# for i in tuples:
#     if len(i) != 0:
#         cleared_tuples.append(i)
# print(cleared_tuples)

#Задание 18
# fio1 = input().split()[-1]
# fio2 = input().split()[-1]
# fio3 = input().split()[-1]
# fio4 = input().split()[-1]
# fio5 = input().split()[-1]

# lists = [fio1, fio2, fio3, fio4, fio5]
# lists.sort()
# print(lists)

#Задание 19  - когда мы пытаемся изменить старый список, то лучше вводить новый списко как в задании, а не стараться изменить старый список!!!!!!!!
# list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# number = 8
# new_list = []
# for i in list_:
#     if i == number:
#         new_list.append(i)
# print(len(new_list))

#Задание 20
# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]
# my_list = []
# total = 0
# for i in list_:
#     number = str(i)
#     if number.isdigit():
#         number = int(number)
#         my_list.append(number)
# for k in my_list:
#     total += k
# print(total)

#Задание 21
# str_list = ['abc', 'xyz', 'aba', '1221']
# new_list = []
# for i in str_list:
#     if i[0] == i[-1]:
#         res = str_list.index(i)
#         new_list.append(res)
# print(new_list)

#Задание 22
# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# max_list = []
# min_list = []
# max_list2 = []
# min_list2 = []
# res = sorted(lists, key = len)
# max_list.append(res[-1][:])
# min_list.append(res[0][:])
# for i in max_list:
#     max_list2.append(i)
# for i in min_list:
#     min_list2.append(i)
# print(f'max_list {max_list2}')
# print(f'min_list {min_list2}')

#Задание 22
# - из телеге взять 2 способа решения!
# Нурсултан:
lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
sort_list = sorted(lists, key = len)

if sort_list[0] == sort_list[-1]:
    print(f'max_list {sort_list[-1]}')
    print(f'min_list {None}')
else:
    print(f'max_list {sort_list[-1]}')
    print(f'min_list {sort_list[0]}')

# Бекболсун:
# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# max_list = lists[0]
# min_list = lists[0]
# for i in lists:
#     if len(i) > len(max_list) and len(i) >= 0:
#             max_list = i
#     if len(i) < len(min_list) and len(i) >= 0:
#             min_list = i
# if len(max_list) > 1:
#     print(f'max_list {max_list}')
#     print(f'min_list {min_list}')
# else:
#     print(f'max_list {max_list}')
#     print(f'min_list {None}')


# res = sorted(lists, key = len)
# max_list = []
# min_list = []
# max_list.append(res[-1])  - не надо вводить эти списки, так как у нас уже есть отсортированный список res, и мы просто потом будем по индексам смоореть дальше
# min_list.append(res[0])
# result2 = int(''.join(map(str, max_list)))
# result1 = int(''.join(map(str, min_list)))

#Задание 23
# step = 5
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# new_list = []

# for i in range(step):
#     new_list.append(list_[i::step])

# print(new_list)





#Списки
#Задание 24
# size = 3
# matrix = []
# for i in range(size):
#     matrix.append([])
#     for j in range(1, size + 1):
#         matrix[i].append(j)
# print(matrix)

#Задание 25:
# word = input()
# my_list = []
# list_ = ['sun', 'flowers', 'rumor', 'stranger', 'adventure', 'architect', 'accompany', 'abandon', 'cartoon']
# for i in list_:
#     if i[0] == word:
#         my_list.append(i)
# print(my_list)

#Задание 26:
# colors1 = ["red", "orange", "green", "blue", "white"]
# colors2 = ["black", "yellow", "green", "blue"]

# res = []
# res2 = []

# for color in colors1:
#     if color not in colors2:
#         res.append(color)

# for color in colors2:
#     if color not in colors1:
#         res2.append(color)

# print(res, res2)
    

#Задание 27
list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]
res = []
for i in list1:
    if i in list2:
        res.append(i)

if len(res) > 0:
    print(True)
else:
    print(False)
    



#Задание 28 
# list_ = [4, 6, 4, 3, 3, 8, 4, 3, 4, 3, 8, 8]
# repeats = 3
# res = []
# for i in list_:
#     if list_.count(i) >= repeats and i not in res:
#         res.append(i)
# print(res)

#Задание 29
# list_ = [1, 2, 3]

# for x in list_:
#     for y in list_:
#         for z in list_:
#             if x != y and y != z and z != x:
#                 print((x, y, z))

#Задание 30
# K = 3
# matrix = []
# for i in range(K):
#     matrix.append([])
# for t in range(0, K):
#     matrix[i].append(0)
# print(matrix)


#Задание 31
# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# res = []
# for i in colors:
#     res.append(i[::-1])
# print(sorted(res, key = len))

#Задание 32
# list_ = [1,2,3,4,5,6,7,8,9,0]
# step = 2
# element = 'A'
# i = step
# while i <= len(list_):
#     list_.insert(i, element)
#     i = i + step + 1
# print(list_)


