from ElasticClient import ElasticClient as es
import json
import urllib

user = "abubaker"
ppassword = "BDf%tJ#VS@6JrAw@9Ktc"

ppassword = urllib.parse.quote(ppassword)

client = es(user, ppassword)
query = json.load(open("query.json"))

response = client.send_query(query, scroll=True, size=1000)

hits = response['hits']['hits']  # dictionary of dictionary
print (len(hits))
print (hits)
wdk = "@timestamp\t message\n"

size = len(response['hits']['hits'])
print(size)
while (size > 0):
    print(size)
    size, page = client.scroll()
    if size == 0:
        break
    for hit in hits:
        log_entry = hit['_source']  # why!!
        wdk += log_entry['@timestamp']
        wdk += "\t"
        wdk += log_entry['message']
        wdk += "\n"

    hits = page['hits']['hits']
    size = len(page['hits']['hits'])
    print(size)
    with open('last.txt', 'w') as f:
         f.write(wdk)
