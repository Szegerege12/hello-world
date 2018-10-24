"""
Pobierz dane numeryczne od użytkownika i zapisz je do listy.
Użyj obsługi wyjątków by zwrócić użytkownikowi uwagę, gdy poda dane nienumeryczne.
Kontynuuj pytanie o dane dopóki użytkownik nie wpisze litery "N"
"""
"""
### opcja pierwsza
list_numbers = []
while True:
    dane = input("Podaj wartosci do wprowadzenia do tablicy\n"
                 "(aby przerwać działanie programu nacisnij N): ")
    try:
        if dane == 'N':
            break
        else:
            list_numbers.append(float(dane))
    except ValueError:
        print("Wpisales wartosc inna niz liczbowa")

"""

### opcja druga
lista_numerow = []
dane = None
while dane != 'N':
    dane = input("Podaj wartosci do wprowadzenia do tablicy\n"
                 "(aby przerwać działanie programu nacisnij N): ")
    try:
        lista_numerow.append(float(dane))

    except ValueError:
        if dane == 'N':
            print('dziekujemy za skorzystanie z naszego programu')
        else:
            print(f"Wpisałeś '{dane}'!!\nPowinieneś podać numer!")

print(lista_numerow)
