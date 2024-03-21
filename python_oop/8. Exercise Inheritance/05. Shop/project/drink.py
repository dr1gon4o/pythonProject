from project.product import Product


class Drink(Product):
    quantityy = 10

    def __init__(self, name):
        super().__init__(name, self.quantityy)
