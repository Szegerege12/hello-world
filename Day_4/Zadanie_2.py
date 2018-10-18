"""
Wymagania:
napisz program który wypisze
liczby od 0 do 20 poza liczbami podzielnymi przez 4
"""
x = range(20)
for i in x:
    if i % 4 !=0:
        print(i)