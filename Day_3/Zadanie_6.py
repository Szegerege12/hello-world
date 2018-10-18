"""
Wymagania:
Pobierz od użytkownika długości boków trójkąta.
Sprawdź czy da się utworzyć trójkąt.
Sprawdź jaki to rodzaj trójkąta:
różnoboczny,
równoramienny,
równoboczny,

Dla chętnych:
prostokątny,
ostrokątny,
rozwartokątny
- skorzystaj z prawa cosinusów - uważaj na precyzję
Podpowiedź:
przydatne moduły:
from math import acos, degrees
"""

### pobieranie długosci trójkąta
a = int(input("Prosze podac bok a: "))
b = int(input("Prosze podac bok b: "))
c = int(input("Prosze podac bok c: "))
if a+b>c and a+c>b and b+c>a:
    print("Trójkąt o podanych bokach może zostać utworzony")
else:
    print("Bład!Trójkat o podanych bokach nie może zostać utworzony")

### sprawdzanie jaki to rodzaj trojkata
if a == b == c:
    print("Trojkat rownoboczny")
elif a !=b !=c:
    print("Trójkat różnoboczny")
else:
    print("Trójkat równoramienny")