#  Below code is available in Mongo-Connect
from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://admin:test123@cluster0.5cm4d9a.mongodb.net/?retryWrites=true&w=majority"

# Create a new client to establish a connection to the MongoDB server
client = MongoClient(uri)

# Access or create a database within the MongoDB server
db = client.url_short_db

# Access or create a collection within the db database
collection_name = db["url_short_collection"]


# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)