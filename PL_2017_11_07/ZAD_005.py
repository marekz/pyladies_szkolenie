# Korzystając z API http://py.net/
# ściągnij i zapisz na dysku losowe zdjęcia kotów (/cat)

import requests
# /cat
# GET
# proper response:
#     200: data
# import requests
# resp = requests.get('http://py.net/somefile')
# with open('file.pdf', 'wb') as file:
#     file.write(resp.content)

url = 'http://py.net/cat'

resp = requests.get(url)
with open('kot.jpeg', 'wb') as file:
    file.write(resp.content)