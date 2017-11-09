# Korzystając z API http://py.net/ zarejestrój się (/register)
# pamiętaj że może być tylko jeden użytkownik pod daną nazwą (name)
# /register
# POST
# requires:
#     "name": string
#     "password": string
# proper response:
#     200: {'success': True}

# url = 'http://mywebsite.org/post'
# a_dict = {"random_key": "with_random_value"}
# resp = requests.post(url, json=a_dict)


import requests

url = 'http://py.net/register/'
data = {'name': 'JakubWedrowycz2', 'password': 'ZabijCzarnaKura'}
resp = requests.post(url,json=data)


print(resp.json())


# resp = requests.post(
#     'http://py.net/registr/',
#     json={
#         'name': 'JakubWedrowycz',
#         'password': 'slkdjldslksfd'
#     }
# )
# print(resp.json())
#
# resp = requests.get('http://py.net/register')
# print(resp.json())

