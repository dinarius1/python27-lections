'================================List================================'
# Список - это изменяемый, итерируемый, индексируемый и упорядоченный тип данных, предназначенный для хранения элементов в строгом порядке. 

list1 = [1,3.5, 'hello', [],  (1,2), None, True, False] - любые типы данных можно положить в список
list1[0]  #10
list1[3]  #[1,2,3]
list1[3][-1]  #3 - так как 3 элемент - это список, то можно ссылать на этот 2 список через индекс
list1[2][-1]  # 'o'

Список и функция список! 
Когда мы говорим о функции list - то мы не можем перебрать цифры, так как у функции слишком мало информации для этого, поэтому лучше использовать функци. range
list2 = list('hello')
print(list2)   #['h','e', 'l', 'l', 'o'], он перебирает строку на элементы

list(100)  #выдается ошибка тк нельзя вывести 0 (пустоту), поэтому можно конечно возвести 100 в строку, но есть и доугой способ:
print(list(5))
print(list(range(3,10,2)))

'==========================Неизменяемость=========================='
string = 'hello'
res = string.upper()
print(string)  #'hello'
print(res)  #'HELLO'

list1 = []
list1.append(1)
list1.append(2)
list1.append(3)
print(list1)  #[1,2,3]

Поэтому список является изменяемым типом данных, его методы ссылаются на тот же изначальный список, там к них один и тот же адрес

'===========================Методы списков==========================='
# append - метод, который добавляет элемент в конце списка
list1 = []
list1.append('hello')
list1.append(500)
print(list1) # ['hello', 500]

# remove - метод, который удаляет элемент из списка по значению, но только первого вхождения этого элемеента.

- Выдаст ошибку если такого элемеента нет в списке
- С данным методом нельзя использовать с инлексом
- Удаляет первый заданный элемент, который он нашел
list = [10, 'hello', 500, 'word', 1000, 'hello', 500]
list.remove('hello')
print(list2)  # 10, 500, 'word', 1000, 'hello', 500]

# pop - метод, который удаляет элемент из списка по индексу если этого индекста нет, выдаст IndexError
list3 = [10,20,30,40,50]
list.pop()
print(list3) #[10,20,30,40]
list3.pop(1)  #удаление по индексу
print(list3) #[10,30,40, 50]
#также метод pop возвращает удаленный элемент
list4 = [10,20,30,40,50]
popped = list4.pop(0)         #можем дать любое название этой переменной. комп видит что до этого был исполльзован метод pop и введена переменная, поэтому и такой результат
print(list4) #[20,30,40,50]
print(popped) #10

Нельзя использовать метод pop c пустыми списками!

# insert - метод, который добавляет элемент в список по индексу
list5 = [1,2,3,4]
list5.insert(0, 'hello')
print(list5)  # ['hello', 1,2,3,4]

#count - считает кол во элемента, который передаем в метод в спискке
list1 = [1,2,3,4,5,6, 1, 2, 1] 
list1.count(1) #4 - тк у нас единиц 4 в списке
list1.count('hello') #0 - нет хеллоу в списке

#index - возрващаеь инлекс данного элемента
list2 = ['hello', ]

# sort - метод, который сортирует по возрастанию
# если передать .sort(reverse=True), то сортирует по убыванию
list3 = [34,12,67,12,89,45]
list3.sort()
print(list3) # [12, 12, 34, 45, 67, 89]
list3.sort(reverse=True)
print(list3) # [89, 67, 45, 34, 12, 12]
# list3.sort()
# list3.reverse()

list4 = ['a', 'c', 'b', 'B', 'A']
list4.sort()
print(list4) # ['A', 'B', 'a', 'b', 'c']

list5 = [10, 'b', 3, 'c', 5]
# list5.sort() 
# TypeError: '<' not supported between instances of 'str' and 'int'

# copy - возвращает копию списка
list1 = [1,2,3]
list2 = list1.copy()
list2.append(4)
print(list1)
print(list2)

# extend - расширяет список другим списком
list1 = [1,2,3,4]
list2 = [5,6,7,8]
# list1.append(list2)
# list1  [1,2,3,4, [5,6,7,8]]

list1.extend(list2)
# list1  [1,2,3,4,5,6,7,8]

#Решение задачи:
print(list1[::-1]) 

list1 = [1,2,3,4,5,6] #создание списка
list1 = list(range(1,11)) #создание списка

list1 = [1,2,3,4,5,6]
print(list(reversed(list1)))
#у нас есть функция reverse и метод reverse
#метод reverse - list1.reverse()
#функция reversed - list(reversed(list1))

