# 5.4 Napisz funkcję, która policzy, ile kilogramów brakuje do normy (diff_to_norm)
# BMI * (wzrost ** 2) = prawid_waga
class Czlowiek:

    bmi = 0
    oczekiwana_waga = 0
    default_bmi = 22.5 #Przyjmuję średnie poprawne BMI

    def __init__(self, name, height, weight):
        self.imie = name
        self.wysokosc = height/100
        self.waga = weight
        self.count_bmi()
        self.diff_to_norm()

    def speak(self):
        print('Mowie prawdę')

    def count_bmi(self):
        self.bmi = self.waga / (self.wysokosc ** 2)

    def diff_to_norm(self):
        self.oczekiwana_waga = self.default_bmi * (self.wysokosc ** 2)
        print("Cześć {3}. Twoje BMI: {0} Idealna waga przy wzroście {1} m to {2} kg".format(self.bmi, self.wysokosc, self.oczekiwana_waga, self.imie))
        if self.bmi < 18.5:
            roznica = self.oczekiwana_waga - self.waga
            print('Musisz przytyć: ', roznica )
        elif self.bmi > 25.0:
            roznica =  self.waga - self.oczekiwana_waga
            print('Musisz schudnąć: ', roznica )
        else:
            print("Tak trzymaj :)")


    def save_data(self):
        pass

    def to_burn(self):
        pass

    def to_eat(self):
        pass

    def what_to_do(self):
        pass

Jan = Czlowiek('Jan', 168, 80)
print("Jan: ", Jan.oczekiwana_waga)

Kuba = Czlowiek('Kuba', 180, 80)
print("Kuba: ", Kuba.oczekiwana_waga)
