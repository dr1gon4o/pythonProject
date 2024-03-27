class Category:

    def __init__(self, x_id: int, name: str):
        self.id = x_id
        self.name = name

    def edit(self, new_name: str):
        self.name = new_name

    def __repr__(self):
        return f"Category {self.id}: {self.name}"
