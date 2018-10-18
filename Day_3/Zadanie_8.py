"""
Wymagania:
pobrać od użytkownika miesiąc i dzień
Określić porę roku.

Rezultat wypisać na ekran
"""
### pobieranie od uzytkownika miesiaca i dnia
day = int(input("Prosze podac dzien: "))
month = str(input("Prosze podac miesiac(styczen,luty,itd): "))

### sprawdzanie po zakresach miesiaca
if month in('Styczen','Luty','Marzec'):
    sezon = 'zima'
elif  month in('Marzec','Kwiecien','Maj'):
    sezon = 'wiosna'
elif  month in('Styczen','Luty','Marzec'):
    sezon = 'lato'
else:
    sezon = 'jesien'

### sprawdzanie po zakresach dnia
if (month == 'Marzec') and (day >= 21):
    sezon = 'wiosna'
elif (month == 'Czerwiec') and (day >= 22):
    sezon = 'lato'
elif (month == 'Wrzesien') and (day >= 23):
    sezon = 'jesien'
elif (month == 'Grudzien') and (day >= 22):
    sezon = 'zima'


### wypisanie por roku
print("Obecna pora roku to:",sezon,)