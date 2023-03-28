# # import datetime
# # date = '31/12/2021'

# # res2 = date.split('/')
# # res2 = list(reversed(res2))
# # res2 = [int(i) for i in res2]
# # res3 = datetime.date(res2[0], res2[1], res2[2])

# # now_1 = datetime.date.today()


# # print(res3)

# # print(now_1)

# # dict1 = {3: 'сходить в кино', 2: 'сделать домашку', 1: 'выгулять собаку'}
# # num = sorted(dict1)
# # res = []
# # for i in num:
# #     for k,v in dict1.items():
# #         if i == k:
# #             res.append(dict1.items())
# # print(res)
# # print(list(dict1.items()))


# # res = sorted(dict1)

# # print(res)

# # date = '31/12/2021'

# # res2 = date.split('/')
# # # res2 = list(reversed(res2))
# # print(res2)


# # class A:
# #     def __init__(self, name) -> None:
# #         self.extensions = name

# # a = A('hello')
# # print(dir(a))

# '''
# Создайте класс Money, объекты которого имеют аттрибуты country и symbol. Наследуйте от него классы Dollar и Euro. У данных методов должна быть переменная класса rate, курс к сому, Dollar - 84.80, Euro - 98.40. Добавьте к этим классам метод exchange, который принимает количество которое нужно обменять в переменную amount и возвращает такую строку:
# '''

# class Money:
#     def __init__(self,country,symbol):
#         self.country = country
#         self.symbol = symbol
# class Dollar(Money):
#     rate = 84.80
#     def exchange(self, amount):
#         return f"$ {amount} равен {Dollar.rate * amount} сомам" 

# class Euro(Money):
#     rate = 98.40
#     def exchange(self, amount): 
#         return f"€ {amount} равен {Euro.rate * amount} сомам" 
# dol = Dollar('Alaska', '$') 
# eu = Euro('France', '€') 

# print(dol.exchange(100)) 
# print(eu.exchange(80))


# 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   


# res = lambda x: x ** 10
# print(res(2))

lst = [3, 3, 2]

target = 6
res = []
for i in lst:
    for inner in lst:
        # print(lst.index(i))
        # print(lst.index(inner))
        if lst.index(i) != lst.index(inner):
            if i+inner == target:
                print(lst.index(i))

class Solution:
    def twoSum(self, nums, target):
        for ind, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in nums:
                if ind != nums.index(num2):
                    return [ind, nums.index(num2)]
                
import datetime
t = datetime.time.now()
print(t)
