"""
Wymagania:
Sprawdź rezultat gry w kółko i krzyżyj
input: string 9 znaków skłądających się z: x, o, -
znaki oznaczają pozycje wierszami od górnego wiersza
Rezultat wypisz na ekran.
"""
###pobieranie ruchów
ruchy = input(str("Wprowadz 9 ruchów  x,o lub -: "))
winx = ('xxx')
wino = ('ooo')
### kombinacje mozliwe dla x
if ruchy[0] + ruchy[1] + ruchy[2] == winx:
    print("Win X")
elif ruchy[0] + ruchy[3] + ruchy[7] == winx:
    print("Win X")
elif ruchy[2] + ruchy[5] + ruchy[8] == winx:
    print("Win X")
elif ruchy[0] + ruchy[4] + ruchy[8] == winx:
    print("Win X")
elif ruchy[2] + ruchy[4] + ruchy[6] == winx:
    print("Win X")
elif ruchy[6] + ruchy[7] + ruchy[8] == winx:
    print("Win X")

#kombinacje mozliwe dla o
if ruchy[0] + ruchy[1] + ruchy[2] == wino:
    print("Win O")
elif ruchy[0] + ruchy[3] + ruchy[7] == wino:
    print("Win O")
elif ruchy[2] + ruchy[5] + ruchy[8] == wino:
    print("Win O")
elif ruchy[0] + ruchy[4] + ruchy[8] == wino:
    print("Win O")
elif ruchy[2] + ruchy[4] + ruchy[6] == wino:
    print("Win O")
elif ruchy[6] + ruchy[7] + ruchy[8] == wino:
    print("Win O")