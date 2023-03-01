# b = 10
# c = 11
# try:
#     print(a)
# except NameError:
#     print('Такой переменной не существует!')

# num1 = int(input())
# num2 = int(input())
# try:
#     print(num1 + num2)
# except Exception as e:
#     print(e)


# num1 = int(input())
# num2 = int(input())
# try:
#     num1+num2
# except ValueError:
#     print('Введите число!')
# else:
#     print(num1+num2)

#Задание 5
# try:
#     dict_ = {'key1': 'value1', 'key2': 'value2'}
#     print(dict_['c'])
# except KeyError:
#     print("Нет такого ключа!")

#а вот тут уже все правильно:
# dict_ = {'key1': 'value1', 'key2': 'value2'}
# try:
#     print(dict_['key1'])
# except KeyError:
#     print("Нет такого ключа!")

# list_ = [1, 4, 9, 16, 25, 36] 
# try:
#     print(list_[33])
# except IndexError:
#     print("Нет такого элемента!")

#Задание 7
#обясните пожалуйстаааааа
# try: 
#     age = int(input()) 
#     if age < 18: 
#         raise ValueError('Доступ запрещён') 
# except ValueError: 
#     print('Введён некорректный возраст') 
# else: 
#     print('Спасибо') 

# try:
#     num1 = int(input())
#     num2 = int(input())
#     print(num1 / num2)
# except (TypeError,ValueError):
#     print("Произошла ошибка!")

# #Задание 9
# try:
#     cash = int(input())
#     if cash < 0:
#         raise ValueError("Сумма не может быть отрицательной!")  # - сюда нельзя писать, так как в таком случае мы не можем использовать except. Если что то сюда запишем, то у нас все равно данный текст замениться на текст в except
# except ValueError as e:
#     print(e)  #поэтому сюда пишем "(Сумма не может быть отрицательной!"), так как except видит любые ошибки, в том числе и ValueError
# else:
#     print(cash)

# try:
#     cash = int(input())
#     if cash < 0:
#         raise ValueError
# except:
#     print("Сумма не может быть отрицательной!")
# else:
#     print(cash)

# list_ = [1, 2, 3]
# try:
#     list_.get(1)
# except AttributeError:
#     print('Ошибка')

# try:
#     string = 'd'
#     num = 1
#     print(string + num)
# except TypeError:
#     print('Unsupported option')

# try: 
#     for x in range(10): 
#         list_.append(x) 
# except NameError: 
#     print([0,1,2,3,4,5,6,7,8,9])

# try:
#     list_ = [1, 2, 3, 4]
#     for i in range(0, len(list_) + 1):
#         print(list_[i])
# except IndexError:
#     print('ошибка')

# Создайте переменную password, который будет содержать пароль в виде строки. Вызовите исключение ValueError, если пароль меньше 6 символов

# try:
#     password = 'short'
#     if len(password) < 6:
#         raise ValueError
# except ValueError:
#     print('Ошибка')
# else:
#     print(password)

# try: 
#     password = 'short' 
#     if len(password) < 6: 
#         raise ValueError() 
# except ValueError: 
#     raise ValueError

#Задание 15
# try:
#     warehouse = [
#     ['1', '2', '3'],
#     [1, 2],
#     [[1], [2], [3]],
#     [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}]]
#     if len(warehouse) > 10:
#         raise TypeError
#     for i in warehouse:
#         if len(i) > 3:
#             raise TypeError
# except TypeError:
#     print("Склад переполнен")
# else:
#     print(warehouse)

# try:
#     inp1 = input()
#     for i in inp1:
#         list(list_).append(int(i))
# except raise Exception(' Данный элемент не является числом!')
# else:
#     print(list_)


# dict_ = {'key1': 'value1', 'key2': 'value2'}

# dict_ = {(1,2,3,[1,2,3]):5}

# print(dict_)


# try: 
#     age = int(input()) 
#     if age < 18: 
#         raise ValueError('Доступ запрещён') 
# except ValueError: 
#     print('Введён некорректный возраст') 
# else: 
#     print('Спасибо') 
# finally:
#     print("До свидания!")

# try:
#     age = int(input()) 
#     if age < 18: 
#         raise Exception('Доступ запрещён') 
# except ValueError: 
#     print('Введён некорректный возраст') 
# except Exception as e:
#     print(e)
# print('Ya prodojau rabotat')

# age = int(input()) 
# if age < 18: 
#     raise Exception('Доступ запрещён') 

#Задание 15
# warehouse = [
#     ['1', '2', '3'],
#     [1, 2],
#     [[1], [2], [3]],
#     [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],
# ]

# for i in warehouse:
#     if len(warehouse)>10 or len(i)>3:
#         raise ValueError

#Задание 18
def filter_comment(comment,banlist=['hate', 'unlike']):
    ban_list = ['hate', 'unlike']
    list1 = comment.split() 
    for i in list1:
        if i in ban_list:
            raise Exception("Ваш комментарий отправлен на перепроверку, так как, возможно, содержит неблагоприятный контекст")
        else:
            return comment
print(filter_comment('I hate sweets'))
        
# comment = input()
# ban_list = ['hate', 'unlike']
# list1 = comment.split() 
# for i in list1:
#     if i in ban_list:
#         raise Exception("Ваш комментарий отправлен на перепроверку, так как, возможно, содержит неблагоприятный контекст")
# print(comment)
        