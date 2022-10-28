import pymongo
# insertion
print('Information of friends')
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['friendsdb']
collection = db['friends']

# finding data by using find_one

one = collection.find_one({'name':'Akash'})
print(one)

# finding data by using find for all related data

#finding all data by using for loop
# alldocs =collection.find({},{'_id':0,'name':1})
# for i in alldocs:
#   print(i)
# -------------deleteing data----------------
# deletedname= collection.delete_one({'name':'Akash'})

#-----------Unset--------------------
unsetone =collection.update_one({'name':'Anoop'},
{'$unset':{'age':''}})
alldocs =collection.find({},{'_id':0})
for i in alldocs:
  print(i)


# 