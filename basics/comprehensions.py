"====================Comprehensions (генератор)===================="
# Генератор, с помощью которого можно создавать помледовательность, используя цикл for
list1 = []
for i in range(1,11):
    list1.append(i)
#list1 = [1,2,3,4,5,6,7,8,9,10]
list1 = [i for i in range(1,11)]  #мы  в начале написали i, чтобы добавить в список
print()

# Синтаксис генератора:
# результат for элемент in последовательность
# результат for элемент in последовательность if фильтр

comprehensions = (i for i in range(1,11))
# print(comprehensions)
# <generator object <genexpr> at 0x7f502e3c2500>
# генератор - итерируемый объект, который не хранит в себе полностью все элементы последовательности, а генерирует их когда требуется

print(next(comprehensions))

#next() - это функция которая принимает в себе генератор, запрашивает следующий элемент у генератора и вохвращает его 

comprehensions = (i for i in range(1,11))
print(list(comprehensions))  
print(list(comprehensions))  #не получится, тк генератор единоразовый 

"========================Синтаксический сахар========================"
# - то есть это тот же самый генератор, только тк мы все оборачиваем в [], то он понимает, что нужно выводить список. так назыввется, тк как имеется в виде простой ситаксис
#list comprehension
list_compr = [i for i in 'hello']
print(list_compr)

#dict comrehension
dict_compr = {i : str(i) for i in range(1,11)}
print(dict_compr)  #{1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10'}

#фильтр if
string = 'Hello WorlD'
res = [i for i in string if i.islower()]
print(res)

"=========================Set Comprihension========================="
set_comp = {x for x in range(10)}
print(set_comp)




# list1 = [i for i in range(1,11) if i % 2 == 0]
# print(list1)
# list1 = [i for i in range(0,11,2)]
# list1.pop(0)
# print(list1)

#Задачка1
# создать списко от 1 до 10, но умноженные на 100
list1 = [i * 100 for i in range(1,11)]
print(list1)

#Задачка2
list_ = ['hello']
list2 = ['hello' for i in range(5)]  # мы в ранж пишем сколько раз нужно вывести 'hello'

#Задачка3
users = ['test1', 'test2', 'test3']
list3 = ['Hello ' + i for i in users]
print(list3)
list4 = [f'Hello {i}' for i in users]
print(list4)

#Задачка4 
# Нужно вывести: [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]] 
list5 = [[x for x in range(1,i + 1)] for i in range(1,6)] 
#мы сначала пишем for i in range(1,6) - это позволяет нам понять с количеством элементов, с которым мы будем работать (в нашем случае у мы должны вывести 5 элементов с диапозоном в зависмости от того какой порядок у этого элемента)
# мы пишем именно range(1,6) - так как будем потом работать с чисоами в диапозоне
#затем мы до этого комприхенша мы пишем, что должно вывести, вводя новый комприхеншен

print(list5)

#Как вытащить вложенный список из списка с помощью генератора? 
#В гите у Насти взять!!!!!!!!!!!!!

dict1 = {'a' : 1, 'b' : 2, 'c' : 3}
#1 способ
dict2 = {v:k  for k,v in dict1.items()}
print(dict2)

#2 способ
dict1 = {'a' : 1, 'b' : 2, 'c' : 3}
res = {}
for k,v in dict1.items():
    res.update({v:k})    #через данный метод можно добавлять элементы, точнее айдейтим, а туда можем записать и словарь
    res[v] = k  #мы тут пишем, что ключ со значением v равег ключу с его значением
print(res)

#Задачка5
# Нужно вывести : {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}
#1 способ
res = {i : [x for x in range(1,i + 1)] for i in range(1,6)}
#2 способ
list5 = [[x for x in range(1,i + 1)] for i in range(1,6)] 
list8 = [i for i in range(1,6)]
dict_ = dict(zip(list8, list5))
print(dict_)



    


