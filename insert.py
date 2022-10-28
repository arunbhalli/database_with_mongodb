import pymongo

# insertion of pymongo
print('Information of friends')
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client.list_database_names())

db = client['friendsdb']
collection = db['friends']
# insert many
info =[{'name':'Shyam','age':25,'address':'Agra India'},
       {'name':'Rahul','age':29,'address':'Agra India'},
       {'name':'Amit','age':26,'address':'Agra India'},
       {'name':'Mausam','age':24,'address':'Agra India'},
       {'name':'Ashish','age':27,'address':'Agra India'},
       {'name':'Tanishk','age':22,'address':'Agra India'},
       {'name':'Ghanshyam','age':20,'address':'Agra India'},
       {'name':'Sundar Singh','age':23,'address':'Agra India'}]
collection.insert_many(info)
for i in collection.find():
  print(i)