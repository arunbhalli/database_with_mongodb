import pymongo
# insertion
datalimit =int(input('Enter no of friends to so there data:- '))
print('Information of friends')
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['friendsdb']
collection = db['friends']


#---sort-----

#alldocs =collection.find({},{'_id':0})
alldocs =collection.find({},{'_id':0}).sort('age')
# -------------limit-------------
alldocs =collection.find({},{'_id':0}).sort('age').limit(datalimit)
for i in alldocs:
  print(i)
