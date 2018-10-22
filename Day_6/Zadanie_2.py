"""
Wymagania:
Napisz funkcję, sprawdzającą czy dana liczba jest w podanym zakresie liczb.

1. Weź pod uwagę zakres jako przekazywaną kolekcję (listę)
2. Weż pod uwagę zakres jako range(liczba)

Nie zapomnij o dokumentacji
Przygotuj zestaw danych testowych
"""
def sprawdzenie_1(liczba,lista):
    """
    :param liczba:
    :param lista:
    :return:
    """
    if liczba in lista:
        print('Liczba znajduje sie na liscie')
    else:
        print('Liczba nie znajduje sie na liscie')

if __name__ == '__main__':
    sprawdzenie_1(1,[1,2,3])
    sprawdzenie_1(1,range(2,8))
