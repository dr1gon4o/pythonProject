from typing import List

from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    valid_waiters = {"FullTimeWaiter": FullTimeWaiter, "HalfTimeWaiter": HalfTimeWaiter}
    valid_clients = {"RegularClient": RegularClient, "VIPClient": VIPClient}

    def __init__(self):
        self.waiters: List[BaseWaiter] = []
        self.clients: List[BaseClient] = []
        # self.waiters = []
        # self.clients = []

    def hire_waiter(self, waiter_type, waiter_name, hours_worked):
        if waiter_type not in {"FullTimeWaiter", "HalfTimeWaiter"}:
        # if waiter_type not in self.valid_waiters:
            return f"{waiter_type} is not a recognized waiter type."
        if any(waiter.name == waiter_name for waiter in self.waiters):
            return f"{waiter_name} is already on the staff."
        waiter = self.valid_waiters[waiter_type](waiter_name, hours_worked)
        self.waiters.append(waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type, client_name):
        if client_type not in {"RegularClient", "VIPClient"}:
        # if client_type not in self.valid_clients:
            return f"{client_type} is not a recognized client type."

        if any(client.name == client_name for client in self.clients):
            return f"{client_name} is already a client."
        client = self.valid_clients[client_type](client_name)
        self.clients.append(client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name):
        for waiter in self.waiters:
            if waiter.name == waiter_name:
                return waiter.report_shift()
        return f"No waiter found with the name {waiter_name}."

    def process_client_order(self, client_name, order_amount):
        for client in self.clients:
            if client.name == client_name:
                points_earned = client.earning_points(order_amount)
                return f"{client_name} earned {points_earned} points from the order."
        return f"{client_name} is not a registered client."

    def apply_discount_to_client(self, client_name):
        for client in self.clients:
            if client.name == client_name:
                discount_percentage, remaining_points = client.apply_discount()
                client.points = remaining_points  # updatvane
                return f"{client_name} received a {discount_percentage}% discount. Remaining points {remaining_points}"
        return f"{client_name} cannot get a discount because this client is not admitted!"

    def generate_report(self):
        total_earnings = sum(waiter.calculate_earnings() for waiter in self.waiters)
        total_client_points = sum(client.points for client in self.clients)
        clients_count = len(self.clients)
        waiters_details = sorted(self.waiters, key=lambda w: w.calculate_earnings(), reverse=True)
        waiters_report = "\n".join([str(waiter) for waiter in waiters_details])
        return f"$$ Monthly Report $$\n" \
               f"Total Earnings: ${total_earnings:.2f}\n" \
               f"Total Clients Unused Points: {total_client_points}\n" \
               f"Total Clients Count: {clients_count}\n" \
               f"** Waiter Details **\n{waiters_report}"
