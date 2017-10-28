# 2.4* Przetłumacz nazwy kolorów do zdania w zadaniu 2.3

#Wczytanie pliku
filename = "py1.2.txt"
mode_access = "r"
file = open(filename, mode_access)
data = file.read()
dataArray = data.split('\n')
colorArray = []
colorHeightArray = []
slo = {}
sizeArray = []

#iteracja po pliku
def create_color_array():
    for element in dataArray:
        color = element[element.find('has')+4:element.find('and')].strip()
        if color in colorArray:
            color
        else:
            colorArray.append(color)

def create_slo():
    for element in colorArray:
        slo[element] = []

def create_data_slo():
    for element in dataArray:
        height = element[element.find('and is ') + 7:element.find('cm')].strip()
        color = element[element.find('has') + 4:element.find('and')].strip()
        slo[color].append(height)

def calculate_and_save_to_file_avarege():
    newFile = "Avarage_height.txt"
    mode = "a"

    openTOWrite = open(newFile, mode)


    for element in slo:
        lElementow = len(slo[element])
        suma = 0
        for num in slo[element]:
            suma = suma + int(num)
        srednia = suma / lElementow

        kolor = slo_translate[element]
        # print(kolor)
        openTOWrite.write("Średni wzrost osób z kolorem oczu {0} wynosi {1} cm\n".format(kolor, srednia))
        print("Średni wzrost osób z kolorem oczu {0} wynosi {1} cm".format(kolor, srednia))

create_color_array()

slo_translate = {
    'yellow': 'żółty',
    'black': 'czarny',
    'blue': 'niebieski',
    'orange': 'pomarańczowy',
    'green, yellow': 'zielony i żółty',
    'red': 'czerwony',
    'brown': 'brązowy',
    'unknown': 'nieznany',
    'gold': 'złoty',
    'blue-gray': 'niebiesko-szary',
    'pink': 'różowy',
    'hazel': 'piwny',
    '': 'Brak',
    'red, blue': 'Czerwone i niebieskie'
}

print(colorArray)
#deklaracja słownika
create_slo()
#   tworzenie wielowymiarowej tablicy z element['kolor oczu']['wzrosty osob']
create_data_slo()
#Operacja obliczenia średniej dla każdego koloru oczu
calculate_and_save_to_file_avarege()



