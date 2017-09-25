from math import pow;

print("Wylicz BMI: ");
czy_kolejna = True

while czy_kolejna:
    waga    = input("Podaj wagę: ");
    wzrost  = input("Podaj wzrost: ");
    bmi = round((float(waga)/pow((float(wzrost))/100,2)), 2);

    statusBMI = "";

    if bmi <= 20:
        statusBMI = "niedowaga";
    elif bmi > 25:
        statusBMI = "nadwaga";
    else:
        statusBMI = "ok";

    print(statusBMI);
    print("Dla wagi: {0} i wzrostu {1} BMI: {2}".format(waga, wzrost, str(bmi)));

    czy_nastepna = input("Wyjść z programu? ")

    if czy_nastepna == 't':
        czy_kolejna = False