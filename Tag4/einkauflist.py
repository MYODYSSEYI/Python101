

listEinkauf = []

with open('einkaufsliste.txt', 'r') as file:
    for line in file:
        listEinkauf.append(line.strip())

def fMenue():
    vAuswahl = input("""
Liste anzeigen      [a]
Eintrag löschen     [l]
Eintrag hinzufügen  [h]
Liste clearen       [c]
: """).lower()
    return(vAuswahl)
def fListeAnzeigen():
    for e in listEinkauf:
        print(e)
def fEintragLöschen():
    for e in listEinkauf:
        print(e)
    listEinkauf.remove(input("Was soll entfernt werden? "))
    fListeAnzeigen()
def fEintragEinfugen():
    for e in listEinkauf:
        print(e)
    listEinkauf.append(input("Was soll hinzu gefügt werden? "))
    fListeAnzeigen()
def fListClear():
    listEinkauf.clear()
    fListeAnzeigen()
    print("\nListe ist gecleared.")

while True:
    vAuswahl = fMenue()

    if vAuswahl == "a":
        fListeAnzeigen()
    elif vAuswahl == "l":
        fEintragLöschen() 
    elif vAuswahl == "h":
        fEintragEinfugen()
    elif vAuswahl == "c":
        fListClear()
    else:
        print("Wrong Button!")
    cont = input("Noch etwas? \n[Y]|[N]").upper()
    if cont == "Y":
        continue
    else:
        break

formatedList = '\n'.join(listEinkauf)

with open('einkaufsliste.txt', 'w') as file:
    file.write(formatedList)


