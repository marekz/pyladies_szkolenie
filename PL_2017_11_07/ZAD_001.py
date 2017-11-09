import requests
resp = requests.get('http://py.net/status')
print(resp.json())

resp = requests.post(
    'http://py.net/status/set',
    json={
        'status': 'Ala ma kota'
    }
)
print(resp.json())

resp = requests.get('http://py.net/status')
print(resp.json())