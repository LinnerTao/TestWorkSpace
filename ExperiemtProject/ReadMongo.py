from pymongo import MongoClient
import json
HostName = '192.168.2.169'

def mongoconn():
    db = MongoClient(HostName,27017)
    my_set = db.MultiApp.test
    return my_set

def ReadData(my_set):
    j = 0
    #n = 0
    ViewName = None
    for i in my_set.find():
       ViewName = i.get("_id")
       k=i.get('states').get('views')
       if(k!=[]):
        for n in range(len(k)):
            text = k[n].get('text')
            KeyNode = {
                '_id': ViewName,
                'viewsnum':n,
                'text':text
            }
            (KeyNode)
            #n+=1
        #break




myset = mongoconn()
ReadData(myset)