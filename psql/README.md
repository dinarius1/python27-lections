# Slash commands
* \l - посмотреть список всех базы данных (бд)
* \c - показывает через какого юзера и к какой бд мы подключены
* \c name_of_db - подключение к какой то бд
* \du - список всех юзеров в postgres
* \dt - список всех таблиц в текущей бд
* \d+ - список всех таблиц в текущей бд с более подробной инфой
* \d+ name_of_table - более подробная инфа о таблице
* \q - выход из субд (psql)

## Термины
postgres - 1. это база данных 2. название юзера postgres
1. субд - система управления бд - по факту это psql, где мы в основном работаем 
2. бд - база данных
3. таблица

# Создание бд и талиц
```sql
CREATE DATABASE name_of_db
-- создание базы данных
```
```sql
CREATE TABLE name_of_table(
    column1 data_type1,
    column1 data_type2,
    ...
);
-- создание таблицы с полями
```

# Заполнение таблиц
```sql
INSERT INTO name_of_table VALUES -- можно писать и с маленькой буквой
-- VALUES - ключевое слово, которое позволяет добавлять какие то значения в таблицу
(val1, val2),
(val_1, val_2);
-- запись данных в таблицу (заполнение всех полей)
```
# Удаление данных из бд
```sql
DROP DATABASE name_of_db;
-- удаление бд

DROP TABLE name_of_table;
-- удаление таблицы
```

# Вывод данных из таблицы
```sql
SELECT * FROM name_of_table;
-- вывод всех записец со всеми полями, так как написали *

SELECT column1, column 2 FROM name_of_table;
-- вывод конкретных полей
```

# Условие 
- используется не только с удалением, но и с select
```sql
DELETE FROM name_of_table WHERE condition;
-- удаление всех записей из таблицы соответсвующих данному условию 

delete from product where price = 100;
-- удалились продукты, цена которых 100
-- строгое равенство

SELECT * FROM name_of_table WHERE name_of_column LIKE '%hello%';
-- записи включающие в себя данную строку с учетом регистра
-- aaahello
-- hello world
-- hello
-- Hello world  - не пройдет (потому что регистр другой) 

SELECT * FROM name_of_table WHERE name_of_column ILIKE '%hello%';
-- записи включающие в себя данную строку без учета регистра
-- aaahello
-- hello world
-- hello
-- Hello world 
-- HeLLo

select * from product where title like '%iphone%';
-- вывод продуктов, где название продукта начинается с iphone, и выведиться все айфоны, где есть слово "iphone". Т.е like - позволяет вывести все похожие запросы
```

```sql
SELECT * FROM name_of_table ORDER BY name_of_column;
-- сортировака записей по данному полю в порядке возрастания
```

```sql
SELECT * FROM name_of_table ORDER BY name_of_column DESC;
-- сортировака записей по данному полю в порядке убывания
```

```sql
SELECT * FROM name_of_table LIMIT 10;
-- вывод первых 10 записей, т.е LIMIT - устанавливает какого то ограничение (усвлоие ограничение)
```

```sql
SELECT * FROM name_of_table OFFSET 10;
-- пропускаем первые 10 записей
```

```sql
SELECT * FROM name_of_table LIMIT 10 OFFSET 5;
-- пропускаем первые 5 записей
-- вытаскиваем 10 записей
```

# Обновление таблицы

```sql
ALTER TABLE name_of_table ADD COLUMN col_name col_type constraint;
-- добавляем новую колонку в таблицу

ALTER TABLE name_of_table DROP COLUMN col_name;
-- удаляем колонку из таблицы

ALTER TABLE name_of_table RENAME COLUMN col_name TO new_col_name;
-- переименновывание колонки

ALTER TABLE name_of_table ALTER COLUMN col_name SET DATA TYPE new_type;
-- изменение типа данных у поля
```

# Ограничения
* `UNIQUE` - не разрешает дубликаты
* `NOT NULL` - требует обязательного заполнения поля
* `PRIMARY KEY` - как UNIQUE и NOT NULL + строит бинарное дерево (binaty tree) для быстрого поиска
* `FOREIGN KEY` - ссылается на PRIMARY KEY в другой таблице и проверяет, существет ли такое id

1. UNIQUE
```sql
shop=# create table test (
shop(# id serial,
shop(# field varchar(50) unique
shop(# );
```
2. NOT NULL
```sql
alter table test add column not_null_field varchar(10) not null;
```

# Связи
## Виды связей
> Один к одному (one to one)
* один человек - один профиль
* один автор - одна автобиография

> Один ко многим (one to many)
* один блоггер - много постов
* одна марка - много моделей
* одна страна - много областей
* одна земля - много языков

> Многие ко многим (many to many)
* один разработчик - много проектов. один проект - много разработчиков
* один человек - много языков. один язык - много носителей этого языка

## Реализация one to many в postgres
```sql
CREATE TABLE blogger (
    id serial PRIMARY KEY,
    name varchar(50),
    age int
);

CREATE TABLE post (
    id serial PRIMARY KEY,
    title varchar(100),
    body text,
    blogger_id int,

    CONSTRAINT fk_post_blogger
    FOREIGN KEY (blogger_id) REFERENCES blogger (id)
);
```

# JOINS
> **JOIN** - иснтрукция, которая позволяет одним SELECT брать данные из двух таблиц (у которых есть связанные поля)

> **INNER JOIN (классический JOIN)** - достаются только те записи, у которых есть данные в обоих таблицах

> **FULL JOIN** - достаются все записи и с первой таблицы и со второй
```sql
blog=# select post.title, post.body,
blogger.name, blogger.email, blogger.age
from post full join blogger
on blogger.id = post.blogger_id;
 title  | body |   name   |     email      | age 
--------+------+----------+----------------+-----
 post 1 | ...  | bloger 3 | ccc@gmail.com  |  26
 post 2 | aaa  | bloger 2 | bb@gmail.com   |  18
 post 3 | ---  | bloger 1 | aa@gmail.com   |  23
 post 4 | aaaa | bloger 4 | gggg@gmail.com |  23
 post 5 | ---  |          |                |    
(5 rows)

```


