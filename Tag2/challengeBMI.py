'''
Erstelle ein Programm, das auf Grund eingegebener Werte für Größe und Gewicht den BMI Brechnet.
Formel:
kg/m²
Untergewicht < 18.5
Normalgewicht 18.5 <= 24.9
Übergewicht 25 <= 29.9
Adipositas 30 <= 34.9
Sumo >= 35
'''

import math

Gewicht = float(input("Dein Gewicht: "))
Groesse = float(input("Dein Gewicht: "))**2

BMI = Gewicht / Groesse

if BMI < 18.5:
    print(f"Untergewicht: {BMI}")
elif BMI == 18.5 <= 24.9:
    print(f"Normalgewicht: {BMI}")  
elif BMI == 25 <= 