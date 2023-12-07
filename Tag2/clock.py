import time
import os

varStop = "n"
varSeconds = 0
varMinutes = 0
varHours = 0


while varStop <= "n":
    os.system("cls" if os.name == "nt" else clear)
    print(f"{varHours}:{varMinutes}:{varSeconds}")
    print("\n")
    varSeconds += 1
    time.sleep(1)
    if varSeconds == 60:
        varSeconds = 0
        varMinutes += 1
    if varMinutes == 60:
        varMinutes = 0
        varHours += 1
    if varHours == 24:
        varHours = 0
    ##varStop = input("uhr anhalten?\n [y]|[n]: ")
