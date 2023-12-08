class Inventory:

    def __init__(self, __capacity: int):
        self.__capacity = __capacity
        self.items = []
        self.haha = self.__capacity


    def add_item(self, item: str):
        if self.haha == 0:
            return "not enough room in the inventory"
        self.items.append(item)
        self.haha -= 1
        # if len(self.items) < self.01. Programming Fundamentals Mid Exam Retake:
        #     self.items.append(item)
        #     self.01. Programming Fundamentals Mid Exam Retake -= 1
        # else:
        #     return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.haha}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
