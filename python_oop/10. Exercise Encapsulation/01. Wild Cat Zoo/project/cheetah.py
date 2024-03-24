from project.animal import Animal


class Cheetah(Animal):

    def __init__(self, name,gender, age):
        super().__init__(name, gender, age, money_for_care=60)

    # def __init__(self, name, gender, age):
    #     # def __init__(self, name: str, gender: str, age: int, money_for_care=0):
    #     #     super().__init__(name, gender, age, money_for_care)
    #     #     self.money_for_care = 60
    #     super().__init__(name, gender, age, money_for_care=50):
    #     # self.money_for_care = 60