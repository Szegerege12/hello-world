"""
Wymagania:
Napisz funkcję, sprawdzającą czy dana liczba jest w podanym zakresie liczb.

1. Weź pod uwagę zakres jako przekazywaną kolekcję (listę)
2. Weż pod uwagę zakres jako range(liczba)

Nie zapomnij o dokumentacji
Przygotuj zestaw danych testowych
"""
def zdanie(boolean):
    """
    Funkcja wyswietlajaca odpowiednie zdanie w zaleznosci od warunku logicznego boolean
    :param boolean:
    :return: string:
    """
    nie = ""
    if not boolean:
        nie = "nie"
    return f"Podana liczba {nie} jest w zakresie"
def sprawdzenie_1(liczba,lista):
    """
    Sprawdza czy podana liczba znajduje sie w podanej kolekcji liczb(lista)
    :param liczba:
    :param lista:
    :return:
    """
    return liczba in lista

def sprawdzenie_2(liczba,range_of_numbers):
    """

    :param liczba:
    :param range_of_numbers:
    :return: boolean:
    """
    return liczba in range_of_numbers
if __name__ == '__main__':
    print("Sprawdzenie pierwszej funkcji czy liczba jest w kolekcji")
    print(zdanie(sprawdzenie_1(1,[1,2,3])))
    print(zdanie(sprawdzenie_1(4,[1,2])))
    print()
    print("Sprawdzenie drugiej funkcji czy liczba jest w zakresie liczb")
    print(zdanie(sprawdzenie_2(3,range(2,8))))
    print(zdanie(sprawdzenie_2(8,(1,7))))

