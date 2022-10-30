'''


1)  Find the student name who scored maximum scores in all (exam, quiz and homework)?

db.Student.aggregate([ {"$project":{"name":1,"Maxscore":{"$max":"$scores.exam"} }} ])
db.Student.aggregate([ {"$project":{"name":1,"Maxscore":{"$max":"$scores.quiz"} }} ])
db.Student.aggregate([ {"$project":{"name":1,"Maxscore":{"$max":"$scores.homework"} }} ])

2) Find students who scored below average in the exam      and pass mark is 40%?
db.Student.find({scores : { $elemMatch:{"score":{$avg : "$score" , $score:40}}}})

3) Find students who scored below pass mark and assigned them as fail, and 
above pass mark as pass in all the categories.
db.Student.find({scores:{$elemMatch:{"score":{$lt : 40,$set : "fail"}}}})
db.Student.find({scores:{$elemMatch:{"score":{$gt : 40,$set : "pass"}}}})

4)Find the total and average of the exam, quiz and homework and 
store them in a separate collection.
db.Student.aggregate([{ $group:{total:{$sum:["$scores.exam","$scores.quiz","$scores.homework"]} }, count: { $sum: 1 }
scores:{$elemMatch:{"score":{average:{$avg:["$score.exam","$score.quiz","$score.homework"]}} ])
db.scores.aggregate( [{$addFields: {totalhomework: { $sum: "$homework" } , 
totalQuiz: { $sum: "$quiz" } ,totalexam:{$sum:"$exam"}}  },  { $addFields: { totalScore:
  { $add: [ "$totalhomework", "$totalQuiz", "$totalexam" ] } } }
] )

5)  Create a new collection which consists of students who scored below average 
and above 40% in all the categories.
db.scores.aggregate( [{$addFields: {average: { $avg: "$homework" } , 
avergae1: { $avg: "$quiz" } ,average2:{$avg:"$exam"}}  },  { $addFields: { averagescores:
  { $add: [ "$average", "$average1", "$average2" ] } } }
] )
6) Create a new collection which consists of students who scored
 below the fail mark in all the categories.
db.scores.aggregate( [{$addFields: {sco: { $lt: 40: "$homework" } , 
sco1: { $lt:40: "$quiz" } ,sco2:{$lt:40:"$exam"}}  },  { $addFields: { scrorers:
 { $add: [ "$sco", "$sco1", "$sco2" ] } } }
] )
7) Create a new collection which consists of students who scored 
above pass mark in all the categories.
db.scores.aggregate( [{$addFields: {sch: { $gt: 40: "$homework" } , 
sch1: { $lt:40: "$quiz" } ,sch2:{$lt:40:"$exam"}}  },  { $addFields: { stu:
 { $add: [ "$sch", "$sch1", "$sch2" ] } } }] )
                                                                      
'''

#1)Find the student name who scored maximum scores in all(exam, quiz and homework)?

import pymongo
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = myclient['guvi']#database created
databases = myclient.list_database_names()
if 'guvi' in databases:
    print("your database exist")
else:
    print("Database do not exist")
mycollection = mydb['Student']
collections = mydb.list_collection_names()
if 'Student' in collections:
    print("your collection exist")
else:
    print("collection do not exist")
data =  mycollection.aggregate([ {"$project":{"name":1,"Maxscore":{"$max":"$scores.exam"} }} ]);
data =  mycollection.aggregate([ {"$project":{"name":1,"Maxscore":{"$max":"$scores.quiz"} }} ]);
data =  mycollection.aggregate([ {"$project":{"name":1,"Maxscore":{"$max":"$scores.homework"} }} ]);

for document in data:
       print(document)
       
#2)Find students who scored below average in the exam and pass mark is 40%?
'''
import pymongo
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = myclient['guvi']#database created
databases = myclient.list_database_names()
if 'guvi' in databases:
    print("your database exist")
else:
    print("Database do not exist")
mycollection = mydb['Student']
collections = mydb.list_collection_names()
if 'Student' in collections:
    print("your collection exist")
else:
    print("collection do not exist")
data =  mycollection.find({"$scores": { "$elemMatch":{"score":{"$avg" : "$score" , "$score":40}}}});
for document in data:
       print(document)'''
       
#3)Find students who scored below pass mark and assigned them as fail, and above pass mark as pass in all the categories.

'''import pymongo
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = myclient['guvi']#database created
databases = myclient.list_database_names()
if 'guvi' in databases:
    print("your database exist")
else:
    print("Database do not exist")
mycollection = mydb['Student']
collections = mydb.list_collection_names()
if 'Student' in collections:
    print("your collection exist")
else:
    print("collection do not exist")
data =  mycollection.find({scores:{"$elemMatch":{"score":{"$lt" : 40,$set : "fail"}}}});
data1 =  mycollection.find({scores:{"$elemMatch":{"score":{"$gt"" : 40,$set : "pass"}}}});
for document in data:
       print(document)
for document in data1:
       print(document)'''
       
#4)Find the total and average of the exam, quiz and homework and store them in a separate collection.

'''
import pymongo
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = myclient['guvi']#database created
databases = myclient.list_database_names()
if 'guvi' in databases:
    print("your database exist")
else:
    print("Database do not exist")
mycollection = mydb['Student']
collections = mydb.list_collection_names()
if 'Student' in collections:
    print("your collection exist")
else:
    print("collection do not exist")
data =  mycollection.aggregate([{ $group:{total:{$sum:["$scores.exam","$scores.quiz","$scores.homework"]} }, count: { $sum: 1 }
scores:{$elemMatch:{"score":{average:{$avg:["$score.exam","$score.quiz","$score.homework"]}} ])
db.scores.aggregate( [{$addFields: {totalhomework: { $sum: "$homework" } , 
totalQuiz: { $sum: "$quiz" } ,totalexam:{$sum:"$exam"}}  },  { $addFields: { totalScore:
  { $add: [ "$totalhomework", "$totalQuiz", "$totalexam" ] } } };
] )
for document in data:
       print(document)'''


#5)Create a new collection which consists of students who scored below average and above 40% in all the categories.
'''
import pymongo
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = myclient['guvi']#database created
databases = myclient.list_database_names()
if 'guvi' in databases:
    print("your database exist")
else:
    print("Database do not exist")
mycollection = mydb['scores']
collections = mydb.list_collection_names()
if 'scores' in collections:
    print("your collection exist")
else:
    print("collection do not exist")
data =  mycollection.aggregate( [{$addFields: {average: { $avg: "$homework" } , avergae1: { $avg: "$quiz" } ,average2:{$avg:"$exam"}}  },  { $addFields: { averagescores: { $add: [ "$average", "$average1", "$average2" ] } } } );

for document in data:
       print(document)'''


#6)Create a new collection which consists of students who scored below the fail mark in all the categories.

'''
import pymongo
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = myclient['guvi']#database created
databases = myclient.list_database_names()
if 'guvi' in databases:
    print("your database exist")
else:
    print("Database do not exist")
mycollection = mydb['scores']
collections = mydb.list_collection_names()
if 'scores' in collections:
    print("your collection exist")
else:
    print("collection do not exist")
data =  mycollection.aggregate( [{$addFields: {sco: { $lt: 40: "$homework" } , sco1: { $lt:40: "$quiz" } ,sco2:{$lt:40:"$exam"}}  },  { $addFields: { scrorers: { $add: [ "$sco", "$sco1", "$sco2" ] } } }] );
for document in data:
       print(document)
'''


#7)Create a new collection which consists of students who scored above pass mark in all the categories.

'''
import pymongo
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = myclient['guvi']#database created
databases = myclient.list_database_names()
if 'guvi' in databases:
    print("your database exist")
else:
    print("Database do not exist")
mycollection = mydb['scores']
collections = mydb.list_collection_names()
if 'scores' in collections:
    print("your collection exist")
else:
    print("collection do not exist")
data =  mycollection.aggregate( [{$addFields: {sch: { $gt: 40: "$homework" } , sch1: { $lt:40: "$quiz" } ,sch2:{$lt:40:"$exam"}}  },  { $addFields: { stu: { $add: [ "$sch", "$sch1", "$sch2" ] } } }] );
for document in data:
       print(document)'''