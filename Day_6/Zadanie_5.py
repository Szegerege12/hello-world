"""
Zadanie z treścią:
Ania chce kupić klawiaturę k oraz pendrive p.
Posiada ustaloną kwotę pieniędzy p.
W sklepie są potane ceny w listach klawiatury i pendrivy.
Ania chce wykorzystać możliwie całą gotówkę, aby kupić klawiaturę i pendrive.


Weż pod uwagę, że Ania potrzebuje zarówno klawiatury jak i pendrive -
zakupienie jednej rzeczy nie wchodzi w grę.
Sprawdź czy uda jej się to zrobić - jeśli tak, wypisz wydaną sumę pieniędzy,
jeśli nie - podaj stosowny komunikat.

Przykładowe dane i wynik:
k = [500 ,125 ,50, 21, 13]
p = [10, 17, 28, 75]
s = 50

wynik:
Ania wydała 50zł na klawiaturę i pendrive (klawiatura kosztowała 21zł, a pendrive 28zł)
wydała 50zł na klawiaturę i pendrive (klawiatura kosztowała 21zł, a pendrive 28zł
########################################################################################################################

k = [500 ,125 ,450, 21, 66]
p = [100, 170, 30, 75]
s = 50

wynik:
Ani nie udało się zrobić zakupów za 50zł.
"""
### deklaracja list zawierajacych ceny klawiatur i pendirve

klawiatury = [11 , 17 , 18 , 23, 67 , 44 , 60 , 99]
pendrive = [16, 19, 26, 25, 30, 49, 39]

### wyswietlenie cennika
print("###cennik klawiatur###")
for counter, value in enumerate(klawiatury, start=1):
    print(counter, value,"zl")

print("###cennik pendrivów###")
for counter, value in enumerate(pendrive, start=1):
    print(counter, value,"zl")
### wprowadzenie pieniedzy przez klientke

srodki=int(input("Prosze podac wysokosc srodków przeznaczonych na zakupy: "))
klawiatura_cena=int(input("Prosze podac cene klawiatury: "))
pendrive_cena=int(input("Prosze podac cene pendrive: "))
suma = klawiatura_cena + pendrive_cena

if srodki >= suma:
    print("Zakup udany. Wydane na klawiature",klawiatura_cena,"Wydane na pendrive",pendrive_cena,"Wydane srodki razem:",suma,"zl")
else:
    print("Za malo srodkow")

