while True:
    liczba = int(input("Podaj liczbe: "))
    if liczba > 10:
        print("Podałeś liczbę większą niż 10. Koniec imprezy.")
        break
    else:
        print("Podałeś liczbę mniejszą niż 11, dawaj dalej!")


for liczba in range(100):
    if liczba % 2 == 0:
        print(f"Wypisuję tylko liczby odzielne przez 2: {liczba}")
