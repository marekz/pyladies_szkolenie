# 5.3 Napisz funkcję, która policzy BMI "Człowieka" (count_bmi)

class Czlowiek:

    bmi = 0

    def __init__(self, name, height, weight):
        self.imie = name
        self.wysokosc = height
        self.waga = weight

    def speak(self):
        print('Mowie prawdę')

    def count_bmi(self):
        wysokosc = self.wysokosc / 100
        self.bmi = self.waga / (wysokosc ** 2)

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


Jan = Czlowiek('Jan', 150, 10)
Jan.speak()
print("{0} waży {1} przy wzroście {2}".format(Jan.imie, Jan.waga, Jan.wysokosc))
print("BMI ", Jan.imie, " - ",  Jan.count_bmi())

# Kazik = Polityk('Kazik', 150, 50)
# Kazik.recive_bribe()
# Kazik.speak()
# print(Kazik.waga)
# print(Kazik.wysokosc)
# print("{0} waży {1} przy wzroście {2}".format(Kazik.imie, Kazik.waga, Kazik.wysokosc))
