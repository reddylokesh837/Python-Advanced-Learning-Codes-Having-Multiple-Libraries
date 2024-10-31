
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://reddylokesh837:WP1M8vw14ueYe4Bd@cluster0.brhof.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"



connection = MongoClient(uri, server_api=ServerApi('1'))



database_obj = connection['lokesh']

collection_obj = database_obj['student']

# collection_obj.insert_one({'Name':'Reddy', 'id ':23, 'course': 'HTML', 'year':2014})

# collection_obj.update_one({'Name':'Reddy'}, {'$set':{'id ':27}})


collection_obj.update_many({'Name': {'$eq':'Lokesh'}}, {'$set': {'id ':25}})

docs = collection_obj.find({'Name':'Lokesh'}, {'_id':0, 'course':0, 'year':0})

for doc in docs:
    print(doc)