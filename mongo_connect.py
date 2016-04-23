#Some libraries
import pymongo
from pymongo import MongoClient
import os.path

#connecting idea
client = MongoClient('localhost', 27017)
db = client['db']
collection = db['wikidata']

#save path
save_path = '/home/msjameel/ijcai_2016/wikidata/documents/'
save_path_aliases = '/home/msjameel/ijcai_2016/wikidata/documents/aliases/'
save_path_claims = '/home/msjameel/ijcai_2016/wikidata/documents/claims/'

counter=0
for item  in collection.find():
    '''item is one record in database'''
    counter +=1
    if counter%1000 == 0:
        print counter/1000

    id1 = item['_id'] #name of the file to be saved
    #completeName = os.path.join(save_path, str(id1)+'.txt')
    completeName1 = os.path.join(save_path, 'labels'+'.txt')
    try:
        id2 = item['labels']['en']['value']
    except:
          pass
    
    '''write set 1'''
    f1 = open(completeName1,'a')
    f1.write(id2.encode("utf-8")+'\n') #write tags list, one line
    #f1.write('\n')
    f1.close()

    completeName2 = os.path.join(save_path, 'descriptions'+'.txt')
    try:
        id3 = item['descriptions']['en']['value']
    except:
          pass

    '''write set 1'''
    f2 = open(completeName2,'a')
    f2.write(id3.encode("utf-8")+'\n') #write tags list, one line
    #f1.write('\n')
    f2.close()

    completeName4 = os.path.join(save_path, 'sitelinks'+'.txt')
    try:
       id3 = item['sitelinks']['enwiki']['title']
    except:
          pass

    '''write set 1'''
    f4 = open(completeName4,'a')
    f4.write(id3.encode("utf-8")+'\n') #write tags list, one line
    #f1.write('\n')
    f4.close()

    completeName3 = os.path.join(save_path_aliases, str(counter)+'.txt')
    '''write set 1'''
    f3 = open(completeName3,'a')
    
    try:
        for aliase in item['aliases']['en']:
	  f3.write(aliase['value'].encode("utf-8")+ '\n') #write tags list, one line
    except:
          pass
    f3.write('\n')
    f3.close()
       