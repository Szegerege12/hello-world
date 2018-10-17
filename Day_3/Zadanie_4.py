"""
Wymagania:
Sprawdź czy podany rok jest rokiem przestępnym.
Rezultat wypisz na ekran.

Podpowiedź:
jest podzielny przez 4, ale nie jest podzielny przez 100
jest podzielny przez 400
"""
### zapytanie o rok
rok = int(input("Podaj rok: "))

### sprawdzanie warunkow
if (rok % 4 == 0) and (rok % 100 !=0) or (rok % 400 == 0):
    print("Rok",rok,"jest rokiem przestepnym")
else:
    print("Rok",rok, "nie jest rokiem przestepnym")



