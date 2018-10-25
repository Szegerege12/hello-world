"""
Wymagania:
Napisz program który stworzy plik csv (nazwij go dane_zadanie_2.csv) z danymi pobieranymi od użytkownika:
Imię, Nazwisko, Rok_Urodzenia. (w pętli)
Nie używaj funkcji.
Nie używaj obsługi wyjątków.
Użyj file.open() i file.close()

Następnie otwórz plik i wypisz jego zawartość na ekran.

Podpowiedź:
Użyj pliku db_engine_before_refactoring jako wzoru
"""
lista = []
import csv

decyzja = str(input("Witaj w programie. Jesli chcesz wpisac imiona nacisnij klawisz 1, jezeli chcesz zakonczyc nacisnij klawisz 2: "))
while decyzja != '2':
    if decyzja == '1':
        imie = str(input('Podaj imie: '))
        nazwisko = str(input('Nazwisko: '))
        data_ur = str(input('Rok urodzenia: '))
        with open('dane_zadanie_3.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            writer.writerow([imie, nazwisko, data_ur])
    else:
        print('Podales zle polecenie')

    decyzja = str(input("Podaj nowe polecenie: "))

