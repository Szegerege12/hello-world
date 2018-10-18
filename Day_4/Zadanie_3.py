"""
Wymagania:
Napisz program wypisujący tabliczkę mnozenia (1 do 10)
dla podanej przez użytkownika liczby

Wynik powinien wyglądać tak:
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
itd.
"""
### pobieranie liczby
liczba = int(input("Podaj liczbe: "))

### petla 11 operacji dla zmiennego i i liczby
for i in range(1,11):
    print(liczba,'x',i,'=',liczba * i)
