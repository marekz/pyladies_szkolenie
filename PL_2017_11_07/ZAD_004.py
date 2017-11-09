# Korzystając z API http://py.net/
# po pobraniu klucza API (api_key)

import requests

url = 'http://py.net/auth/'
data = {'name': 'JakubWedrowycz2', 'password': 'ZabijCzarnaKura'}

resp = requests.post(url, json=data)

key_set = resp.json()
api_key = key_set['api_key']
name = key_set['name']

# ustaw status swojego użytkownika (/user_status/set)
# /user_status/set
# POST
# requires:
#     "api_key": string
#     "status": string
# proper response:
#     {'success': True}
url = 'http://py.net/user_status/set'
status = 'Bij Bardaka'
data = {"api_key": api_key, "status": status}
resp = requests.post(url, json=data)
print(resp.json())

# i sprawdź status innych (/user_status)
# import requests
# resp = requests.get('http://py.net/somefile')
# with open('file.pdf', 'wb') as file:
#     file.write(resp.content)
url = 'http://py.net/user_status'
resp = requests.get(url)
print(resp.json())
# w szczególności koleżanki/kolegi obok.

url = 'http://py.net/user_status?name=Magdalena'
myStatus = requests.get(url)
dane = myStatus.json()
print(dane['Magdalena'])
