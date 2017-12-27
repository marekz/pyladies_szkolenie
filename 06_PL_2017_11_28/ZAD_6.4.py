# Zaimplementuj metodę magiczną __str__,
# która wyświetli aktualne wartości np. <zeg h=0, m=3, s=5>

class Czas:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours;
        self.minutes = minutes;
        self.seconds = seconds;
    def __str__(self):
        return ("<zeg h={}, m={}, s={}>".format(self.hours, self.minutes, self.seconds))

class Zegar(Czas):
    def __init__(self, t_format, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.t_format = t_format

    def __str__(self):
        temp = super().__str__()
        temp+= " format = {}".format(self.t_format)

class DokladnyZegar(Zegar):
    def __init__(self, *args, m_sec=0, **kwargs):
        super().__init__(*args, **kwargs)
        self.m_sec = m_sec

    def __str__(self):
        return ("<zeg h={}, m={}, s={}>".format(self.hours, self.minutes, self.seconds))

m_zeg = Zegar('12H', hours=11, seconds=33, minutes=21)

print(m_zeg)