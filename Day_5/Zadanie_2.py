"""
Wymagania:
Napisz program, który wczytuje od użytkownika wartości
i dodaje je do listy dopóki użytkownik nie poda wartości 'nie'

Wypisz listę na ekran.
"""

lista = []
while True:
    n = input("Podaj wartosc: ")
    lista.append(n)
    if  n == ('nie'):
        break

print(lista)