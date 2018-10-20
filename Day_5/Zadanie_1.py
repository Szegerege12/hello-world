"""
Wymagania:
Stwórz listę kolorów.
Wypisz je w kolejności.

NAstępnie wybierz losowo jeden z kolorów,
przypisz go do nowej zmiennej i wypisz na ekran.

Podpowiedź:
Skorzystaj z modułu random
"""
### deklaracja tabeli i wyswietlenie w kolejnosci
kolory = ['czarny','bialy','czerwony','niebieski','zielony']
print(kolory)

### import modulu random
import random
##import funkcji choice z modulu random
from random import choice

### przypisanie nowej zmiennej
losowy = (random.choice(kolory))
print("Losowy kolor z listy to:",losowy,)