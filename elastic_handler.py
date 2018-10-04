import json
from elasticsearch import Elasticsearch
from file_reader import UserFileReader

class ElasticHandler(object):
	
	def __init__(self):
		self.es =  Elasticsearch([{'host': 'localhost', 'port': 9200}])

class UserElasticHandler(ElasticHandler):

	def __init__(self):
		super(UserElasticHandler, self).__init__()

	def upload(self):
		user_file_reader = UserFileReader('sample_data', 'user_data.txt')
		list_user = user_file_reader.get_users()
		for i in range(len(list_user)):
			self.es.index(index='sw', doc_type='user', id=(i+1), body=list_user[i])

	def get_by_uid(self, uid):
		result = es.get(index='sw', doc_type='people', id=5)
		print(result)

	def get_by_name(self, name):
		result = es.search(index="sw", body={"query": {"match": {'name': name}}})
		print(result)