from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop(Product):
    __file_name = 'products.txt.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            pprint(file.read())

    def add(self, *product):
        with open(self.__file_name, 'a') as file:
            if self.name in file:
                print('Продукт уже есть в магазине')
            else:
                file.write(self.name)



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')




