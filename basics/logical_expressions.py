
"===================Логические и условные операторы==================="
# логические операторы - выражения, которые возвращают True, если выражение верное, False - если не верное

# print()
# Знак присвоения: =
# знак сравнения: ==
# знак неравенства: !=
# знак больше: >
# знак больше или равно: >=    (всегла идет сначала стрела)

# Нельзя сравнивать разные типы данных, слова в разных регистрах
# print('5' == 5)  - False
# print("Hello" == 'hello')  - False

"============================AND OR NOT============================"
# and - и
# or - или
# not - не
# print(not True)  -> False
# print(not False)  -> True
"===========================Boolean Type==========================="
ДОПИСАТЬ!!!!!!

В булевом значении есть ряд особенностей:
бул всегда показыввает Неправду, если:
1. это 0
2. bool() - это пустота (внутри функции не будет ничего)
3.  bool([]) - это пустой список  - Неправда

бул показыввает Правду, если:
1. bool(' ') - пробел является тоже символом!!  - Тру
2. bool([[]]) - это не пустой список, в нем есть еще один список, т.е он не пустой!!!  - Правда

'==============================NoneType=============================='
# None - это неизменяемый ТИП ДАННЫХ с одним значением None (пустота), который используется для обозначения пустоты - поэтому он False
# print(bool(None))  -> False
# print(bool('None')) -> True
Лучше в None использовать is!!
Is - показывает сущность двух сравнивающих выражений
== - больше показывает математическое сравнение
Например:
a = [1,2,4]
b = [1,2,4]
a == b # True
a is b #False, так как у них разные айди, они находятся в разных ячейках данных
"==========================Условные операторы========================"
# Условный оператор - это конструкция, которая используется для того,чтобы при разных входных данных код работал по разному (в зависимости от условия).

if условие1:
    тело1
    #тело1 будет исполняться только если условие верно

различнеф другие возможные кострукции с if, elif, else.....

Особенности условных операторов:
1. В 1 констуркции мы можем только 1 раз использовать команду if
2. В 1 конструкции мы можем использовать неограниченное число elif или же его не использовать вообще
3. В 1 конструкции мы можем использовать только один раз else или же его не использовать вообще

num = int(input())
if num > 0:
    print(f'число {num} - положительное')

password = input('придумайте свой пароль: '):
if not len(password) >= 8:
    print('ваш пароль меньше 8 символов')

"============================Тернарные операторы==================="
# Тернарные операторы - это условие в одну строку
# Его синтаксис: тело1 if условие else тело2

num = int(input())
res = 'Hello' if num == 5 else 'Bye'
print(res)
