# Protocols
> **HTTP** - Hyper Text Transfer Protocol, протокол, который построин на протоколах **IP/TCP**.

> **HTTPS** - более новая версия HTTP, где появилось шифрование и SSL сертификаты

## HTTP методы
* **GET** - метод для получения данных
* **POST** - метод для отправки данных на создание 
* **PUT** - полное обновление или создание (если не найдет что обновлять, то он просто создаст это обновлять)
* **PATCH** - чистичное обновление (с помощью него можно в  целом все обновить, не только какую то часть)
* **DELETE** - удаление
* TRACE - трассировка (проверка связи), все начинается с него, чтобы проверить свзязь живая или нет
* HEAD - получение headers для запроса
* OPTIONS - получение списка методов на данную url

# Status Code
* 1ХХ - информационные (получение информации между сервисом и клиентом)
* 2ХХ - успешные 
200 - ОК - успешно заработал (получил данные)
* 3ХХ - перенаправление (клик по ссылке и в других случаях как необходимо )
* 4ХХ - ошибки клинта (фронтендщика) 
400 - некорректные данные (со стороны клиента ошибка)
404 - сслыка непрвильная
* 5ХХ - ошибки сервера - сервер умер

# URL
> URL (Uniform Resourse Locator) - имя адресной ссылки
`https://www.google.com/search?q=hello`

> **DOMAIN** - уникальное название, к которому прикреплен какой то определенный сервер (ip adress) 
`www.google.com` - пример домена

> **URI** - подпуть `/search` ( все что написано после http:// - 34.173.115.25/api/v1/products/)

> **Query Params** - пары ключ-значения, идут после ? 

ДОПИСАТЬ ГИТХАБ