from etl.transform import transform_orders

def test_transform_orders():
    mock_data = [
        {"quantity": "2", "price": "10.5"},
        {"quantity": "3", "price": "5.0"}
    ]
    result = transform_orders(mock_data)
    assert result[0]["total"] == 21.0
    assert isinstance(result[1]["price"], float)
    assert isinstance(result[1]["quantity"], int)
