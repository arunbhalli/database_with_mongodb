
import pymongo
# importing pymongo and connecting with mongodb-----------
print('welcome to mongodb')
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client.list_database_names())
