# 5.6 Zakładając, że aby schudnąć 1 kg trzeba spalić 6000kcal,
# napisz funkcjonalność, która powie użytkownikowi,
# ile powinien godzin
# biegać(500kcal/h) /
# jeździć rowerem(600kcal/h) /
# uprawiać hobby(250kcal/h) /
# grać w szachy(150kcal/h) /
# etc. aby być w normie (to_burn).
import json

class Czlowiek:

    bmi = 0
    oczekiwana_waga = 0
    default_bmi = 22.5 #Przyjmuję średnie poprawne BMI
    burn_activity = {'running':500,'riding_bike':600,'easy_hobby':250,'play_cheese':150}

    def __init__(self, name, height, weight):
        self.imie = name
        self.wysokosc = height/100
        self.waga = weight
        self.count_bmi()
        self.diff_to_norm()
        self.to_burn()

    def speak(self):
        print('Mowie prawdę')

    def count_bmi(self):
        self.bmi = self.waga / (self.wysokosc ** 2)

    def diff_to_norm(self):
        self.oczekiwana_waga = self.default_bmi * (self.wysokosc ** 2)
        print("Cześć {3}. Ważysz: {4}. Twoje BMI: {0} Idealna waga przy wzroście {1} m to {2} kg".format(self.bmi, self.wysokosc, self.oczekiwana_waga, self.imie, self.waga))
        if self.bmi < 18.5:
            roznica = self.oczekiwana_waga - self.waga
            print('Musisz przytyć: ', roznica )
        elif self.bmi > 25.0:
            roznica =  self.waga - self.oczekiwana_waga
            print('Musisz schudnąć: ', roznica )
        else:
            print("Tak trzymaj :)")


    def save_data(self):

        with open ('{}.json'.format(self.imie), 'w') as file:
            json.dump(
            {
                'imie': self.imie,
                'dane': {
                    'waga': self.waga,
                    'wzrost': self.wysokosc,
                    'bmi': self.bmi
                }
            },
            file
        )

    def to_burn(self):
        print("Aby schudnąć musisz: ")
        for element in self.burn_activity:
            print("{0}: {1}".format(element, self.burn_activity[element]))

    def to_eat(self):
        pass

    def what_to_do(self):
        pass

Jan = Czlowiek('Jan', 140, 30)
# Jan.count_bmi()
# Jan.diff_to_norm()
# Jan.save_data()
Kuba = Czlowiek('Kuba', 140, 200)
# Kuba.count_bmi()
# Kuba.diff_to_norm()
# Kuba.save_data()
