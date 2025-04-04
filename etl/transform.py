def transform_orders(data):
    for row in data:
        row["quantity"] = int(row["quantity"])
        row["price"] = float(row["price"])
        row["total"] = row["quantity"] * row["price"]
    return data