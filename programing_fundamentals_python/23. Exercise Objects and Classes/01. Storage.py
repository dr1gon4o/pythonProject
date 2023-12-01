
class Storage:
    # storage = []

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product: str):
        if self.capacity > 0:
            self.capacity -= 1
            self.storage.append(product)

    def get_products(self):
        return self.storage

#     def get_products(self):
#         return Storage.storage


storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())

