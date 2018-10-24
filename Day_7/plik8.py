### odczytywanie pliku z zadania drugiego, przy wyswietlaniu kolejnych linii pliku
with open ('dane_osobowe_csv', mode='r') as plik:
    for line in plik:
        print(line, end='')

with open('mezczyzni_csv', mode='w') as plik1:
    for line in plik1:
        print(line, end='')