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
    def __init__(self, collection_name, memcache_client):
        self.collection = collection_name
        self.memcache = memcache_client

    # def get_short_url(self, long_url: str) -> str:
    #     mapping = self.collection.find_one({"long_url": long_url})
    #     return mapping['short_url'] if mapping else None

    # def get_long_url(self, short_url: str) -> str:
    #     mapping = self.collection.find_one({"short_url": short_url})
    #     return mapping['long_url'] if mapping else None

    # def insert_url_mapping(self, short_url: str, long_url: str) -> None:
    #     self.collection.insert_one({"short_url": short_url, "long_url": long_url})
        
    def get_short_url(self, long_url: str) -> str:
        # Check cache first
        cached_short_url = self.memcache.get(long_url)
        if cached_short_url:
            return cached_short_url.decode('utf-8')

        # If not found in cache, check database
        mapping = self.collection.find_one({"long_url": long_url})
        if mapping:
            short_url = mapping['short_url']
            # Cache the result for future use
            self.memcache.set(long_url, short_url)
            return short_url
        else:
            return None
        

    def get_long_url(self, short_url: str) -> str:
        # Check cache first
        cached_long_url = self.memcache.get(short_url)
        if cached_long_url:
            return cached_long_url.decode('utf-8')

        # If not found in cache, check database
        mapping = self.collection.find_one({"short_url": short_url})
        if mapping:
            long_url = mapping['long_url']
            # Cache the result for future use
            self.memcache.set(short_url, long_url)
            return long_url
        else:
            return None


    def insert_url_mapping(self, short_url: str, long_url: str) -> None:
        # Insert data into the database
        self.collection.insert_one({"short_url": short_url, "long_url": long_url})
        # Update cache with the new mapping
        self.memcache.set(long_url, short_url)
        self.memcache.set(short_url, long_url)
