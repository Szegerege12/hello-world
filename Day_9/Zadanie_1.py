"""
Wymagania:
Napisz klasę mającą dwie metody:
- get_string
- print_string

get_string - pobiera od użytkownika stringa
print_string - wypisuje stringa na ekran - co druga litera powinna być wielka.

Przykład:
asdasdasdasd -> 'AsDaSdAsDaSd'
"""
from itertools import chain
class Wydruk(object):
    def __init__(self):
        self.class_string=""
    def get_string(self):
        self.claas_string = input("Podaj wyraz: ")

    def print_string(self):
        maly = self.claas_string[1::2].lower()
        duzy = self.claas_string[::2].upper()
        lista = list(chain(*zip(duzy, maly)))
        print("".join(lista))

str = Wydruk()
str.get_string()
str.print_string()
