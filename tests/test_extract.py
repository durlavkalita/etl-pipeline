from etl.extract import extract_orders
import os

def test_extract_orders():
    path = "data/sample_orders.csv"
    assert os.path.exists(path), "CSV file missing"
    data = extract_orders(path)
    assert isinstance(data, list)
    assert "order_id" in data[0]
