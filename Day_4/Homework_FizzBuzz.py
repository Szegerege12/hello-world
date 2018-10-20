"""
Wymagania:
Biorąc pod uwagę liczby od 1 do 100(włącznie)
napisz "Fizz" jeśli liczba jest podzielna przez 3
napisz "Buzz" jeśli liczba jest podzielna przez 5
napisz "FizzBuzz" jeśli liczba jest podzielna przez 3 i przez 5
jeśli nie spełnia żadnego z tych warunków wypisz liczbę.

1 - użyj pętli while
2 - użyj pętli for
"""
x = int(input("Podaj liczbe: "))
### wczytywanie liczby
for i in range(1,100):
    if x % 3 ==0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 5 and i % 3 == 0:
        print("FizzBuzz")