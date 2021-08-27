class BaseProduct:
    name_type = None

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Burger(BaseProduct):
    name_type = 'Burger'

    def __str__(self):
        return f'{self.name_type} : {self.name} - {self.price}'


class Pizza(BaseProduct):
    name_type = 'Pizza'

    def __init__(self, name, price, size):
        super(self, name, price)
        self.size = size

product_1 = Pizza('Pizza', 250)
product_2 = Burger('burger', 450)

print(product_1.name, product_1.price)
print(product_2)
print(BaseProduct.name_type)
