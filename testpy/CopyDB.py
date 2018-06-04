from pymongo import MongoClient
import json
outputdir='H:\\appinfor\\'
conn = MongoClient('192.168.2.169', 27017)
db = conn.MultiApp
my_set = db.AppList
my_set2= db.test1
conn2 = MongoClient('localhost',27017)
my_set3 = conn2.MultiApp.AppList
UI_set = conn2.MultiApp.AppUI

for i in my_set2.find():
    UI_set.insert(i)