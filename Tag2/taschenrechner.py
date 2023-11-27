# calculation with python 
# variables for calculations

varOK1 = "nicht ok"
varOK2 = "nicht ok"
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

while varOK1 == "nicht ok":    
    print("Wähle zwischen \n [+] Addition \n [-] Subtraktion \n [*] Multiplikation \n [/] Division \n [**] Potenz \n [%] Modulo \n [x] exit")

    if var_Rechnungsart != ["+", "-", "*", "/", "**", "%"]:
        print("Try again!")
        varOK1 = "nicht ok"
    else:
        varOK1 = "ok"

while varOK2 == "nicht ok":
    try: 
        var_a = float(input("a = "))
        var_b = float(input("b = "))
        varOK2 = "ok"

    except:
        print("Only numbers BOI!")
        varOK2 = "nicht ok"


    
    print(var_ergebnis)
    break