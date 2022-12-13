from connector import Connector


class Product:
    id: int
    title: str
    price: float
    count: int
    category: int

    def __init__(self, data_json):
        self.id = data_json.get('id')
        self.title = data_json.get('title')
        self.price = data_json.get('price')
        self.count = data_json.get('count')
        self.category = data_json.get('category')

    def __bool__(self):
        """
        Проверяет есть ли товар в наличии
        """
        return bool(self.count)

    def __len__(self):
        """
        Возвращает количество товара на складе
        """
        return self.count

    def __str__(self):
        return f'\nТовар:{self.title} c id:{self.id} стоимостью:{self.price} в наличии:{self.count}\n'


class Category:
    id: int
    title: str
    description: str
    products: list

    def __init__(self, data_json):
        self.id = data_json.get('id')
        self.title = data_json.get('title')
        self.description = data_json.get('description')
        self.products = data_json.get('products')

    def __bool__(self):
        """
        Проверяет есть ли товар в категории
        """
        return bool(self.id)

    def __len__(self):
        """
        Возвращает количество наименований товаров, у которых есть наличие на складе
        """
        return len([x for x in self.products if self.products['count']])

    def __str__(self):
        return f'\nid:{self.id} - Категория:{self.title} - Описание:{self.description}\n'


class Shop:
    """ Класс для работы с магазином """
    # products: list
    # categories: list

    def __init__(self, *args, **kwargs):
        pass

    def get_categories(self):
        """
        Показать все категории пользователю в произвольном виде, главное, чтобы пользователь
        мог видеть идентификаторы (id) каждой категории
        """
        return [print(Category(x)) for x in Connector('categories.json').select({})]

    def get_products(self):
        """
        Запросить номер категории и вывести все товары, которые относятся к этой категории
        Обработать вариант отсутствия введенного номера
        """
        req = input('Введите номер категории: ')

        if not req.isdigit:
            print ('Принимаются только числа')

        else:
            return [print(Product(x)) for x in Connector('products.json').select({'category':int(req)})]

    def get_product(self):
        """
        Запросить ввод номера товара и вывести всю информацию по нему в произвольном виде
        Обработать вариант отсутствия введенного номера
        """
        req = input('Введите номер товара: ')

        if not req.isdigit:
            print ('Принимаются только числа')

        else:
            [print(Product(x)) for x in Connector('products.json').select({'id':int(req)})]

if __name__=='__main__': 

    shop = Shop()
    shop.get_categories()
    shop.get_product()
    shop.get_products()