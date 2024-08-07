import time
import random
from pymongo import MongoClient
import numpy as np

def connect_to_mongo(uri, db_name):
    client = MongoClient(uri)
    return client[db_name]

def insert_documents(db, collection_name, num_docs):
    collection = db[collection_name]
    documents = [{"key": i, "value": random.random()} for i in range(num_docs)]
    start_time = time.time()
    collection.insert_many(documents)
    duration = time.time() - start_time
    return duration

def read_documents(db, collection_name, num_docs):
    collection = db[collection_name]
    start_time = time.time()
    for i in range(num_docs):
        collection.find_one({"key": i})
    duration = time.time() - start_time
    return duration

def run_benchmark(uri, db_name, collection_name, num_docs):
    db = connect_to_mongo(uri, db_name)
    insert_time = insert_documents(db, collection_name, num_docs)
    read_time = read_documents(db, collection_name, num_docs)
    return insert_time, read_time

if __name__ == "__main__":
    uri = "mongodb://localhost:27017/"
    db_name = "benchmark_db"
    collection_name = "test_collection"
    num_docs = 1000

    insert_time, read_time = run_benchmark(uri, db_name, collection_name, num_docs)
    print(f"Insert Time: {insert_time:.2f} seconds")
    print(f"Read Time: {read_time:.2f} seconds")
