from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/")
DB_NAME = "ecommerce"
COLLECTION_NAME = "orders"

def load_orders(data):
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    result = collection.insert_many(data)
    print(f"Inserted {len(result.inserted_ids)} documents.")
