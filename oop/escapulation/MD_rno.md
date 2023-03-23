## Задание 1

Создайте класс A и объявите в нём 3 метода:

    публичный(public) (возвращает строку 'Public method'),
    защищённый(protected) (возвращает строку 'Protected method')
    приватный(private) (возвращает строку 'Private method')

Затем создайте экземпляр в переменной obj1 данного класса и вызовите (с выводом в терминал) по очереди каждый из методов. Не забудьте, что нужно вызвать приватный метод так, чтобы ошибка не выводилась

```py
class A:
    def public(self):
        return 'Public method'

    def _protected(self):
        return 'Protected method'

    def __private(self):
        return 'Private method'

obj1 = A()
print(obj1.public())
print(obj1._protected())
print(obj1._A__private())
```
> чтобы вытащить приватный метод, то можно сослаться на класс и вытащить оттуда его метод