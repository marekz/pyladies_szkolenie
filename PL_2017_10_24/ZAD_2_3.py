# 2.3*Zapisz średni wzrost postaci dla każdego z kolorów w osobnych linijkach w formie:
# Średni wzrost osób z kolorem oczu blue wynosi 123,12 cm.

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

def calculate_avarege():
    for element in slo:
        lElementow = len(slo[element])
        suma = 0
        for num in slo[element]:
            suma = suma + int(num)
        srednia = suma / lElementow
        print("Średni wzrost osób z kolorem oczu {0} wynosi {1} cm".format(element, srednia))


create_color_array()
#deklaracja słownika
create_slo()
#   tworzenie wielowymiarowej tablicy z element['kolor oczu']['wzrosty osob']
create_data_slo()
#Operacja obliczenia średniej dla każdego koloru oczu
calculate_avarege()



