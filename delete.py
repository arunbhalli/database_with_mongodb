import pymongo
# insertion
print('Information of friends')
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['friendsdb']
collection = db['friends']
# -------------deleteing data----------------
#deletedname= collection.delete_one({'name':'Akash'})
#alldocs =collection.find({},{'_id':0})
alldocs =collection.find({'age':24},{'_id':0})
for i in alldocs:
  print(i)