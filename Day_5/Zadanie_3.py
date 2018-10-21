"""
Wymagania:
Napisz program, który wczytuje od użytkownika stringi w postaci klucz - wartość
Dodaj je do słownika.
Jeśli dany klucz istnieje w słowniku - nie rób nic.

Zapewnij możliwość podania kolejnych par klucz-wartość lub zaprzestawania ich podawania.

Wypisz elementy słownika na ekran w formie "klucz -> wartość"

Podpowiedź:
Użyj dwóch inputów do pobrania wartości
"""
### pobieranie informacji od uzytkownika

slownik = {}
while True:
    imie =input("Prosze podac nazwisko wlasciciela pojazdu[nacisnij q zeby wyjsc): ")
    if imie == 'q':
        break
    else:
        pojazd =input("Prosze podac marke samochodu: ")
        slownik[imie]=pojazd

for key, value in slownik.items():
    print(key," = ",value)
