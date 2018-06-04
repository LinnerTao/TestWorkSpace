from pymongo import MongoClient
from bson.objectid import ObjectId
import json
def InsertMongo(Nodes):
    client = MongoClient('192.168.2.169', 27017)
    db = client.MultiApp
    collection = db.test
    collection.insert(Nodes)

def ReadFiles(name,path,list1):
    client = MongoClient('192.168.2.169', 27017)
    db = client.MultiApp
    collection = db.test
    for i in list1:
        with open(path+'\\'+i,'r') as f:
            temp = json.loads(f.read())
            KeyNode = {
                '_id' : name+'_'+i,
                'states':temp
            }
            InsertMongo(KeyNode)

            #print (type(temp))
            #InsertMongo(temp)


import os

def ReadOnekindFiles(string):
    path = string #'D:\ExData\\air.com.tencent.qqfarmios_3.3.4__27\\states'
    list=[]
    filelist = os.listdir(path)
    for i in filelist:
        if os.path.splitext(i)[1]=='.json':
            list.append(i)
    return list


