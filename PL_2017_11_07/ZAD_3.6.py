# Korzystając z API http://py.net/ spróbój użyc querry stringów (query_string)

# /query_string
# GET
# proper response:
#     200: {
#     "parsed": bool,
#     "args": dict,
#     "url": dict,
#     "query_string": dict
# }

import requests

url = 'http://py.net/query_string?name=ala'
resp = requests.get(url)
from pprint import pprint as pp

pp(resp.json())
print(resp.json())

