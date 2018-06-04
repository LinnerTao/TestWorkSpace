from pymongo import MongoClient
import json
outputdir='H:\\appinfor\\'
conn = MongoClient('192.168.2.169', 27017)
db = conn.mongoQueue
my_set = db.TestList1
k=0
for i in my_set.find().sort([('apkname', 1)]):
        if k==5:
            break
        k=k+1
        print(i.get('apkname')+'_'+i.get('apkversion')+'--'+str(i.get('num')))
