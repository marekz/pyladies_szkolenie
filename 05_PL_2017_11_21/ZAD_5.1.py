# 5.1 Wyobraźmy sobie klasę "Człowiek" z metodą "mowa" i podklasę "Człowieka" - "Polityk"
# z metodami "przyjmij łapówkę" i "kłam".
# Domyślnie "Człowiek" po wykonaniu metody "mów" (speak) wypisze "Mowie prawdę",
# natomiast każda instancja "Polityka" powie "Kłamie, bo mogę",
# chyba że wcześniej została wykonana metoda "przyjmij łapówkę" (recive_bribe), wtedy powie prawdę.

class Czlowiek:
    def __init__(self):
        pass

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


czlowiek1 = Czlowiek()
czlowiek1.speak()

polityk = Polityk()
polityk.speak()