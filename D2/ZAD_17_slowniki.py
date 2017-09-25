slo_dame_osobiste = {
    'Magda': {
        'Imie': 'Magda',
        'Nazwisko': 'Kamińska',
        'Zawod': 'webdeveloper',
        'Daata urodzenia': 1999,
        'Zainteresowania': [
            'Motocykle',
            'Podróże',
            'Internet'
        ],
        'Stan konta': 1989.12
    },
    'Marek': {
        'Imie': 'Marek',
        'Nazwisko': 'Zdybel',
        'Zawod': 'programista',
        'Daata urodzenia': 1998,
        'Zainteresowania': [
            'Motocykle',
            'Gry komputerowe',
            'Fotografia'
        ],
        'Stan konta': 1989.12
    }
}

print("Stan konta przed zmianą: " + str(slo_dame_osobiste['Marek']['Stan konta']))
slo_dame_osobiste['Marek']['Stan konta'] = slo_dame_osobiste['Marek']['Stan konta'] * 2
print("Stan konta po zmianie: " + str(slo_dame_osobiste['Marek']['Stan konta']))

print("Zainteresowania {0}: {1}".format(slo_dame_osobiste['Magda']['Imie'], slo_dame_osobiste['Magda']['Zainteresowania']))

slo_dame_osobiste['Magda']['Zainteresowania'].append('Wspinanie')
slo_dame_osobiste['Magda']['Zainteresowania'].append('Nurkowanie')

print("Zainteresowania po zmianie {0}: {1}".format(slo_dame_osobiste['Magda']['Imie'], slo_dame_osobiste['Magda']['Zainteresowania']))

print("Nazwisko przed zmianą: " + slo_dame_osobiste['Magda']['Nazwisko'])
slo_dame_osobiste['Magda']['Nazwisko'] = 'Kurek'
print("Nazwisko po zmienie: " + slo_dame_osobiste['Magda']['Nazwisko'])

slo_dame_osobiste['Magda']['Drugie imie'] = 'Beata';
slo_dame_osobiste['Marek']['Drugie imie'] = 'Józek';

slo_dame_osobiste['Magda']['Wiek'] = 18
slo_dame_osobiste['Marek']['Wiek'] = 20

slo_dame_osobiste['Magda']['Wyksztalcenie'] = 'Znaczne'
slo_dame_osobiste['Marek']['Wyksztalcenie'] = 'Duży bagaż'

print(slo_dame_osobiste['Magda'])
print(slo_dame_osobiste['Marek'])

del slo_dame_osobiste['Magda']['Daata urodzenia']
del slo_dame_osobiste['Marek']['Daata urodzenia']

slo_dame_osobiste['Magda']['Wiek'] += 5;
slo_dame_osobiste['Marek']['Wiek'] += 5;

print(slo_dame_osobiste['Magda'])
print(slo_dame_osobiste['Marek'])
