"==========================Пакеты и модули=========================="
# Module - это любой файл с раширением .py
# from test import a
# print(a)  #hello из файла test

# import test
# print(test.a)

#package - набор модулей (в папке обязательно должно быть..... )

"==========================Работа с файлами=========================="
# open - функция, которая позволяет открывать файлы в определенном режиме
# r - read (тольео для чтения)
# w - write (только для перезаписи, каждый раз при открытии очищает файл и позволяет вписывать новую информацию)
# a - append (только для дозаписи, добавляется в конец)
# x - создает файл, но если файл уже есть - ошибка
# b - бинарный вид

"================================Read================================"
file = open('test.txt')
# если такого файла нет, то выйдет ошибка
# необходимо запускать файл, находясь в той папке, где находится этот файл
# если не указать режим, то по умолчанию откроется в режиме чтения. чтобы указать режим, то нужно во 2 аргументе указать в кавычках название режима ("a")

print(dir())



# closed - метод, которые возвращае булевое значение по поводу того, закрыт файл или нет

# name - метод, передает название файла, в котором мы сейчас
print(file.name) 

#readable, writable - метод, которые возвращае булевое значение по поводу того, можем ли мы сейчас чиать/ писать

print('readable', file.readable()) #True

print(file.read()) #читает с начала до конца
print(file.read()) # '' - потому что каретка в конце файла
file.seek(0) #через данный метод, мы можем указать откуда считывать. чтобы указать откуда читать, то указываем индекс символа откуда надо

file.seek(0)
print(file.read(5))  #читаем только Hello
print(file.read())   #считываем от 5 и до конца - World Makers

file.seek(0)
print(file.readline())  #считывает Hello до \n - т.е до переноса
print(file.readline())  #считывает World до \n - т.е до переноса

file.seek(0)
print(file.readline(2))  #считывает до элемента которого мы написал внури функции

file.seek(0)
print(file.readlines()) #['Hello\n', 'World\n', 'Makers\n']

file.seek(10)
print(file.tell()) #каретка находится на 10 символе

print(file.closed)  #False
file.close()  # !важно закрывать файлы, пишем его в конце
print(file.closed) #True

"===============================Write==============================="
file = open('new_file.txt', 'w')
#если файла нет - создает
#если есть - очищает

#readable, writable - метод, которые возвращае булевое значение по поводу того, можем ли мы сейчас чиать/ писать

print('readable', file.readable()) #False
print('writable', file.writable()) #True

#file.read()
#в режиме записи нельзя читать, тоже самое в режиме чтения (нельзя писать)

file.write('Hello ')
file.write('World')
#Hello World

file.writelines(['Hello', 'World'])
file.writelines(['\nNew', '\nWorld'])
#Hello World HelloWorld
#New
#Line

file.seek(0)
file.write('AAA')
#AAAlo World HelloWorld   - код презаписывает строку
#New
#Line

file.close()

"===============================Append==============================="
file = open('new_file2.txt', 'a')
# если файла нет,то создается новый

print('readable', file.readable()) #False
print('writable', file.writable()) #True

file.write('Hello')
#дозапись идет в конце файла (старые данные не удаляются)

file.seek(0)
file.write('New')
#дозапись илет в конец файла, так как мы в режиме append

file.close()

"========================Контекстный менеджер========================"
# try:
#     file = open('aaa', 'w')
#     file.read()
# finally:
#     file.close()

with open('test.txt') as f:
    f.read()
    f.seek(0)
#файл сразу закрывается после того как мы вышли из режима with
print(f.closed)