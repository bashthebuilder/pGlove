import pymongo
from pymongo import MongoClient
import os.path

#connecting idea
#Here the assumption is that the code connects to a local machine localhost and port 27017. One can cange this based on one's requirements.
client = MongoClient('localhost', 27017)
#I have named the directory which contains my databases as db
db = client['db']
collection = db['wikidata']

counter=0
for item in collection.find():
  counter += 1
    
  try:
    label = item [ 'labels' ] [ 'en' ] [ 'value' ]
    entity_id = item [ 'id' ]
    for properties in item [ 'claims' ]:
      property_id=properties
      for inner_properties in item [ 'claims' ] [ property_id ]:
	label = label.replace(" ", "_")
	print label + " " + entity_id + " " + property_id + " " +  str ( inner_properties [ 'mainsnak' ] [ 'datavalue' ] [ 'value' ] [ 'upperBound' ] )
  except:
    pass
  