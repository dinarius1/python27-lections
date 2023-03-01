# from functools import reduce
# def len_(list1):
#   res = sorted(list1, key = len)
#   return res[-1]
# result = reduce(len_(), ['kate', 'nil', 'a'])
# print(result)

# 7) Есть глобальная переменная, которая обозначает размер самой главной первой матрешки. Напишите функцию, в которой к размеру главной матрешки прибавляется размер второй матрешки, который определен в этой функции. То же самое сделайте и с третьей функцией внутри второй. Верните результат сложения.

big = 10
def toy():
  global big
  middle = 8
  big = big + middle
  def toy2():
    nonlocal big
    small = 5
    big = big + small
  return big
print(toy())

#новое решение
# big = 10
# def toy():
#   global big
#   middle = 8
#   big = big + middle
#   def toy2():
#     global big
#     small = 5
#     big = big + small
#   toy2()
#   return big
# print(toy())


from functools import reduce
# def len_():
#   res = sorted(list1, key = len)
#   return res[-1]
# print(list(reduce(len_(), ['kate', 'nil', 'a'])))


names = ['kate', 'nil', 'a']

print(reduce(lambda x,y: x if len(x)>len(y) else y, ['kate', 'nil', 'a']))