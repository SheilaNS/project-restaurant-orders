import csv
from collections import Counter


def get_most_ordered(orders, customer):
    customer_orders = [order[1] for order in orders if order[0] == customer]
    return Counter(customer_orders).most_common()[0][0]


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, mode="r", encoding="utf-8") as file:
            orders = [*csv.reader(file)]
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    maria_most_ordered_dish = get_most_ordered(orders, "maria")

    with open("data/mkt_campaign.txt", mode="w", encoding="utf-8") as file:
        file.write(f"{maria_most_ordered_dish}\n")
