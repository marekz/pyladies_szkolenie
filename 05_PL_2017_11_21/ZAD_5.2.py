# 5.2 Stwórz konstruktor (__init__) dla klasy "Człowiek", który oprócz imienia pobierze też wzrost i wagę.

class Czlowiek:
    def __init__(self, name, height, weight):
        self.imie = name
        self.wysokosc = height
        self.waga = weight

    def speak(self):
        print('Mowie prawdę')

    def count_bmi(self):
        pass

    def diff_to_norm(self):
        pass

    def save_data(self):
        pass

    def to_burn(self):
        pass

    def to_eat(self):
        pass

    def what_to_do(self):
        pass

class Polityk(Czlowiek):

    bribe = False

    def speak(self):
        if self.bribe == True:
            super().speak()
        else:
            print('Kłamie, bo mogę')

    def recive_bribe(self):
        self.bribe = True


Jan = Czlowiek('Jan', 150, 50)
Jan.speak()
print("{0} waży {1} przy wzroście {2}".format(Jan.imie, Jan.waga, Jan.wysokosc))

Kazik = Polityk('Kazik', 150, 50)
Kazik.recive_bribe()
Kazik.speak()
print(Kazik.waga)
print(Kazik.wysokosc)
print("{0} waży {1} przy wzroście {2}".format(Kazik.imie, Kazik.waga, Kazik.wysokosc))
