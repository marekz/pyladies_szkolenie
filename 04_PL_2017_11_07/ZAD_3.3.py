# Korzystając z API http://py.net/
# pobierz klucz API (api_key) - zaloguj się (/auth).
# /auth
# POST
# requires:
#     "name": string
#     "password": string
# proper response:
#     {'api_key': string, 'name': string}


import requests

url = 'http://py.net/auth/'
data = {'name': 'JakubWedrowycz2', 'password': 'ZabijCzarnaKura'}
resp = requests.post(url, json=data)
print(resp.json())