import time
import os

varStop = "n"
varSeconds = int(input("Seconds: "))
varMinutes = int(input("Minutes: "))
varHours = int(input("Hours: "))


while varStop <= "n":
    os.system("cls" if os.name == "nt" else clear)
    print(f"{varHours}:{varMinutes}:{varSeconds}")
    print("\n")
    varSeconds -= 1
    time.sleep(1)
    if varSeconds == -1: 
        varSeconds = 59 
        varMinutes -= 1
    if varMinutes == -1:
        varMinutes = 59
        varHours -= 1
    if varHours ==0 and varMinutes == 0 and varSeconds == 0:
        time.sleep(1) 
        varStop = "stop"
        os.system("cls" if os.name == "nt" else clear)
        print(f"{varHours}:{varMinutes}:{varSeconds} \nFINISHED!")
        break

