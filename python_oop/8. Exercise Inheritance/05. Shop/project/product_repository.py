from typing import List

from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        # for product in self.products:
        #     if product.name == product_name:
        #         self.products.remove(product_name)

        product = self.find(product_name)

        if product:
            self.products.remove(product)

    def __repr__(self):
        return f"\n".join(f"{p.name}: {p.quantity}" for p in self.products)
