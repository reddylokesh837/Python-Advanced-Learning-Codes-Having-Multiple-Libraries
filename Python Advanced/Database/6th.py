from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://reddylokesh837:WP1M8vw14ueYe4Bd@cluster0.brhof.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
try:
    connection = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    connection.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    exit(1)  # Exit if connection fails

# Now accessing the database and collection
try:
    database_obj = connection["lokesh"]  # Accessing the database
    collection_obj = database_obj["student"]  # Accessing the collection
    
    # Retrieving and printing one document from the collection
    collection_obj.insert_one({'name': 'Lokesh', 'id': 23})
    collection_obj.insert_one({'name': 'Raj', 'id': 24})
    document = collection_obj.find()
    if document:
        print("Found a document:", document)
    else:
        print("No documents found in the collection.")
except Exception as e:
    print(f"Error interacting with MongoDB: {e}")

finally:
    connection.close()  # Ensure the connection is closed at the end
