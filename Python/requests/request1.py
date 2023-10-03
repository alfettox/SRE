import requests as rq
import json

headers = {'Authorization': 'Bearer myAuthCode'}
res = rq.get("https://giovannidefranceschi.wordpress.com/", headers = headers)
print(res.content)

data = {'key1': '001', 'key2':'002', 'key3':'003'}



json_data = json.dumps(data)

res = rq.post('https://httpbin.org/post', data=json_data)

print(res.text)

import requests

url = 'https://httpbin.org/get'
headers = {'My-Custom-Header': 'Hello, World!'}

response = requests.get(url, headers=headers)

print(response.text)