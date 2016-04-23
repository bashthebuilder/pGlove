#Some libraries
import pymongo
from pymongo import MongoClient
import os.path
import json

save_path_claims = '/home/msjameel/ijcai_2016/wikidata/documents/claims/'

#connecting idea
client = MongoClient('localhost', 27017)
db = client['db']
collection = db['wikidata']

counter = 0
for item in collection.find():
    '''item is one record in database'''
    counter += 1
    if counter % 1000 == 0:
        print counter / 1000
    completeName4 = os.path.join(save_path_claims, str(counter) + '.txt')
    f5 = open(completeName4, 'a')
    try:
        for properties in item['claims']:
            for ppt in item['claims'][properties]:
                f5.write(properties.encode("utf-8")+' ')
                json.dump(ppt['mainsnak'],f5)
    except:
        pass
    f5.write('\n')
    f5.close()