# Zaimplementuj metodę pozwalającą zwiększyć czas o minutę, sekundę, godzinę,
# a w przypadku Dokładnego Zegara dodatkowo milisekundy.
# Pamiętaj że przekraczając 60minutę lub sekundę powinna też odpowiednio zwiększyć odpowiednio godzinę lub minutę.
# Przykład zeg = Zegar(0, 2, 45) zeg.add_time(second=20) print(zeg) >>> <zeg h=0, m=3, s=5>

class Czas:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours;
        self.minutes = minutes;
        self.seconds = seconds;

    def __str__(self):
        return ("<zeg h={}, m={}, s={}>".format(self.hours, self.minutes, self.seconds))

    @classmethod
    def __get_name(cls):
        return cls.__name__

    def set_time(self, h=12, m=34, s=66):
        if h:
            self.hours = h
        if m:
            self.minutes = m
        if s:
            self.seconds = s

    def upTime(self, h=0, m=0, s=0):
        if h:
            self.hours += h
            if self.hours >= 24:
                self.hours -= 24

        if m:
            self.minutes += m
            if self.minutes // 60 >= 1:
                self.hours += self.m // 60

        if s:
            if self.seconds + s > 59:
                self.minutes +=1
                self.seconds = self.seconds + s - 60


n_czas = Czas(hours=11, minutes=45, seconds=50)
print(n_czas)
n_czas.upTime(24, 20,25)
print(n_czas)
