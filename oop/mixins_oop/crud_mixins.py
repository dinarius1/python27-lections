class CreateMixin:
    def product_create(self, title,price):
        #self.__class__ - обращение к классу, который наследовался от этого миксина
        model = self.__class__   #теперь в model - класс ProductCrud
        obj = model()
        _id = model._id
        obj.title = title
        obj.price = price
        obj.id = _id
        model.objects[_id] = obj
        model._id += 1

class ReadMixin:
    def product_details(self, p_id):
        model = self.__class__ 
        obj = model.objects.get(p_id)
        print({"id": obj.id, "title": obj.title, "price": obj.price})
        
class UpdateMixin:
    def product_update(self, p_id, title, price):
        model = self.__class__
        obj = model.objects.get(p_id)
        #перезаписываем значения 
        obj.title = title
        obj.price = price

class DeleteMixin:
    def delete_product(self, p_id):
        model = self.__class__
        model.objects.pop(p_id)

class ProductCrud(CreateMixin, ReadMixin, UpdateMixin, DeleteMixin):
    objects = {}
    _id = 1

crud = ProductCrud()
crud.product_create('Samsung Note 20 Ultra', 50000)
# crud.product_details(1) 
#{'id': 1, 'title': 'Samsung Note 20 Ultra', 'price': 50000}
crud.product_create('Iphone 14 Pro Max', 100000)
crud.product_details(1) 
crud.delete_product(2)
crud.product_details(2) 
#выходит ошибка, так как нет такого атрибута, ибо мы его удалили
# AttributeError: 'NoneType' object has no attribute 'id'

# crud.product_update(2,'Iphone 14 Pro Max', 120000)
# crud.product_details(2) 


