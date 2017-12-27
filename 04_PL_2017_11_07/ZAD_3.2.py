# Korzystając z API http://py.net/ zarejestrój się (/register) pamiętaj że może być tylko jeden użytkownik pod daną nazwą (name)

import requests

url = "http://py.net/register/"
data = {"name": "JakubWedrowycz2", "password": "ZabijCzarnaKura"}
resp = requests.post(url, json=data)
print(resp.json())