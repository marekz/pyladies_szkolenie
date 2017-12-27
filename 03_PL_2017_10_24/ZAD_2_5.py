# 2.5 Znajdź i zapisz wszystkie imiona kobiet do pliku sw_women
# a wszystkich mężczyzn do sw_men

import json

def checkGender():

    for element in data:
        print("Nazwa: {0}: Wiek: {1}".format(element['name'], element['gender']))
        if element['gender'] == 'female':
            file_save = 'sw_women'
        elif element['gender'] == 'male':
            file_save = 'sw_men'

        openFile = open(file_save, 'a')
        openFile.write("Nazwa: {0}\n".format(element['name']))
        openFile.close()

#Import file
file = "py1.2.json"
acces_mode = "r"

dataJson = open(file, acces_mode)
data = json.load(dataJson)

checkGender()