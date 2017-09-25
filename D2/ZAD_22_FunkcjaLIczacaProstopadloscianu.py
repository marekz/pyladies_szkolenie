def zapytaj():
    szerokosc = int(input("Podaj szerokość prostopadłościoanu: "))
    glebokosc = int(input("Podaj głębokość prostopadłościoanu: "))
    wysokosc = int(input("Podaj wysokość prostopadłościoanu: "))

    objetosc = ObjetoscProstopadloscianu(szerokosc, wysokosc, glebokosc)
    print("Objętość prostopadłoscianu: {0}".format(objetosc))

def ObjetoscProstopadloscianu(a, b, c):
    return a * b * c

zapytaj()