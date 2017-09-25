from math import pi;

print(len(str(10)));
# print(len(str(10.12)));
# print(len("test"));

imie = input("Podaj imię: ");
imieLen = len(imie);
print("""Imie {0}, zawiera {1} znaków.""".format(imie, imieLen));

print("Liczba PI: " + str(pi));