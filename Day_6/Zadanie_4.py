"""
Sprawdz czy słowo lub fraza jest anagramem –
czy czytane w przód i wspak jest identyczne

Podpowiedź:
Użyj funkcji do odwracania stringa z Zadania_1

Nie zapomnij o dokumentacji
Przygotuj zestaw danych testowych
"""

def is_anagram(str1,str2):
    """
    Funkcja sotujaca podane wyrazy w listy, i sprawdzajaca znaki czy sa anagramami
    :param str1:
    :param str2:
    :return: boolean
    """
    list_str1=list(str1)
    list_str1.sort()
    list_str2=list(str2)
    list_str2.sort()

    return (list_str1 == list_str2)

print(is_anagram('anagram','margana'))
print(is_anagram('cat','tac'))