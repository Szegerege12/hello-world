"""
Wymagania:
Pobierz od użytkownika nazwę miesiąca.
Pobierz od użytkownika rok.

Wskaż liczbę dni w miesiącu.
Rezultat wypisz na ekran.
"""

### pobieranie nazwy miesiaca i roku
month = int(input("Number of month: "))
year = int(input("Year: "))
from calendar import monthrange
wynik = monthrange(year,month)
print(wynik)