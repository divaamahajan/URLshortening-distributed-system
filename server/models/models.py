"""
A model,is typically used in the context of an application's code to represent and 
interact with the data stored in a MongoDB collection. 

It acts as an abstraction layer between the application code and the database, 
providing methods for querying, updating, and manipulating the data. 

The model often encapsulates  the logic for interacting with the database, 
including CRUD (Create, Read, Update, Delete) operations and data validation.
"""

#  collection_name is created in the database configs
class UrlMappingModel:
    def __init__(self, collection_name):
        # self.client = MongoClient(uri)
        # self.db = self.client[db_name]
        # self.collection = self.db[collection_name]
        self.collection = collection_name

    def get_short_url(self, long_url: str) -> str:
        mapping = self.collection.find_one({"long_url": long_url})
        return mapping['short_url'] if mapping else None

    def get_long_url(self, short_url: str) -> str:
        mapping = self.collection.find_one({"short_url": short_url})
        return mapping['long_url'] if mapping else None

    def insert_url_mapping(self, short_url: str, long_url: str) -> None:
        self.collection.insert_one({"short_url": short_url, "long_url": long_url})
