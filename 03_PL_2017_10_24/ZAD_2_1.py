# 2.1	Wczytaj plik i stwórz słownik w którym kluczem będzie imię (i nazwisko)
# a wartością będzie słownik z kluczami kolor oczu i wzrost Przykład: {"Yoda": {"height": 66, "eyes": "brown"}}

filename = "py1.2.txt"
mode_access = "r"

file = open(filename, mode_access)

data = file.read()
dataArray = data.split('\n')


for element in dataArray:
   slownik = {}
   myElements = element.split('.')
   myElement = myElements[1].strip()
   data = {}
   data["height"] = int(myElement[myElement.find('and is')+7:myElement.find('cm')].strip())
   eyes = {}
   data["eyes"] = myElement[myElement.find('has')+4:myElement.find('and')].strip()
   slownik[myElement[0:myElement.find('has')].strip()] = data

   print(slownik)
