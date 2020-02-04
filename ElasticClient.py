from elasticsearch import Elasticsearch
import json
import certifi
class ElasticClient:
	def __init__(self, user, password, url = 'kibana.emulab.net/elasticsearch'):
		self.query = ''
		es_url = 'https://' + user + ':' + password + '@' + url
		self.es = Elasticsearch([es_url], timeout=60,use_ssl=True, ca_certs=certifi.where())
		self.sid = None

	def send_query(self, query, scroll = False, size = 1000):
		scrollTime = '0'
		if scroll:
			scrollTime = '2m'
			
		results = self.es.search(scroll = scrollTime,
			size = size,
			body=json.loads(json.dumps(query))
		)
		self.sid = results['_scroll_id']
		return json.loads(json.dumps(results))

	def scroll(self):
		page = self.es.scroll(scroll_id = self.sid, scroll = '2m')
		self.sid = page['_scroll_id']
		scroll_size = len(page['hits']['hits'])
		json_page = None
		if scroll_size > 0:
			json_page = json.loads(json.dumps(page))
		return scroll_size, json_page
