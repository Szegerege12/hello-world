"""
Wymagania:
Sprawdź czy podana przez użytkownika liczba
jest podzielna przez 3, 5, 7

Wypisz wyniki na ekran.

Pamiętaj o komentarzach.
Rezultat wypisz na ekran.

Podpowiedź:
Odpowiednio formatuj stringi
"""
### wprowadzanie liczby pamietac o int.input!!!
liczba = int(input('Wprowadz liczbe: '))

##sprawdzanie warunków dla 3, 5 ,7
if liczba%3==0:
    print("Wprowadzona liczba jest podzielna przez '3'")
else:
    print("Wprowadzona liczba jest niepodzielna przez 3")