# Task 1
# import json
# with open('test.json') as f:
#     python_obj = json.loads(f.read())
# with open('task.py', 'a+') as f2:
#     print(python_obj)
#     f2.write(python_obj)
#     f2.seek(0)
#     f2.read()

# #Верное решение
# # import json 
# # file1 = open('task1.json') 
# # python_obj = json.loads(file1.read()) 
# # file1.close() 

# # with open('task1.py', 'w') as file2: 
# #     file2.write(str(python_obj))      #почему нам надо в формат str его хаписывать? разве смысл задания тогда не измениться?


# #Task 6
# # import json
# # json_products = '[{"title":"iphone","price":700,"rating":4.8},{"title":"asus","price":1300,"rating":3.9},{"title":"macbook pro","price":1500,"rating":4.9},{"title":"samsung","price":150,"rating":5.0}]'
# # python_products = json.loads(json_products)
# # python_products2 = [i['title'] for i in python_products if i["rating"] > 4]
# # print(python_products2)


# Task 7
# import json
# with open('test.json') as f:
#     python = json.loads(f.read())
#     json2 = []

#     for dict_ in python:
#         print(dict_.update({'description': '...'}))
#         json2.append(dict_)
#     print(json2)
# with open('test.json') as f2:
    # json.dump(json2, f2)

# # 2 способ

# # import json
# # with open('db.json') as f:
# #     python = json.loads(f.read())
# #     json2 = ["description":"..." for i in python for inner in i]
# # with open('new_db.json') as f2:
# #     json.dump(json2, f2)

# # Правильное решение
# # import json
# # with open('test.json') as f:
# #     python = json.loads(f.read())
# #     for i in python:
# #         i['discription'] = 'black'
# # with open('new_db.json', 'w+') as f2:
# #     json.dump(python, f2)


# #Task 8
# # [
# #   {
# #     "id": 1,
# #     "title": "iphone",
# #     "price": 700,
# #     "rating": 4.8
# #   },
# #   {
# #     "id": 2,
# #     "title": "asus",
# #     "price": 1300,
# #     "rating": 3.9
# #   },
# #   {
# #     "id": 3,
# #     "title": "macbook pro",
# #     "price": 1500,
# #     "rating": 4.9
# #   },
# #   {
# #     "id": 4,
# #     "title": "samsung",
# #     "price": 150,
# #     "rating": 5.0
# #   }
# # ]

# # import json
# # with open('test.json') as f:
# #     new = json.loads(f.read())
# #     for i in new:
# #         if i['id'] == 3:
# #             new.remove(i)
# #     print(new)

# # with open('new_db.json', 'w+') as f2:
# #     json.dump(new,f2)

# #Task 9
# import json
# def  create_new(id, title, description, price, rating):
#     new = {'id' : id, 'title' : title, 'description' : description, 'price' : price, 'rating' : rating}
#     with open('db.json') as f:
#         new2 = json.load(f.read())  #почему так нельзя писать
#         new2.append(new)
#     with open('new_db.json', 'w+') as f2:
#         f2.write(new2)   #почему так нельзя писать
        
# print(create_new(3,'apple', 'red', 80, 4.5))

# import json 
# def create_new(id: int, title: str, description: str, price: int, rating:float) -> None: 
#     dict_={'id':id, 'title':title, 'description':description, 'price':price, 'rating':rating} 
#     with open('db.json') as file: 
#         res = json.load(file)
#         res.append(dict_) 
#         with open('new_db.json', 'w') as f: 
#             f.write(json.dumps(res)) 
# create_new(10, 'assa', 'asd', 12, 25.0)


# #Task 10
# [{'id': 4, 'title': 'samsung', 'price': 150, 'rating': 5.0}, {'id': 3, 'title': 'macbook pro', 'price': 1500, 'rating': 4.9}, {'id': 1, 'title': 'iphone', 'price': 700, 'rating': 4.8}, {'id': 2, 'title': 'asus', 'price': 1300, 'rating': 3.9}]

import json
def get_sorted(json_filename: str):
    with open(json_filename) as f:
        res = json.loads(f.read())
        # res.sort(reverse=True, key=lambda x: x['rating']) - 2 способ решения
#         ratings = [i['rating'] for i in res]
#         ratings.sort(reverse = True)
#         new = []

#         # for i in res:
#         #     for number in ratings:
#         #         if i['rating'] == number:
#         #             new.append(i)
        # return new
        for number in ratings:
            for i in res:
                if i['rating'] == number:
                    new.append(i)
        return new
# get_sorted('db.json')
# print(get_sorted('db.json'))

import json

def update(id: int, title: str=None, price: int=None, rating: float=None) -> None:
    with open('db.json') as f:
        obj = json.load(f)

    for prod in obj:
        if prod['id'] == id:
            for name, val in zip(
                ['title', 'price', 'rating'],
                [title, price, rating]
            ):
                if val is not None:
                    prod[name] = val
            break

    else:
        raise ValueError

    with open('new_db.json', 'w') as f:
        json.dump(obj, f)   
    
# #Task 14

# bulk_create([{'id': 100, 'title': 'product1', 'price': 1500, 'rating': 4.6}, {'id': 101, 'title': 'product2', 'price': 2004, 'rating': 1.2}, {'id': 102, 'title': 'product3', 'price': 2095, 'rating': 2.1}, {'id': 103, 'title': 'product4', 'price': 3200, 'rating': 5.0}])

# new_db.json = [
#     {'id': 1, 'title': 'iphone', 'price': 700, 'rating': 4.8},
#     {'id': 2, 'title': 'asus', 'price': 1300, 'rating': 3.9}, 
#     {'id': 4, 'title': 'samsung', 'price': 150, 'rating': 5.0}, {'id': 3, 'title': 'samsungXL', 'price': 1500, 'rating': 5.0}, {'id': 6, 'title': 'samsungXXL', 'price': 15000, 'rating': 5.0}, {'id': 100, 'title': 'product1', 'price': 1500, 'rating': 4.6}, {'id': 101, 'title': 'product2', 'price': 2004, 'rating': 1.2}, {'id': 102, 'title': 'product3', 'price': 2095, 'rating': 2.1}, {'id': 103, 'title': 'product4', 'price': 3200, 'rating': 5.0}]

import json
def bulk_create(products):
    with open('db.json') as f:
        old = json.load(f)
        id_ = [i['id'] for i in old]

        for el in products:
            if el['id'] not in id_:
                old.append(el)
    with open('new_db.json', 'w') as f2:
        json.dump(old, f2)

bulk_create([{'id': 100, 'title': 'product1', 'price': 1500, 'rating': 4.6}, {'id': 101, 'title': 'product2', 'price': 2004, 'rating': 1.2}, {'id': 102, 'title': 'product3', 'price': 2095, 'rating': 2.1}, {'id': 103, 'title': 'product4', 'price': 3200, 'rating': 5.0}])
