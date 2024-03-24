


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price <= self.__budget and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        # elif len(self.animals) < self.__animal_capacity:
        #     return "Not enough budget"
        if self.__animal_capacity and self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for workerr in self.workers:
            if workerr.name == worker_name:
                self.workers.remove(workerr)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"


    def pay_workers(self):
        sum = 0
        for workk in self.workers:
            sum += workk.salary

        if self.__budget >= sum:
            self.__budget -= sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):

        sum2 = 0
        for animm in self.animals:
            sum2 += animm.money_for_care

        if self.__budget >= sum2:
            self.__budget -= sum2
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        haha = {'Lion': [], 'Tiger': [], 'Cheetah': []}

        for x in self.animals:
            haha[x.__class__.__name__].append(str(x))

        # return f"You have {len(self.animals)} animals\n" \
        #        f"----- {len(haha['Lion'])} Lions:\n" \
        #        f"{haha['Lion']}\n" \
        #        f"----- {len(haha['Tiger'])} Tigers:\n" \
        #        f"{haha['Tiger']}\n" \
        #        f"----- {len(haha['Cheetah'])} Cheetahs:\n" \
        #        f"{haha['Cheetah']}"

        # tova e vtori variant za print.. po lesno kato se polzva join za \n na vsiako izrechenie sled zapetaiata
        final = [f"You have {len(self.animals)} animals",
                 f"----- {len(haha['Lion'])} Lions:", *haha['Lion'],
                 f"----- {len(haha['Tiger'])} Tigers:", *haha['Tiger'],
                 f"----- {len(haha['Cheetah'])} Cheetahs:", *haha['Cheetah']]

        return '\n'.join(final)

    def workers_status(self):
        haha2 = {'Keeper': [], 'Caretaker': [], 'Vet': []}

        for x in self.workers:
            haha2[x.__class__.__name__].append(str(x))

        # return f"You have {len(self.workers)} workers\n" \
        #        f"----- {len(haha2['Keeper'])} Keepers:\n" \
        #        f"{haha2['Keeper']}\n" \
        #        f"----- {len(haha2['caretaker'])} Caretakers:\n" \
        #        f"{haha2['caretaker']}\n" \
        #        f"----- {len(haha2['Vet'])} Vets:\n" \
        #        f"{haha2['Vet']}"

        # kato vtori variant
        final = [f"You have {len(self.workers)} workers",
                 f"----- {len(haha2['Keeper'])} Keepers:", *haha2['Keeper'],
                 f"----- {len(haha2['Caretaker'])} Caretakers:", *haha2['Caretaker'],
                 f"----- {len(haha2['Vet'])} Vets:", *haha2['Vet']]

        return '\n'.join(final)