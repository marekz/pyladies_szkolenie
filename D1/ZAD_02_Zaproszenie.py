# Wygenerować zaproszenie na podstawie parametrów:
# imie
# nazwisko
# tytul
# przymiotnik
# ulubiony smak


tytul = "Pan";
imie = "Jacek";
nazwisko = "Placek";
przymiotnik = "Szanowny";
smak = "czekoladowy";

trescZaproszenia = """{0} {1} {2} 
   {3} przyjacielu chciałbym Cię zaprosić na swoje urodziny
   na których będę serwował Twój ulubiony {4} tort. 
   Piotr""".format(tytul, imie, nazwisko, przymiotnik,smak);
print(trescZaproszenia);

# print(math.pi());