from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
# declarative_base - она создает класс

# driver://user:password@host:port/db_name - чтобы подключиться к postgresql, используем данный шаблон
db_url = 'postgresql://user:1@127.0.0.1:5432/sqlalchemy_test'
engine = create_engine(db_url)
#подключение к базе данных

Base = declarative_base()
# базовый класс для таблиц

#создаем таблицу
class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key= True)
    title = Column(String)
    price = Column(Integer)

    def __repr__(self): #rpr именно, а не str, так как у нас спиок элементов
        return f'({self.id} -> {self.title})'

Base.metadata.create_all(bind=engine) 
#записываем таблицу в баду данных

SessionLocal = sessionmaker(bind=engine)
#создаем класс для сессий (один объект от данного класса - одна сессия)

session = SessionLocal()
#создаем сессию

new_product = Product(title='product1', price = 220)
#создаем продукт на уровне Питоне (запись в таблицу)
# поэтому необходимо для орм создать запрос на запись в таблицу

# session.add(new_product)
#добавляем запрос в сессию

# session.commit()
# сохраняем изменения и отправляем набор запросов бд

products = session.query(Product).all()
#получаем все записи из таблицы Product
print(products)

# session.add(Product(title='product2', price=34))
# session.add(Product(title='product3', price=245))
# session.add(Product(title='product4', price=45))
# session.add(Product(title='product5', price=345))
# session.commit()

res = session.query(Product).filter(Product.price > 100).all()
#получаем все записи из таблицы Product, у которого цена больше 100
print(res)

product3 = session.query(Product).get(3)
# получаем продукт под id 3
print(product3)

product4 = session.query(Product).get(4)
# получаем продукт под id 4
# session.delete(product4)
#удаляем продукт

# session.commit()
#сохранияем изменения в бд

product3.title = 'new title'
product3.price = 100
#изменяем продукт. Update. Обновляем наш продукт

session.commit()
#сохранияем изменения в бд

'''
При запуске файла в терминале мы лишь добавляем изменения к прошлым данным, мы не запускаем новый файл, мы лишь запускаем старый файл с новыми изменениями

Поэтомы мы можем удалить это из файла после его запуска
# session.add(Product(title='product2', price=34))
# session.add(Product(title='product3', price=245))
# session.add(Product(title='product4', price=45))
# session.add(Product(title='product5', price=345))
# session.commit()

Так как терминал уже получил новые данные
'''



