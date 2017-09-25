lista_zona = [
    input("Produkt 1: "),
    input("Produkt 2: "),
    input("Produkt 3: "),
    input("Produkt 4: "),
    input("Produkt 5: ")
];

print(lista_zona);

lista_maz = [
    input("Produkt 1: "),
    input("Produkt 2: "),
    input("Produkt 3: "),
    input("Produkt 4: "),
    input("Produkt 5: ")
];

maz_lista_ok = [];
maz_lista_nadmiarowa = [];

for element_maz in lista_maz:

    if element_maz in lista_zona:
        maz_lista_ok.append(element_maz);
    else:
        maz_lista_nadmiarowa.append(element_maz);


print("Poprawna lista zakupow: {0}".format(maz_lista_ok));
print("Nadmiarowa lista zakupów: {0}".format(maz_lista_nadmiarowa));