"""
Wymagania:
Napisz funkcję odwaracjącą podanego stringa.
Nie zapomnij o dokumentacji
"""
def odwroc(wyraz):
    """Reversed copy of string
    :param wyraz
    :return wyraz"""
    return wyraz[::-1]


if __name__ == '__main__':
    wyraz = str(input("Podaj wyraz do odwrócenia: "))
    print("Oryginalny wyraz",wyraz)
    print("Odwrócony wyraz",odwroc(wyraz))