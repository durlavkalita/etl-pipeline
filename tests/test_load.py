from unittest.mock import patch, MagicMock
from etl.load import load_orders

@patch("etl.load.MongoClient")
def test_load_orders(mock_mongo):
    mock_collection = MagicMock()
    mock_mongo.return_value.__getitem__.return_value.__getitem__.return_value = mock_collection

    test_data = [{"order_id": 1, "product": "Test", "quantity": 1, "price": 10, "total": 10}]
    load_orders(test_data)
    mock_collection.insert_many.assert_called_once()
