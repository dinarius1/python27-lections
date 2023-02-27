x = int(input())
y = int(input())
res1 = x % y
res2 = x // y
if res1 != 0:
    print(f'Частное: {res2}')
    print(f'Остаток: {res1}')
elif res1 == 0:
    print(f'Частное: {res2}')

Про 19 задание еще себе написать !!! Решение, там есть свои особенности

20 задание:
a = int(input())
b = int(input())
c = int(input())
if a + b > c:
    print('yes')
elif a + c > b:
    print('yes')
elif b + c > a:
    print('yes')
else:
    print('no')

Задание 21
a = int(input())
b = int(input())
c = int(input())
if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
    print('rectangular')
elif a ** 2 > b ** 2 + c ** 2 or b ** 2 > a ** 2 + c ** 2 or c ** 2 > a ** 2 + b ** 2:
    print('acute')
elif a ** 2 < b ** 2 + c ** 2 or b ** 2 < a ** 2 + c**2 or c ** 2 < a ** 2 + b ** 2:
    print('obtuse')
else:
    print('impossible')

a = int(input())
b = int(input())
c = int(input())
if a + b > and a + c > b and b + c> a:
    if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
        print('rectangular')
    elif a ** 2 > b ** 2 + c ** 2 or b ** 2 > a ** 2 + c ** 2 or c ** 2 > a ** 2 + b ** 2:
        print('acute')
    else:
        print('obtuse')
else:
    print('impossible')

Задание 22
n = int(input())
one = n // 10
two = n % 10
if two == 1 or one == 1 and two < 0:
    print(f'На лугу пасется {n} корова')
elif two == 0 or one <= 9 and two < 0:
    print(f'На лугу пасется {n} коров')
else:
    print(f'На лугу пасется {n} коровы')

n = int(input())
one = n // 10
two = n % 10
if two == 1 or one == 1 and two < 0:
    print(f'На лугу пасется {n} корова')
elif two == 0 or one <= 9 and two < 0:
    print(f'На лугу пасется {n} коров')
else:
    print(f'На лугу пасется {n} коровы')

    