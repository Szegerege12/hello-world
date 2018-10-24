"""
Wymagania:
Utwórz plik dane_osobowe.csv z 10 wierszami, zawierającymi dane:
Imię, Nazwisko, Data_Urodzenia, Płeć, Adres_Ulica, Adres_Nr_Domu, Adres_Nr_Lokalu, Adres_Kod_Pocztowy, Adres_Miasto

Następnie na podstawie utworzonego pliku utwórz dwa nowe:
dane_kobiety.csv
dane_mezczyzni.csv
zawierające odpowiednie rekordy z pliku dane_osobowe.csv
"""
def append_to_file(file_name, lines):
    """
    Funkcja dodajaca linijke do pliku o podanej nazwie
    :param file_name: 
    :param lines: 
    :return: 
    """
    with open(file_name, 'a+') as f:
        lines = [line if line[-1] == '\n' else line+'\n' for line in lines]
        f.writelines(lines)


### importowanie modulu csv
import csv
### tworzenie pliku o nazwie dane_osobowe_csv i kolejne dodawanie do niego wierszy wg. polecenia(klucza)
with open('dane_osobowe1.csv', 'w', newline='') as csvfile:
    w = csv.writer(csvfile, delimiter=',')
    w.writerow(['Imie','Nazwisko','Data_Urodzenia','Płec','Adres','Kod_Pocztowy'])
    w.writerow(['Marek', 'Szynszyl', '1994', 'M', 'Lublin', '24-220'])
    w.writerow(['Kamil', 'Lemieszek', '1986', 'M', 'Babin 33', '24-550'])
    w.writerow(['Anna', 'Jantar', '1960', 'K', 'Warszawa', '03-030'])
    w.writerow(['Andrea', 'Breivik', '1986', 'K', 'Norwegia', '66-360'])
    w.writerow(['Tomasz', 'Jachimek', '1970', 'M', 'Warszawa 17', '03-330'])
    w.writerow(['Agata', 'Klepka', '1925', 'K', 'Wawolnica', '34-223'])
    w.writerow(['Anna', 'Kozidrak', '1966', 'K', 'Uniszowice', '24-100'])
    w.writerow(['Agnieszka', 'Tupolew', '1980', 'K', 'Strzeszkowice 33', '24-220'])
    w.writerow(['Adam', 'Pałka', '1965', 'M', 'Strzeszkowice Duże 12', '24-220'])


with open('dane_osobowe1.csv', 'r') as csvfile:
    linie = csvfile.readlines()
    print(linie)
    for i in linie:
        plec = i.split(',')[3]
        print(plec)
        if plec == 'K':
            append_to_file('kobiety.csv', [1])
        elif plec == 'M':
            append_to_file('mezczyzni.csv', [1])
        else:
            print('bledna plec')

