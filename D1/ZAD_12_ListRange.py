lista = list(range(0, 100));

print(lista[35:44]);
print(lista[64:]);
print(lista[:34]);
print(lista[::-1]);
print(lista[:34:4]);
print(lista[-65:-28]);

for a in lista:
    print("{0} element listy".format(a));

lista.append(1000);
lista.pop(78);
lista.pop(0);
lista.pop(-10);

for a in lista:
    print("{0} element listy".format(a));