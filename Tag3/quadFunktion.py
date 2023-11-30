import math

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

v_Auswahl = 0

while v_Auswahl != " ":    
    print("Was möchtest du berechnen?\nQuader:\n")
    v_Auswahl = input("Raumdiagonale     [e]\n" + "Umfang            [u]\n" + "Grundfläche       [G]\n" + "Mantelfläche      [M]\n" + "Abbrechen       [Leertaste]\n")

    if v_Auswahl == "e" or v_Auswahl == "E":
        a = int(0)
        b = int(0)
        c = int(0)
        while a != float and b != float and c != float:
            try:
                a = float(input('Gib einen Wert für "a" an.\n'))
                b = float(input('Gib einen Wert für "b" an.\n'))
                c = float(input('Gib einen Wert für "c" an.\n'))
                f_Raum(a, b, c)
                break
            except:
                print("Numbers only!")
                continue
        vContinue = input("Noch eine Rechnung? [Y]|[N]")
        if vContinue == "y" or vContinue == "Y":
            continue
        else:
            break
    elif v_Auswahl == "u" or v_Auswahl == "U":
        a = int(0)
        b = int(0)
        while a != float and b != float:
            try:
                a = float(input('Gib einen Wert für "a" an.\n'))
                b = float(input('Gib einen Wert für "b" an.\n'))
                f_Auswahl(a, b)
                break
            except:
                print("Numbers only!")
                continue
        vContinue = input("Noch eine Rechnung? [Y]|[N]")
        if vContinue == "y" or vContinue == "Y":
            continue
        else:
            break
    elif v_Auswahl == "G" or v_Auswahl == "g":
        a = int(0)
        b = int(0)
        while a != float and b != float:
            try:
                a = float(input('Gib einen Wert für "a" an.\n'))
                b = float(input('Gib einen Wert für "b" an.\n'))
                f_Grundfl(a, b)
                break
            except:
                print("Numbers only!")
                continue
        vContinue = input("Noch eine Rechnung? [Y]|[N]")
        if vContinue == "y" or vContinue == "Y":
            continue
        else:
            break
    elif v_Auswahl == "M" or v_Auswahl == "m":
        a = int(0)
        b = int(0)
        c = int(0)
        while a != float and b != float and c != float:
            try:
                a = float(input('Gib einen Wert für "a" an.\n'))
                b = float(input('Gib einen Wert für "b" an.\n'))
                c = float(input('Gib einen Wert für "c" an.\n'))
                f_Mantelfl(a, b, c)
                break
            except:
                print("Numbers only!")
                continue
        vContinue = input("Noch eine Rechnung? [Y]|[N]")
        if vContinue == "y" or vContinue == "Y":
            continue
        else:
            break
    elif v_Auswahl == " ":
        print("Good bye!")
    else:
        print("Wrong choice!\n")
        continue
