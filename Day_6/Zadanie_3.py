"""
Wymagania:
Sprawdz czy strint jest pangramem –
zawiera wszystkie litery z alfabetu angielskiego
Np.:
"The quick brown fox jumps over the lazy dog"

Nie zapomnij o dokumentacji
Przygotuj zestaw danych testowych
"""
def is_pangram(phrase):
    '''

    :param phrase:
    :return:
    '''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in phrase:
            return False

    return True

if __name__ == '__main__':
    print(is_pangram('dupa'))
    print(is_pangram('The quick brown fox jumps over the lazy dog'))