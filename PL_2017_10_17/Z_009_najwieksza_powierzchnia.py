# Korzystając w ze ściągniętego pliku z bazą krajów. Znajdź kraj o największej powierzchni i wyświetl jego nazwę i powierzchnię.
from countries import *

def biggest_country():
    max_area = 0
    tmp_area = 0

    for element in countries:
        tmp_area = element['area']

        if tmp_area > max_area:
            max_area = tmp_area
            biggest_country = element['name']['official']

        data = [biggest_country, max_area]

    return data

biggest_country_data = biggest_country()

print("""Największym krajem jest {0} 
o powierzchni {1}
""".format(biggest_country_data[0], biggest_country_data[1]))