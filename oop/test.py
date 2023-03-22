# import datetime
# date = '31/12/2021'

# res2 = date.split('/')
# res2 = list(reversed(res2))
# res2 = [int(i) for i in res2]
# res3 = datetime.date(res2[0], res2[1], res2[2])

# now_1 = datetime.date.today()


# print(res3)

# print(now_1)

# dict1 = {3: 'сходить в кино', 2: 'сделать домашку', 1: 'выгулять собаку'}
# num = sorted(dict1)
# res = []
# for i in num:
#     for k,v in dict1.items():
#         if i == k:
#             res.append(dict1.items())
# print(res)
# print(list(dict1.items()))


# res = sorted(dict1)

# print(res)

# date = '31/12/2021'

# res2 = date.split('/')
# # res2 = list(reversed(res2))
# print(res2)


class A:
    def __init__(self, name) -> None:
        self.extensions = name

a = A('hello')
print(dir(a))