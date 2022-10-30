'''
Create a collection.
db.createCollection("telephone")

For CRUD operation, create a directory which has 
fields like Name, Phone number, Place etc.,
db.telephone.insert({"name":"gnana","ph":"12345","place":"tn"})
db.telephone.insert({"name":"lakshmi","ph":"645449","place":"kl"})
db.telephone.insert({"name":"lara","ph":"65765","place":"AP"})

RETRIEVE
db.telephone.find()
db.telephone.find().pretty()
db.telephone.find({place:"kl"})

UPDATE
db.telephone.update({"name":"gnana","name":"malasanthi"})

DELETE
db.telephone.remove({"name":"lakshmi"},{"justOne":true})

Make a query to find records you just created.
db.telephone.find().pretty()

update_one()
db.telephone.updateOne({name: "malasanthi"}, {$set:{place:"tn"}})

delete_one()
db.telephone.deleteOne({"place":AP})

'''
#CREATION

import pymongo
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = myclient['guvi']#database created
databases = myclient.list_database_names()
if 'guvi' in databases:
    print("your database exist")
else:
    print("Database do not exist")
mycollection = mydb['telephones']
collections = mydb.list_collection_names()
if 'telephones' in databases:
    print("your collection exist")
else:
    print("collection do not exist")

my_info = {
         'name':"gnana",
         'ph':12345,
         'place':"TN"        
         }
'''my_info = {
         'name':"lakshmi",
         'ph':241354,
         'place':"KL"        
         }'''
'''my_info = {
         'name':"lara",
         'ph':34979,
         'place':"AP"        
         }'''
mycollection.insert_one(my_info)

id_doc = mycollection.insert_one(my_info)
print(id_doc.insert_id)


#RETRIEVE

import pymongo
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = myclient['guvi']#database created
databases = myclient.list_database_names()
if 'guvi' in databases:
    print("your database exist")
else:
    print("Database do not exist")
mycollection = mydb['telephones']
collections = mydb.list_collection_names()
if 'telephones' in collections:
    print("your collection exist")
else:
    print("collection do not exist")
telephones = [
       {"name":input("enter your name")},
       {"name":"lakshmi"}
      ]
mycollection.find_one(telephones)
data = mycollection.find_one()
print(data)

#UPDATE

import pymongo
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = myclient['guvi']#database created
databases = myclient.list_database_names()
if 'guvi' in databases:
    print("your database exist")
else:
    print("Database do not exist")
mycollection = mydb['telephones']
collections = mydb.list_collection_names()
if 'telephones' in collections:
    print("your collection exist")
else:
    print("collection do not exist")
dat ={'name':'gnana'}
new_data = {'$set': {"name":'malasanthi','ph':'241354','place':'KL'}}
mycollection.update_one(dat,new_data)

data = mycollection.find()
for document in data:
       print(document)


#DELETE

import pymongo
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = myclient['guvi']#database created
databases = myclient.list_database_names()
if 'guvi' in databases:
    print("your database exist")
else:
    print("Database do not exist")
mycollection = mydb['telephones']
collections = mydb.list_collection_names()
if 'telephones' in collections:
    print("your collection exist")
else:
    print("collection do not exist")
dat = {'name':'gnana'}
mycollection.delete_one(dat)

data = mycollection.find()
for document in data:
     print(document)



# Make a query to find records you just created.

import pymongo
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = myclient['guvi']#database created
databases = myclient.list_database_names()
if 'guvi' in databases:
    print("your database exist")
else:
    print("Database do not exist")
mycollection = mydb['telephones']
collections = mydb.list_collection_names()
if 'telephones' in collections:
    print("your collection exist")
else:
    print("collection do not exist")

mycollection.find().pretty()

data = mycollection.find()
for document in data:
     print(document)
     

# UPDATE_ONE

import pymongo
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = myclient['guvi']#database created
databases = myclient.list_database_names()
if 'guvi' in databases:
    print("your database exist")
else:
    print("Database do not exist")
mycollection = mydb['telephones']
collections = mydb.list_collection_names()
if 'telephones' in collections:
    print("your collection exist")
else:
    print("collection do not exist")
dat = ({'name': "malasanthi"},{"$set":{'place':"tn"}})
mycollection.update_one(dat)

data = mycollection.find()
for document in data:
     print(document)
     
#DELETE_ONE

import pymongo
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = myclient['guvi']#database created
databases = myclient.list_database_names()
if 'guvi' in databases:
    print("your database exist")
else:
    print("Database do not exist")
mycollection = mydb['telephones']
collections = mydb.list_collection_names()
if 'telephones' in collections:
    print("your collection exist")
else:
    print("collection do not exist")
dat = {"place":'AP'}
mycollection.delete_one(dat)

data = mycollection.find()
for document in data:
     print(document)