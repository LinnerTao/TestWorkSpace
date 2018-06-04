from pymongo import MongoClient
import json
add = '192.168.2.169'
cnn = MongoClient(add,27017)
my_set = cnn.MultiApp.test1
for i in my_set.find({'_id':{'$regex':'air.com.tencent'}}):
    for j in i.get('states'):
        print (j)
    print ('\n')

