__author__ = 'msjameel'

import pymongo
from pymongo import MongoClient
import os.path
import json

#need to capture P279 property
#connecting idea
#Here the assumption is that the code connects to a local machine localhost and port 27017. One can cange this based on one's requirements.
client = MongoClient('localhost', 27017)
#I have named the directory which contains my databases as db
db = client['db']
collection = db['wikidata']

#save path
save_path = '/home/msjameel/ijcai_2016/wikidata/documents/'

for item  in collection.find():
    '''item is one record in database'''
    id1 = item['id'] #get the item id

    if ( id1[0] == 'P'):
        try:
            id_label = item['labels']['en']['value']
            for properties in item['claims']['P1647']:
                print id1 + ' ' + id_label + ' ' + 'P' + str(properties['mainsnak']['datavalue']['value']['numeric-id'])
        except:
            pass
