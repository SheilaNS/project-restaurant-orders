import csv
from collections import Counter


def get_most_ordered(orders, customer):
    customer_orders = [order[1] for order in orders if order[0] == customer]
    return Counter(customer_orders).most_common()[0][0]


def get_customer_count_dish(orders, customer, dish):
    custumer_orders = [
        order[1]
        for order in orders
        if order[0] == customer and order[1] == dish
    ]
    return len(custumer_orders)


def get_never_ordered_dishes(orders, customer):
    dishes = set(order[1] for order in orders)
    customer_orders = set(order[1] for order in orders if order[0] == customer)
    return dishes - customer_orders


def get_never_visited_days(orders, customer):
    days = set(order[2] for order in orders)
    customer_days = set(
        order[2] for order in orders if order[0] == customer
    )
    return days - customer_days


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, mode="r", encoding="utf-8") as file:
            orders = [*csv.reader(file)]
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    maria_most_ordered_dish = get_most_ordered(orders, "maria")
    count_arnaldo_burgers = get_customer_count_dish(
        orders, "arnaldo", "hamburguer"
    )
    joao_never_ordered_dishes = get_never_ordered_dishes(orders, "joao")
    joao_never_visited_days = get_never_visited_days(orders, "joao")

    with open("data/mkt_campaign.txt", mode="w", encoding="utf-8") as file:
        file.write(
            f"{maria_most_ordered_dish}\n"
            f"{count_arnaldo_burgers}\n"
            f"{joao_never_ordered_dishes}\n"
            f"{joao_never_visited_days}\n"
        )
