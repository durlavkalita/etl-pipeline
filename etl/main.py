from extract import extract_orders
from transform import transform_orders
from load import load_orders

def run_etl():
    data = extract_orders("data/sample_orders.csv")
    transformed = transform_orders(data)
    load_orders(transformed)

if __name__ == "__main__":
    run_etl()
