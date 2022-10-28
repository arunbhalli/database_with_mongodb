import pymongo
# insertion
print('Finding data by using crud')
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['friendsdb']
collection = db['friends']
# -------------update data----------------
updateOne =collection.update_one({'name':'Anoop'},
{'$set':{'age':24}})

#-----------Unset--------------------
# unsetone =collection.update_one({'name':'Anoop'},
# {'$unset':{'age':''}})
alldocs =collection.find({},{'_id':0})
alldocs =collection.find({'age':24},{'_id':0})
for i in alldocs:
  print(i)