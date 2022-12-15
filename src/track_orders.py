from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        customer_orders = [
            order[1] for order in self.orders if order[0] == customer
        ]
        return Counter(customer_orders).most_common()[0][0]

    def get_never_ordered_per_customer(self, customer):
        dishes = set(order[1] for order in self.orders)
        customer_orders = set(
            order[1] for order in self.orders if order[0] == customer
        )
        return dishes - customer_orders

    def get_days_never_visited_per_customer(self, customer):
        days = set(order[2] for order in self.orders)
        customer_days = set(
            order[2] for order in self.orders if order[0] == customer
        )
        return days - customer_days

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
