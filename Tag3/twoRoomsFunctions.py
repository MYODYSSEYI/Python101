import math

print("Der Quader\n")

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
    Mantelfl = round(2*a*c++2*b*c)
    print(f"Mantelfläche:           {Mantelfl}\n")

print("Gib die Werte für den ersten raum ein: ")

v_R1a = float(input('Gib einen Wert für "a" an.\n'))
v_R1b = float(input('Gib einen Wert für "b" an.\n'))
v_R1c = float(input('Gib einen Wert für "c" an.\n'))


print(f"Grundfläche Raum 1: ")
f_Grundfl(v_R1a, v_R1b)

print("Gib die Werte für den zweiteb raum ein: ")

v_R2a = float(input('Gib einen Wert für "a" an.\n'))
v_R2b = float(input('Gib einen Wert für "b" an.\n'))
v_R2c = float(input('Gib einen Wert für "c" an.\n'))



print(f"Mantelfläche Raum 2: ")
f_Mantelfl(v_R2a, v_R2b, v_R2c)
