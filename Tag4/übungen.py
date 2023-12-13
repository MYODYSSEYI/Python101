#  # Fügen Sie oberhalb beider print Anweisungen einen kommentar mit dem aktuellen Datum im Format TT.MM.JJ ein.
# wort1 = "Guten"
# wort2 = "Tag"
# wort3 = "Allerseits"
#  
# # 13.12.23
# print ((wort1, wort2, wort3))
# gruss = wort1 + " " + wort2 + " " +wort3
# print(gruss)
#
# ''Fügen Sie im angezeigten Programm eine Fliesskomma Variable f ein. weisen Sie Ihr den Anfangswert 42 zu.
# '''
# # Deklariert eine variable f als Gleitkommazahl und weist ihr den Anfangswert 42 zu.
# f = 42.0
#  
# # Ausgabe der Variable f
# print (f)


# '''Ergänzen Sie das angezeigte Programm so, dass ein Nutzer zwei Zahlen eingeben muss.
# Dann soll das Programm die gesamte Rechnung mit dem Produkt p ausgeben.
# Beispiel zur Ausgabe: 5 * 7 = 35
# '''
# # Programm liest zwei Zahlen ein und multipliziert diese.
# # Ausgabe der gesamten Rechnung mit beiden Multiplikanden und dem Produkt p am Schluss.
# # Eingabe der zwei Zahlen
# zahl1 = float(input("a: "))
# zahl2 = float(input("b: "))
# p = zahl1 * zahl2
# # Einfügen der Ausgabeanweisung zur Darstellung der gesamten Rechnung.
# print(zahl1, '*', zahl2, '=', p)

# '''Verbrennungsmotoren in Autos arbeiten am besten , wenn sich die Betriebstemperatur in einem Bereich von 80 bis 120 Grad Celcius befin
# det - Grenzwerte inklusive.
# Ergänzen Sie das angezeigte Programm mit dem Boolschen Ausdruck der True (wahr) liefert, wenn die Temperatur in der numerischen Varia
# ble temp innerhalb des genannten Temperaturbereichs liegt.
# '''
# # Programm fragt nach der Betriebstemperatur und bestimmt ob die Temperatur im optimalen Bereich liegt.
# temp=int(input("Betriebstemperatur"))
# if temp >=80 and temp <= 120:
#     temp = True
# else:
#     temp = False
#
# print(temp)
# # Passenden Boolschen Ausdruck in der if Anweisung eintragen.


# '''Benutzen Sie die Zähklervariable z in einer Schleife, um eine Zeichenkette "sterne" mit einer variablen Anzahl Sternen n zu generiere
# n und zu drucken.
# '''
# # Liest die Anzahl Sterne als Variable n ein - Füllt String Variable "sterne"
# # mit der eingegebenen Anzahl Sterne unter Verwendung der Zählervariable z.
# n = int(input("Anzahl Sterne eingeben: "))
# sterne = ""
# # Schleife mit dem Zähler eintragen
# for i in range(1,n+1):
#     sterne += "*"
# # Ausdruck des Strings mit den Sternen
# print(sterne)

# '''Fügen Sie eine mehrzeilige Mehrweganweisung (if ... else) ein.
# Diese soll feststellen, ob die eingegebene Tagestemperatur t über oder gleich 25 Grad ist.
# Flass erfüllt, muss "Getränkeflasche einpacken!" ausgegeben werden, falls nicht "Keine Getränke notwendig."
# '''
# # Programm druckt zwei alternative Empfehlungen, je nach eingegebener
# # Temperatur, ob grösser/ gleich oder kleiner 25 Grad Celsius.
# # Einlesen der Temperatur
# t = int(input("Bitte Temperatur eingeben:"))
# #
# # if t >= 25:
# #     print("Getränkeflasche einpacken!")
# # else:
# #     print("Keine Getränke notwendig!")
# #
#
# '''Schreiben SIe eine Python Funktion paarungen(n). Diese beinhaltet die Formel p=n*(n-1)/2 und übernimmt n als Parameter.
# # Rufen Sie diese Funktion anschliessend in der print-Anweisung auf.
# # Achten Sie darauf, dass das Resultat als ganzzahliger Wert aus der Funktion zurückgegeben wird.
# # '''
# # # Programm berechnet die Anzahl der möglichen verschiedenen Paarungen von n Elementen
# # # als p=int(n*(n-1)/2)
# # # Liest die Anzahl Elemente ein
# # n = int(input("Anzahl Elemente eingeben: "))
# # # Definition einer Funktion paarungen(n) zur Bestimmung der Anzahl an Paarungen mit der
# # # gennanten Formel
# # def paarungen(n):
# #     p=n*(n-1)/2
# #     return(p)
# # # Ausdruck mit Aufruf der Funktion zur Berechnung von paarungen(n).
# # print("Die Anzahl Paarungen von ",n,"Elementen ist:", paarungen(n))
#
# # ''' Ergänzen Sie das angezeigte Programm so, dass es mit Hilfe eienr Funktion der Python Bibliothek "time" das lokal aktuelle Datum und
# # die Uhrzeit formatiert ausgibt.
# # '''
# # # Programm druckt aktuelles Datum und Zeit mit Hilfe der Python Bibliothek "time"
# # # Deklaration der verwendung der Bibliotheksfunktionen
# # from time import localtime 
# # from time import strftime
# # # Print # Get the local time
# # local_time = localtime()
# #
# # # Format the time
# # formatted_time = strftime("%Y-%m-%d %H:%M:%S", local_time)
# #
# # print(formatted_time)
#
# '''Korrigieren Sie die fehlerhafte Programmlogik sowie die falsche Verwendung eines Datentypen im folgenden Programm
# Ein Reifendruck von weniger als 1.75 bar gilt als zu gering, ein Druck von mehr als 2 bar als zu hoch
# '''
# # Programm kontrolliert und beurteilt den Reifendruck: unter 1.75 als zu gering, ueber 2 als zu hoch
# # Eingabe des Reifendrucks
# reifen_druck = float(input("Reifendruck eingeben. "))
# # Ausgabe Beurteilung
# if reifen_druck < 1.75:
#     print("Der Reifendruck ist zu gering")
# elif reifen_druck <= 2.00:
#     print("Der Reifendruck ist richtig")
# hjlse:
#     print("Der Reifendruck ist zu hoch")
