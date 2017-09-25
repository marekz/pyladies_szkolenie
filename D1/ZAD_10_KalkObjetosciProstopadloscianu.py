print("Kalkulator objętości prostopadłościanu");
szer = input("Podaj szerokość: ");
gleb = input("Podaj głębokość: ");
wyso = input("Podaj wysokość : ");

obj = int(gleb) * int(szer) * int(wyso);
typ = "";

if (szer == gleb and gleb == wyso):
    typ = "Sześcian idealny";
elif szer == gleb:
    typ = "Podstawa kwadratowa";

print("""Objętość prostopadłoscioanu: {0}
Typ: {1}""".format(obj, typ));