# Zaimplementuj metodę set_time, która pozwoli nadpisać aktualne wartości czasu.

class Czas:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours;
        self.minutes = minutes;
        self.seconds = seconds;
    def __str__(self):
        temp = "{} ".format(self.__get_name())
        for atr in dir(self):
            if not atr.strtswith('_'):
                temp += "{}={} ".format(atr, getattr(self, atr))
        return temp

    @classmethod
    def __get_name(cls):
        return cls.__name__

    def set_time(self, h=0, m=0, s=0):
        if h:
            self.hours = h
        if m:
            self.minutes = m
        if s:
            self.seconds = s


class Zegar(Czas):
    def __init__(self, t_format, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.t_format = t_format

    def __str__(self):
        temp = super().__str__()
        temp += " format={}".format(self.t_format)
        return temp

class DokladnyZegar(Zegar):
    def __init__(self, *args, m_sec=0, **kwargs):
        super().__init__(*args, **kwargs)
        self.m_sec = m_sec

    def __str__(self):
        return ("<zeg h={}, m={}, s={}>".format(self.hours, self.minutes, self.seconds))

    def set_time(self, ms=None, **kwargs):
        super().set_time(**kwargs)
        if ms:
            self.m_sec = ms

m_zeg = Zegar('12H', hours=11, seconds=33, minutes=21)

print(m_zeg)