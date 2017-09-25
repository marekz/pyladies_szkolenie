text_1 = "Ala ma kota a kot ma Ale";
text_2 = "Pyladies.start() ma przerwe obiadową o godz 14";

# inserted = input("Wprowadź tekst do podzielenia: ");

selected = text_1;
# selected = text_2;
# selected = inserted;
selectedLength = len(selected);
halfSelected = int(selectedLength)/2;
halfString = selected[0:int(halfSelected)];
print(halfString);