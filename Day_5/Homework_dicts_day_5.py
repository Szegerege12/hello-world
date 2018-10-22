"""
Wymagania:
Napisz program który będzie pytać o podanie imienia,
dodaje imię do słownika,
zapyta co chcemy zrobić :
    czy imie jest w słowniku,
    dodac do słownika,
    usunąć ze słownika,
    podać liczbę imion w słowniku,
    wypisac imiona,
    wypisać imię i jego liczbę wystąpień
    wyjść z programu
    kontynuować podawanie imion

Każdą wykonaną opcję proszę opatrzyć stosownym komunikatem

Pomyśl:
Jak wykorzystać słownik, co zrobić gdy podane imię już istnieje?
Jak policzyć liczbę imion w słowniku?
"""
### podawanie imienia
name = ()
slownik = {}
while True:
    print("-"*10)
    name = input(str("Prosze podac imie, lub 'q' aby wyjsc: "))
    print("-" * 10)
    if name == 'q':
        break
    else:
        nr = input("Prosze podac nr: ")
        slownik[name] = nr
    for key,val in slownik.items():
         print(key,'=',val)

print("-"*10)
wybor = str(input("Nacisnij: \n"
                  "C - by sprawdzic czy imie jest w slowniku\n"
                  "R - by usunac imie ze slownika\n"
                  "L - by sprawdzic liczbe imion w slowniku\n"))
if wybor == 'c':
    szukaj = input("Jakie imie chcesz wyszukac: ?")
    if szukaj in slownik:
            print("Imie wystepuje")
    else:
            print("Podane imie nie wystepuje w slowniku")
elif wybor == 'r':
    usun = input("Jakie imie chcesz usunac ze slownika?: ")
    del slownik[usun]
    print("Imie",usun,"zostalo usuniete ze slownika")
    print(slownik)
elif wybor == 'l':
    liczenie = (len(slownik))
    print("Liczba imion w słowniku to:",liczenie,)
