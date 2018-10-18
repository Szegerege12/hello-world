"""
Wymagania:
Napisać kalkulator temperatury:
- Stopnie Celcjusza
- Stopnie Farenheita
- Kelviny

Pobrać dane od użytkownika w formacie "35C", "100F" lub "17K"

Wypisać rezultat na ekran.
"""
### pobieranie danych od uzytkownika

temperatura = int(input("Wprowadz liczbe stopni: "))
jednostka = str(input("Wprowadz jednostkę C K lub F: "))
celcjusz = (temperatura -32) * 5.0 / 9.0
farenhait = (temperatura * 9.0 / 5.0) +32
ckelvin = temperatura + 273
kelvinc = temperatura - 273
if jednostka == 'c':
    print("",temperatura,"C to;")
    print("Farenhaidy:",farenhait,)
    print("Kelviny: ",ckelvin,)
elif jednostka == 'f':
    print("",temperatura,"F to:")
    print("Celcjusz:",celcjusz,)
    print("Kelviny:",celcjusz + 273,)
elif jednostka == 'k':
    print("",temperatura,"K to:")
    print("Celcjusz:",kelvinc)
    print("Farenhaidy:" + farenhait * 9/5 - 459.67)