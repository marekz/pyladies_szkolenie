# trzy elementowa lista składająca się z imiona i wiek
from builtins import print

element_1 = ['Marek', 17];
element_2 = ['Madzia', 16];
element_3 = ['Kufel', 9];

lista_list = [];

lista_list.append(element_1);
lista_list.append(element_2);
lista_list.append(element_3);

print("Lista imion: ");
for a in lista_list:
    print("Imię: {0}".format(a[0]));

print("----------------------");

print("Wiek: ");
for a in lista_list:
    print("Lat: {0}".format(a[1]));

print("----------------------");

print("Lista osób z wiekiem: ");
for a in lista_list:
    print("Osoba: {0}, wiek: {1}".format(a[0], str(a[1])));

print("----------------------");

lista_list.pop(0);
lista_list.pop(-1);

element_4 = ["Jurek", 12];
lista_list.append(element_4);

print("Lista osób z wiekiem: ");
for a in lista_list:
    print("Osoba: {0}, wiek: {1}".format(a[0], str(a[1])));

# element_1.pop(1);