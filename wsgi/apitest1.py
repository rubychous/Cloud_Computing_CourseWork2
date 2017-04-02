import os
import pymongo
import json
import pandas as pd

connection_string = os.environ['OPENSHIFT_MONGODB_DB_URL']
myMongo_client = pymongo.MongoClient(connection_string)

print(connection_string)

myMongo_London_DB_client = myMongo_client.apitest2.London_Visitors

filepath = 'internationalvisitorslondonraw.csv'

my_df = pd.read_csv(filepath, dtype=None, skipinitialspace=True)

my_documents = json.loads(my_df.T.to_json()).values()

myMongo_London_DB_client.drop()

myMongo_London_DB_client.insert(my_documents)

test_query_response = myMongo_London_DB_client.find({'year': '2002','purpose':'Business', 'mode':'Air', 'nights':{"$lte": 1}})

for i, doc in enumerate(test_query_response):
	print(i+1)
	for attr, val in doc.iteritems():
		print('{}:{}'.format(attr, val))
	print('\n')

myMongo_client.close()
