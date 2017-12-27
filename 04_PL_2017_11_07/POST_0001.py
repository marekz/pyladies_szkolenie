import requests


url = 'http://mywebsite.org/post'
a_dict = {"random_key": "with_random_value"}
resp = requests.post(url, json=a_dict)