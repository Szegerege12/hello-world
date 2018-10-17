"""
Wymagania:
Napisz algorytm wystawiający ocenę na podstawie punktów uzyskanych na egzaminie
podaj ocenę na podstawie progu procentowego
5 od 90 do 100, 4+ od 80, 4 od 70, 3+ od 60, 3 od 50
Rezultat wypisz na ekran.

Podpowiedź:
przyjmij dane od uzytkownika
zweryfikuj dane
wypisz odpowiedni wynik lub komentarz dotyczący wprowadzonych danych
"""
### wprowadzenie ilosci punktów
liczba_pkt = int(input("Wprowadź liczbę punktów uzyskanych na egzaminie: "))

### sprawdzenie ilosci pkt na dana ocene
if liczba_pkt <=100 and liczba_pkt >=90:
    print("Ocena uzyskana za egzamin to 5")
elif liczba_pkt <=90 and liczba_pkt >=80:
    print("Ocena uzyskana za egzamin to 4+")
elif liczba_pkt <=80 and liczba_pkt >=70:
    print("Ocena uzyskana z egzaminu to 4")
elif liczba_pkt <=70 and liczba_pkt >=60:
    print("Ocena uzyskana z egzaminu to 3+")
elif liczba_pkt <= 60 and liczba_pkt >= 50:
    print("Ocena uzyskana z egzaminu to 3")
else:
    print("Egzamin niezaliczony")
