#This Python code is used to get data from the Wikidata JSON file. When the collection is indexed in MongoDB, this code can then be used to connect to MongoDB in order to extract the relevant data in a human readable form. As the Wikidata collection is large, this code might take some time to complete. In general, it is efficient.

#Some libraries
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
save_path = '/home/msjameel/ijcai_2016/wikidata/documents/'
save_path_aliases = '/home/msjameel/ijcai_2016/wikidata/documents/aliases/'
save_path_claims = '/home/msjameel/ijcai_2016/wikidata/documents/claims/'

#this counter variable wil be used to see the progress of the program
counter=0
for item  in collection.find():
    '''item is one record in database'''
    counter +=1
    if counter%1000 == 0:
        print counter/1000

    id1 = item['_id'] #name of the file to be saved, but ignored it in this code.

    #let's get the id of the entity here.
    completeName4 = os.path.join(save_path, 'IDs'+'.txt')
    try:
        id4 = item['id']
    except:
        pass

    #write the output to a file, there will be only one file generated. each line in the file contains the ID.
    f4= open(completeName4,'a')
    f4.write(id4.encode("utf-8","strict")+'\n')
    f4.close()

    #completeName = os.path.join(save_path, str(id1)+'.txt')
    completeName1 = os.path.join(save_path, 'labels'+'.txt')
    try:
        id2 = item['labels']['en']['value']
    except:
          pass
    
    '''write set 1'''
    f1 = open(completeName1,'a')
    f1.write(id2.encode("utf-8","strict")+'\n') #write tags list, one line
    #f1.write('\n')
    f1.close()

    completeName2 = os.path.join(save_path, 'descriptions'+'.txt')
    try:
        id3 = item['descriptions']['en']['value']
    except:
          pass

    '''write set 1'''
    f2 = open(completeName2,'a')
    f2.write(id3.encode("utf-8","strict")+'\n') #write tags list, one line
    #f1.write('\n')
    f2.close()

    completeName4 = os.path.join(save_path, 'sitelinks'+'.txt')
    try:
       id3 = item['sitelinks']['enwiki']['title']
    except:
          pass

    '''write set 1'''
    f4 = open(completeName4,'a')
    f4.write(id3.encode("utf-8","strict")+'\n') #write tags list, one line
    #f1.write('\n')
    f4.close()

#    completeName3 = os.path.join(save_path_aliases, str(counter)+'.txt')
    '''write set 1'''
#    f3 = open(completeName3,'a')
    
 #   try:
 #       for aliase in item['aliases']['en']:
#	  f3.write(aliase['value'].encode("utf-8")+ '\n') #write tags list, one line
 #   except:
 #         pass
 #   f3.write('\n')
 #   f3.close()
       
