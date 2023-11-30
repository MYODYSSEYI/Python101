
listEinkauf = ["Brot", "Wasser"]

def fMenue():
    vAuswahl = input("\nListe anzeigen [a]\nEintrag löschen [l]\nEintrag hinzufügen [h]\n: ")
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


while True:
    vAuswahl = fMenue()

    if vAuswahl == "a":
        fListeAnzeigen()
    elif vAuswahl == "l":
        fEintragLöschen() 
    elif vAuswahl == "h":
        fEintragEinfugen()
    else:
        print("Wrong Button!")

