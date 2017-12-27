# Stwórz klasę Zegar, która dziedziczy po Czas
# a konstruktor (__init__) będzie brał obowiązkowo parametr format (12H lub 24H) oprócz tych co Czas.

class Czas:

    hours = 0
    minutes = 0
    seconds = 0


    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours;
        self.minutes = minutes;
        self.seconds = seconds;


class Zegar(Czas):

    def __init__(self, t_format, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.t_format = t_format

zeg = Zegar('12H', 11, seconds=11, minutes=12)
print(zeg.seconds)
print(zeg.minutes)
print(zeg.hours)