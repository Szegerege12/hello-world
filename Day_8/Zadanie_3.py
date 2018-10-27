"""
Wymagania:
Zrefaktoruj Zadanie_2 w tym pliku:
Stwórz nowy plik na podstawie pliku z Zadania_2 - nazwij go dane_zadanie_3.csv
użyj 'with open' do obsługi plików
Użyj funkcji
Użyj obsługi błędów aby upewnić się, że rok jest daną numeryczną
Dodaj kolumnę "Wiek", wartość ma być obliczona z obecnego roku przy użyciu danych z kolumny Rok_Urodzenia

Następnie otwórz plik i wypisz jego zawartość na ekran.

Podpowiedź:
Użyj pliku db_engine jako wzoru
"""
names_list = []
welcome_message = "Baza danych\
\nWybierz opcję:\
\nDodaj wiersz do programu 1:\
\nZakoncz dzialanie programu 2:\ "

import csv

def action(note):
    """
    Input dla okreslonej zmiennej
    :param note:
    :return:
    """
    return input(note)

decyzja = action(welcome_message)
while decyzja != '2':
    if decyzja == '1':
        imie = str(input('Podaj imie: '))
        nazwisko = str(input('Nazwisko: '))
        data_ur = str(input('Rok urodzenia: '))
        wiek = int(input('Wiek: '))
        with open('dane_zadanie_4.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            writer.writerow([imie, nazwisko, data_ur, wiek])
    else:
        print('Podales zle polecenie')

    decyzja = str(input("Podaj nowe polecenie: "))