"""
Wymagania:
Wypisać logiką boolowską pierwsze i drugie prawo de morgana
oraz
rozpisać poszczególne tabele wartości logicznych

Restrykcje:
Nie wolno dostarczać znaków z zewnątrz

Podpowiedzi:
https://pl.wikipedia.org/wiki/Prawa_De_Morgana
"""
# De Morgan law:
A = True
B = True
x = (not(A and B)) == ((not A) or (not B))
y = (not(A or B)) == ((not A) and (not B))
z = (A or B) == (not(not A) and (not B))
print("Pierwsze prawo DeMorgana:")
print(x)
print("Drugiee prawo DeMorgana:")
print(y)
print("Alternatywa:")
print(z)

#tabele wartosci logicznych
print("Tabela AND")
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print("Tabela OR")
print(True or True)
print(True or False)
print(False or True)
print(False and False)