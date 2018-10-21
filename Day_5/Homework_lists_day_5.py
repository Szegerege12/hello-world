"""
Wymagania:
Napisz program który będzie pytać o podanie imienia,
dodaje do listy,
zapyta co chcemy zrobić :
    czy imie jest w liście,
    dodac do listy,
    usunąć z listy,
    podać liczbę imion w liscie,
    wypisac imiona,
    wyjść z programu
    kontynuować podawanie imion

Każdą wykonaną opcję proszę opatrzyć stosownym komunikatem
"""
lista = []
print("Witaj w programie. Jesli chcesz zakonczyć jego działanie kliknij klawisz 'q'\n")

while True:
    imie = input(str("Podaj imie: "))
    if imie == 'q':
        break
    else:
        lista.append(imie)

print("Aby sprawdzić ile elementow jest w liscie nacisnij przycisk 'E'\n"
      "Aby wypisac imiona z listy kliknij przycisk 'P'\n"
      "Aby dodac imie do listy kliknij 'd'")
decyzja = str(input("Co chcesz teraz zrobic: "))
if decyzja == 'e':
    licznik = len(lista)
    print("Aktualnie na liscie jest:",licznik,"pozycji")
elif decyzja == 'p':
    print("Twoja lista imion to:\n",lista,)
elif decyzja == 'd':
    dodanie = str(input("Podaj imie ktore chcesz dodac do listy: "))
    lista.append(dodanie)
    print(lista)