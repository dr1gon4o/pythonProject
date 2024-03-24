from project.animal import Animal


class Tiger(Animal):
    # care = 45
    # def __init__(self, name,gender, age):
    #     super().__init__(self.care)

    def __init__(self, name,gender, age):
        super().__init__(name, gender, age, money_for_care=45)