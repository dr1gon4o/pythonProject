from typing import List
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:

    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvdd = None

        for x in self.dvds:
            if x.id == dvd_id:
                dvdd = x

        for cust in self.customers:
            if cust.id == customer_id:
                if dvdd in cust.rented_dvds:
                    return f"{cust.name} has already rented {dvdd.name}"

                if dvdd.is_rented:
                    return "DVD is already rented"

                if cust.age < dvdd.age_restriction:
                    return f"{cust.name} should be at least {dvdd.age_restriction} to rent this movie"

                dvdd.is_rented = True
                cust.rented_dvds.append(dvdd)
                return f"{cust.name} has successfully rented {dvdd.name}"
            # self.dvds.append(dvdd)

    def return_dvd(self, customer_id, dvd_id):
        dvdd = None

        for x in self.dvds:
            if x.id == dvd_id:
                dvdd = x

        for cust in self.customers:
            if cust.id == customer_id:
                if dvdd in cust.rented_dvds:
                    cust.rented_dvds.remove(dvdd)
                    dvdd.is_rented = False
                    return f"{cust.name} has successfully returned {dvdd.name}"
                return f"{cust.name} does not have that DVD"

    def __repr__(self):
        hoho = '\n'.join(str(d) for d in self.customers)
        hoho2 = '\n'.join(str(d) for d in self.dvds)

        return f"{hoho}\n" \
               f"{hoho2}"


