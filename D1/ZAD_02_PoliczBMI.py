print("Wylicz BMI: ");
waga    = input("Podaj wagę: ");
wzrost  = input("Podaj wzrost: ");
bmi = float(waga) / (float(wzrost) ** 2);
print("Twoje BMI: " + str(bmi));