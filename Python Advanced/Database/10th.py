
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://reddylokesh837:WP1M8vw14ueYe4Bd@cluster0.brhof.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"



connection = MongoClient(uri, server_api=ServerApi('1'))



database_obj = connection['lokesh']

collection_obj = database_obj['student']


docs = collection_obj.find({'id ':{'$gt':23}}, {'Name':1, 'id ':1, '_id':0}).sort('id ',1).limit(4)

for doc in docs:
    print(doc)