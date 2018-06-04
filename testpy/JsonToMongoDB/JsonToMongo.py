from WriteMongoData import *
path = 'D:\ExData\\air.com.tencent.qqfarmios_3.3.4__27\\states'#the path of json
name = 'air.com.tencent.qqfarmios_3.3.4__27'#the name of app
list1 = ReadOnekindFiles(path)#all json files
ReadFiles(name,path,list1)#
#InsertMongo(Nodes)
