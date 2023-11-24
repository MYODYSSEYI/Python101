while True:
    print("Wähle zwischen \n [+] Addition \n [-] Subtraktion \n [*] Multiplikation \n [/] Division \n [**] Potenz \n [%] Modulo \n [x] exit")
    var_Rechnungsart = input("Ihre Auswahl: ")
    if var_Rechnungsart == "x":
        print("Bye!")
        break
    elif var_Rechnungsart not in ["+", "-", "*", "/", "**", "%"]:
        print("Try again!")
        continue
    try:
        var_a = float(input("a = "))
        var_b = float(input("b = "))
        var_c = float(input("c = "))
    except ValueError:
        print("Only numbers BOI! Try again.")
        continue
    # if statements
    if var_Rechnungsart == "+":
        var_ergebnis = var_a + var_b + var_c

    elif var_Rechnungsart == "-":
        var_ergebnis = var_a - var_b - var_c

    elif var_Rechnungsart == "*":
        var_ergebnis = var_a * var_b * var_c

    elif var_Rechnungsart == "/":
        var_ergebnis = var_a / var_b / var_c

    elif var_Rechnungsart == "**":
        var_ergebnis = var_a ** var_b

    elif var_Rechnungsart == "%":
        var_ergebnis = var_a % var_b
        
        print(var_ergebnis)
        continue
