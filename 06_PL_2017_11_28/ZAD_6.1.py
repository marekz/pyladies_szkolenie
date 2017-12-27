# Stwórz klasę Czas, której konstruktor (__init__) będzie brał trzy opcjonalne argumenty, godzine, minuty, sekundy i zapisywal je w odpowiednich zmiennych w klasie.

class Czas:

    hours = 0
    minutes = 0
    seconds = 0


    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours;
        self.minutes = minutes;
        self.seconds = seconds;


    # __str__(self):
    #     pass
    #
    # set_time(self):
    #     pass
    #
    # add_time(self):
    #     pass
    #
    # get_seconds(self):
    #     return self.seconds
    #
    # get_minutes(self):
    #     return self.minutes
    #
    # get_hours(self):
    #     return self.hours


class Zegar:
    pass

class DokładnyZegar:
    pass



def mojprint():
    pass

m_czas = Czas(1,2,3)
print(m_czas.hours)
print(m_czas.minutes)
print(m_czas.seconds)
