from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    air_cons = 0.9

    def drive(self, distance):
        total = (self.fuel_consumption + Car.air_cons) * distance

        if total <= self.fuel_quantity:
            self.fuel_quantity -= total

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    air_cons = 1.6

    def drive(self, distance):
        total = (self.fuel_consumption + Truck.air_cons) * distance

        if total <= self.fuel_quantity:
            self.fuel_quantity -= total

    def refuel(self, fuel):
        fuel = 0.95 * fuel
        self.fuel_quantity += fuel


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
