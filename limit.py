import pymongo
# insertion
datalimit =int(input('Insert no of friends to so there data:- '))
print('Information of friends according to input numbers:')
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['friendsdb']
collection = db['friends']

# -------------limit-------------
alldocs =collection.find({},{'_id':0}).sort('age').limit(datalimit)
for i in alldocs:
  print(i)