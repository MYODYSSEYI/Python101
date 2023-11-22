# calculation with python 
# variables for calculations 
print("Wähle zwischen \n [+] Addition \n [-] Subtraktion \n [*] Multiplikation \n [/] Division \n [**] Potenz \n [%] Modulo \n [x] exit")

var_Rechnungsart = input("Ihre Auswahl: ") 
if var_Rechnungsart == "x":
    print("Bye!")
    exit()

elif var_Rechnungsart != "+" and  var_Rechnungsart != "-" and var_Rechnungsart != "*" and var_Rechnungsart != "/" and var_Rechnungsart != "**" and var_Rechnungsart != "%":
    print("Try again!")
    exit()

try: 
    var_a = float(input("a = "))
except:
    print("Only numbers BOI!")
    exit()
try:
    var_b = float(input("b = "))
except:
    print("Only numbers BOI!")
    exit()
try:
    var_c = float(input("c = "))
except var_c != type(float):
    print("Numbers only!")
    exit()

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