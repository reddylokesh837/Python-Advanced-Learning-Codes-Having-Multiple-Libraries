from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://reddylokesh837:WP1M8vw14ueYe4Bd@cluster0.brhof.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"




connection = MongoClient(uri, server_api=ServerApi('1'))


database_obj = connection['lokesh']

collection_obj = database_obj['student']


# documents =[
#     {'Name':'Loki', 'id ': 23, 'course':'Python', 'year':2013},
#     {'Name':'Raj', 'id ': 24, 'course':'Java', 'year':2014},
#     {'Name':'Ravi', 'id ': 25, 'course':'JavaScript', 'year':2015},
#     {'Name':'Ramesh', 'id ': 26, 'course':'Data Science', 'year':2016},
#     {'Name':'Lokesh', 'id ': 27, 'course':'Machine Learning', 'year':2017},
#     {'Name':'Ravi', 'id ': 28, 'course':'AI', 'year':2018},
#     {'Name':'Ramesh', 'id ': 29, 'course':'Cloud Computing', 'year':2019},
#     {'Name':'Lokesh', 'id ': 30, 'course':'Data Analysis', 'year':2020}
# ]





# returnValue = collection_obj.insert_many(documents)

# print(returnValue.inserted_ids)


print('Find one document')
doc =collection_obj.find_one()
print(doc)

print("All documents")
docs = collection_obj.find({'course':'Python'})
for doc in docs:
    print(doc)