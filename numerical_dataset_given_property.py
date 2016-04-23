import pymongo
from pymongo import MongoClient
import os.path

#connecting idea
#Here the assumption is that the code connects to a local machine localhost and port 27017. One can cange this based on one's requirements.
client = MongoClient('localhost', 27017)
#I have named the directory which contains my databases as db
db = client['db']
collection = db['wikidata']

for item in collection.find():
  try:
    label = item [ 'labels' ] [ 'en' ] [ 'value' ]
    entity_id = item [ 'id' ]
    for properties in item [ 'claims' ][ 'P569' ]:
      label = label.replace ( " ", "-" )
      #print label + " " + entity_id + " " + 'P569' + " " +  str ( properties [ 'mainsnak' ] [ 'datavalue' ] [ 'value' ] [ 'upperBound' ] )
      #print label + " " + entity_id + " " + 'P1086' + " " + 'deity_of' + " " + 'Q' + str(properties['mainsnak']['datavalue']['value']['numeric-id'])
      print label + " " + entity_id + " " + 'P569' + " " +  str ( properties [ 'mainsnak' ] [ 'datavalue' ] [ 'value' ] [ 'time' ] )
  except:
    pass
