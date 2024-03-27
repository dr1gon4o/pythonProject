class Equipment:
    id = 1

    def __init__(self, name : str):
        self.name = name
        self.id = Equipment.id

    @staticmethod
    def get_next_id():
        curreq = Equipment.id
        Equipment.id +=1
        return curreq

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

