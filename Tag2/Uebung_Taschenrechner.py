print("Bitte wählen Sie aus: \n [+] Addition \n [-] Subtraktion) \n [*] Multiplikation \n [/] Division \n [**] Potenz \n [%] Modulo \n")


var_pruef_Rechnungsart = "nicht ok"
var_pruef_Eingabe = "nicht ok"

# Rechnungsart auswählen
while var_pruef_Rechnungsart == "nicht ok":
    var_Rechnungsart = input("Bitte wähle deine Rechnungsart aus: \n")
    if var_Rechnungsart != "+" and var_Rechnungsart != "-" and var_Rechnungsart != "*"  and var_Rechnungsart != "/" and var_Rechnungsart != "**" and var_Rechnungsart != "%":
        print("Falsche Eingabe! \n")
        var_pruef_Rechnungsart = "nicht ok"
    else:
        var_pruef_Rechnungsart = "ok"

# Werte eingeben
while var_pruef_Eingabe == "nicht ok":
    try:
        var_a = float(input("a="))
        var_b = float(input("b="))
        var_pruef_Eingabe = "ok"
    except:
        print("Die Eingabe muss eine Zahl sein \nBitte neu starten")
        

if var_Rechnungsart == "+":
    var_ergebnis = var_a + var_b
elif var_Rechnungsart == "-":
    var_ergebnis = var_a - var_b
elif var_Rechnungsart == "*":
    var_ergebnis = var_a * var_b
elif var_Rechnungsart == "/":
    var_ergebnis = var_a / var_b
elif var_Rechnungsart == "**":
    var_ergebnis = var_a ** var_b
elif var_Rechnungsart == "%":
    var_ergebnis = var_a % var_b
else:
    print("Falsche Eingabe! \n Bitte starten Sie das Programm neu.")
    exit()
    
print("Das Ergebnis ist:", var_ergebnis)
