import csv

with open('kobiety_csv', 'w') as f2:
    with open('dane_osobowe_csv',mode='r') as infile:
        reader = list(csv.reader(infile)) ### calosc do listy
        header = reader[0] ### pierszy wiersz to naglowek
        for row in reader:
            if 'Plec' == 'K':
                print(row(Imie)

plik = open('kobiety_csv', mode='r')
for line in plik:
    print(line)