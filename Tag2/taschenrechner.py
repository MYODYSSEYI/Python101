# calculation with python 
# variables for calculations
while True:    
    print("Wähle zwischen \n [+] Addition \n [-] Subtraktion \n [*] Multiplikation \n [/] Division \n [**] Potenz \n [%] Modulo \n [x] exit")

    var_Rechnungsart = input("Ihre Auswahl: ") 
    if var_Rechnungsart == "x":
        print("Bye!")
        break
    elif var_Rechnungsart != ["+", "-", "*", "/", "**", "%"]:
        print("Try again!")
        continue
    
    try: 
        var_a = float(input("a = "))
        var_b = float(input("b = "))

    except:
        print("Only numbers BOI!")
        continue

    # if statements 
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
        
    print(var_ergebnis)
    break