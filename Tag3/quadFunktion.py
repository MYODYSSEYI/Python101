'''
Der Quader a, b, c input... alle formeln berechnen.

a 
b 
Raumdiagonale e = 
umfang u = 
Grundfläche G = 
Mantelfläche M = 
c 
Oberfläche O = 
Volumen V = 
Länge aller Seiten I = 
Flächendiagonale d 
Flächendiagonale dsc 
Flächendiagonale d
''' 
import math

'''
a = float(input('Gib einen Wert für "a" an.\n'))
b = float(input('Gib einen Wert für "b" an.\n'))
c = float(input('Gib einen Wert für "c" an.\n'))
'''

def f_Raum(a, b, c):
    Raumdiagonale = round(math.sqrt(a**2+b**2+c**2))
    print(f"\nRaumdiagonale:          {Raumdiagonale}\n")
def f_Umfang(a, b):
    Umfang = round(2*a+2*b)
    print(f"Umfang:                 {Umfang}\n")
def f_Grundfl(a, b):
    Grundfl = round(a*b)
    print(f"Grundfläche:            {Grundfl}\n")
def f_Mantelfl(a, b, c):
    Mantelfl = round(2*a*c+2*b*c)
    print(f"Mantelfläche:           {Mantelfl}\n")

print("Was möchtest du berechnen?\n")
v_Auswahl = input("Raumdiagonale     [e]\n" + "Umfang            [u]\n" + "Grundfläche       [G]\n" + "Mantelfläche      [M]\n")

if v_Auswahl == "e" or v_Auswahl == "E":
    a = float(input('Gib einen Wert für "a" an.\n'))
    b = float(input('Gib einen Wert für "b" an.\n'))
    c = float(input('Gib einen Wert für "c" an.\n'))
    f_Raum(a, b, c)
elif v_Auswahl == "u" or v_Auswahl == "U":
    a = float(input('Gib einen Wert für "a" an.\n'))
    b = float(input('Gib einen Wert für "b" an.\n'))
    f_Auswahl(a, b)
elif v_Auswahl == "G" or v_Auswahl == "g":
    a = float(input('Gib einen Wert für "a" an.\n'))
    b = float(input('Gib einen Wert für "b" an.\n'))
    f_Grundfl(a, b)
elif v_Auswahl == "M" or v_Auswahl == "m":
    a = float(input('Gib einen Wert für "a" an.\n'))
    b = float(input('Gib einen Wert für "b" an.\n'))
    c = float(input('Gib einen Wert für "c" an.\n'))
    f_Mantelfl(a, b, c)
else:
    pass 
