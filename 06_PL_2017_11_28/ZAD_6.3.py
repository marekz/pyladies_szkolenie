# Stwórz klasę DokładnyZegar, która dziedziczy po Zegar
# i która jeszcze będzie przyjmowała opcjonalnie milisekundy.

class Czas:

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours;
        self.minutes = minutes;
        self.seconds = seconds;

class Zegar(Czas):

    def __init__(self, t_format, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.t_format = t_format

class DokladnyZegar(Zegar):
    def __init__(self, *args, m_sec=0, **kwargs):
        super().__init__(*args, **kwargs)
        self.m_sec = m_sec

"""
argument pozycyjne potem *args
argument nazwane a potem *kwargs

"""

m_zeg = DokladnyZegar('12H', 11, m_sec=2, hours=10, seconds=11, minutes=12)
print(m_zeg.seconds)
print(m_zeg.minutes)
print(m_zeg.hours)
print(m_zeg.m_sec)