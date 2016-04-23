import pymongo
from pymongo import MongoClient
import os.path

#connecting idea
#Here the assumption is that the code connects to a local machine localhost and port 27017. One can cange this based on one's requirements.
client = MongoClient('localhost', 27017)
#I have named the directory which contains my databases as db
db = client['db']
collection = db['wikidata']

#save path
save_path_aliases = '/home/msjameel/ijcai_2016/wikidata/documents/'

#this counter variable wil be used to see the progress of the program
counter=0
for item  in collection.find():
    '''item is one record in database'''
    counter +=1
    if counter%1000 == 0:
        print counter/1000

    id1 = item['_id'] #name of the file to be saved, but ignored it in this code.

    completeName = os.path.join(save_path_aliases,'aliases'+'.txt')
    '''write set 1'''
    f3 = open(completeName,'a')

    try:
        for aliase in item['aliases']['en']:
            f3.write(aliase['value'].encode("utf-8","strict")+'\n') #write tags list, one line
    except:
           pass
    f3.close()
