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
    print('Liczba ',liczba, 'jest podzielna przz 3')
else:
    print('Liczba ',liczba, 'jest niepodzielna przz 3')

if liczba%5==0:
    print('Liczba ',liczba, 'jest podzielna przz 5')
else:
    print('Liczba ',liczba, 'jest niepodzielna przz 5')
if liczba%7==0:
    print('Liczba ',liczba, 'jest podzielna przez 7')
else:
    print('Liczba',liczba, 'jest niepodzielna przez 7')