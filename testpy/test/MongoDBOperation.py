from pymongo import MongoClient
outputdir='H:\\appinfor\\'
conn = MongoClient('192.168.2.169', 27017)
db = conn.mongoQueue
my_set = db.TestList1
j=1
for i in my_set.find().sort([('apkname',1)]):
    #if i['pop']==False:

        appid=appname=appversion=''
        appid=i.get('_id')
        appname=i.get('apkname')
        appversion=i.get('apkversion')
        print(appid+'_'+appname+'_'+appversion)
        # db.DroidUicrawllist.update({"_id":appname},{'$set':{'pop':True}})
        my_set.update({"_id": appid}, {'$set': {"pop": False}})
        my_set.update({"_id":appid},{'$set': {"num": j}})
        j+=1

