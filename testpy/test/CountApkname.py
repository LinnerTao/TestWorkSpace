from pymongo import MongoClient
import json
outputdir='H:\\appinfor\\'
conn = MongoClient('192.168.2.169', 27017)
db = conn.mongoQueue
my_set = db.TestList1
my_set2=conn.mycol.testdb
file = 'D:'+ '/test.json'
j=0
a=[]
apk_nodes=[]
n=0
for i in my_set.find().distinct('apkname'):
    apk_node = {
        "apkname": i,
        "apkversion": ''
    }
    for j in my_set.find({'apkname':i}):
      a.append(j.get('apkversion'))
      #apk_node["apkversion"]+=''.join([j.get("apkversion")])
    apk_node["apkversion"]=a
    a=[]
    apk_nodes.append(apk_node)


fb = open(file,'w')
fb.write(json.dumps(apk_nodes,indent=2))
fb.close()
my_set2.insert(apk_nodes)
