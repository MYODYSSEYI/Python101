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

print("Der Quader\n\n")

a = float(input('Gib einen Wert für "a" an.\n'))
b = float(input('Gib einen Wert für "b" an.\n'))
c = float(input('Gib einen Wert für "c" an.\n'))

Raumdiagonale = math.sqrt(a**2+b**2+c**2)
Umfang = 2*a+2*b
Grundfl = a*b
Mantelfl = 2*a*c++2*b*c
Oberfl = 2*a*c+2*b*c+2*a*b
Volumen = a*b*c
LenAllSides = 4*a+b+4*c 
FlDiagAB = math.sqrt(a**2+b**2)
FlDiagBC = math.sqrt(c**2+b**2)
FlDiagAC = math.sqrt(a**2+c**2)

print(f"\n Raumdiagonale:       {Raumdiagonale}\n",
      f"Umfang:                 {Umfang}\n",
      f"Mantelfläche:           {Mantelfl}\n",
      f"Oberfläche:             {Oberfl}\n",
      f"Volumen:                {Volumen}\n",
      f"Länge aller Seiten:     {LenAllSides}\n",
      f"Flächendiagonale a-b:   {FlDiagAB}\n",
      f"Flächendiagonale b-c:   {FlDiagBC}\n",
      f"Flächendiagonale a-c:   {FlDiagAC}\n")  


