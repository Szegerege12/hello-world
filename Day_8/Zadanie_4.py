"""
Opis:
Kod oblicza i wypisuje BMI z podanej wagi i wzrostu.

Popraw błędy (zdebuguj kod)
"""
patients = [[70, 1.8], [80, 1.9], [150, 1.7]]

def calculate_bmi(height, weight):
    return weight / (height ** 2)

for patient in patients:
    weight, height = patient
    bmi = calculate_bmi(height, weight)
    print(patient)
    print(bmi)
    print("Patient's BMI is: {:.2f}".format(bmi))