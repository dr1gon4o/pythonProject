from typing import List

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:

    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):

        # haha = [str(x) for x in self.subscriptions]
        # haha2 = [str(x) for x in self.customers]
        # haha3 = [str(x) for x in self.trainers]
        # haha4 = [str(x) for x in self.equipment]
        # haha5 = [str(x) for x in self.plans]
        # return f"{''.join(haha)}\n" \
        #        f"{''.join(haha2)}\n" \
        #        f"{''.join(haha3)}\n" \
        #        f"{''.join(haha4)}\n" \
        #        f"{''.join(haha5)}\n"

        final = []
        result = [self.subscriptions, self.customers, self.trainers, self.equipment, self.plans]

        for i in result:
            for el in i:
                if el.id == subscription_id:
                    final.append(str(el))
                    break

        return '\n'.join(final)
