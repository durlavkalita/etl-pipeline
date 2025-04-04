import csv

def extract_orders(csv_path: str):
    with open(csv_path, newline='') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]