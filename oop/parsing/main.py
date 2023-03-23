import requests
import re    #модуль, который позволяет ...
from bs4 import BeautifulSoup as BS
from typing import List  #импортировали из форматирования typing

class BaseParser:
    BASE_URL : str  #мы указади типизацию, тип данного BASE_URL, благодаря этому код не ругается
    query_param: str = 'q'  #query_param - название поискового ключа
    
    @staticmethod  #так как мы не будем его изменять, его по идее можно выкинуь за глобальное пространство
    def get_soup(url: str) -> BS:
        html = requests.get(url).text
        return BS(html, 'lxml')
    
    # @staticmethod    - есть  еще такое  решение, но он не самое лучшее
    # def format_title(title : str) -> str:
    #     return title.replace('\r', '').replace('\t', '').replace('\n', ' ')
    
    @staticmethod
    def format_title(title: str) -> str:
        return " ".join(title.replace("\r", "").replace("\t", "").split())
    
    @staticmethod
    def format_price(price: str) -> str:
        return int(re.search('\d+', price).group(0)) #group(0) - позволяет найти первый элемент из переменной

    '''
    def search - является главной функцией
    '''
    def search(self,query : str) -> List[dict]: #query - поисковое слово
        'принимает поисковое слово и возвращает список со всеми результатами' #то, что написано сверху - это документация
        return self.get_product(f'{self.BASE_URL}?{self.query_param}={query}')

    
    def get_product(self, url: str) -> List[dict]:  #List[dict] - означает, что в списке будут словари
        soup = self.get_soup(url)
        products = self._get_products_list(soup)
        results = []
        for product in products:
            product_info = self._get_product_info(product)
            results.append(product_info)
        return results
    
    def _get_products_list(self, soup : BS) -> List[BS]:
        "метод, в котором ищутся все блоки с продуктами" 
        raise NotImplementedError  #мы специально вызываем ошибку, чтобы мы помнили, что нужно обязательно переписать данный метод. Ведь у всех сайтов разный код, поэтому невозмоэно созать единый шаблон
    
    def _get_product_info(self,  soup : BS) -> dict:
        'метод в котором ищется title, price продукта'



class KivanoParser(BaseParser):
    BASE_URL = 'https://www.kivano.kg/product/index'
    query_param = 'search'

    def _get_products_list(self, soup: BS) -> List[BS]:
        return soup.find_all('div', {'class' : 'product_listbox'})
    
    def _get_product_info(self, soup: BS) -> dict:
        title = soup.find('div', {'class': 'listbox_title'}).text
        price = soup.find('div', {'class': 'listbox_price'}).text
        return {'title' : self.format_title(title), 'price' : self.format_price(price)}

print(KivanoParser().search('кубик'))
# [{'title': '\nНасадка для нарезки кубиками Kenwood KAX-400\n', 'price': '\n13578 сом\n'}]

class KulikovParser(BaseParser):
    BASE_URL = 'https://site.kulikov.com/katalog'
    

    def _get_products_list(self, soup: BS) -> List[BS]:
        return soup.find_all('div', {'class' : 'product-item'})
    
    def _get_product_info(self, soup: BS) -> dict:
        title = soup.find('h3', {'class' : "product-item-title"}).text
        price = soup.find('span', {'class' : "product-item-price-current"}).text
        return {'title' : self.format_title(title), 'price' : self.format_price(price)}

print(KulikovParser().search('торт'))  #KulikovParser() - пишем в данном случае со скобками, так как мы создаем объект, но мы просто не оборачиваем его в какую то переменную

'''
Вывод:

[{'title': 'Торт "Nutella" гранд (1,150 кг)', 'price': 1190}, {'title': 'Торт "Эстерхази" (0,650 кг)', 'price': 990}, {'title': 'Торт "Фисташковый" с малиной (0,650 кг)', 'price': 890}, {'title': 'Торт-сет "Ореховый" (0,540 кг)', 'price': 150}, {'title': 'Торт -сет "Бисквитно-ягодный" (0,570 кг)', 'price': 690}, {'title': 'Торт «Шварцвальд» гранд плюс (1,800 кг)', 'price': 1750}, {'title': 'Торт-сет «Ассорти» (0,750 кг)', 'price': 850}, {'title': 'Торт «Красный бархат» гранд плюс', 'price': 1450}, {'title': 'Торт «Кудрявый пинчер» гранд плюс', 'price': 1850}, {'title': 'Торт "Медовик с орехами" гранд', 'price': 890}, {'title': 'Торт "Медовик с орехами" гранд плюс', 'price': 1350}, {'title': 'Торт "Malina" классик', 'price': 890}]
'''



    