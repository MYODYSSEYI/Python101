zahl = int(input("Gib eine Zahl ein: "))
zahl2 = int(input("Gib eine Zahl ein: "))
rest = zahl % zahl2 

if rest == 0:
    print(f"{zahl} is devisible by {zahl2}")
else:
    print(f"{zahl} is not devisible by {zahl2}")
