# benutzer soll seinen namen sagen
# benutzer soll sein alter eingeben
# ist der benutzer älter als 40, soll er um sein Lieblingstier gefragt werden
# ist der benutzer jünger als 40, soll er um seinen Lieblingsfilm gefragt werden
# ausgegeben werden soll am ende: "Der Nutzer is x Jahre alt, sein Lieblingsfilm/tier ist x."
while True:
    varName = input("Was ist dein name? \n")
    varAlter = int(input("Wie alt bist du? \n"))
    if varAlter >= 40:
        varLT = input("Was ist dein Lieblingstier? \n")
        print(f"Dein Name ist {varName} du bist {varAlter} Jahre alt und dein Lieblingstier ist {varLT}, ist das korrekt?")
        varCorrect = input("[Y]|[N]\n")
    else:
        varLF = input("Was ist dein Lieblingsfilm? \n")
        print(f"Dein Name ist {varName} du bist {varAlter} Jahre alt und dein Lieblingsfilm ist {varLF}, ist das korrekt?")
        varCorrect = input("[Y]|[N]\n")
    if varCorrect == "Y" or "y":
        print(f"Es war schön dich kennengelernt zu haben.\nMan sieht sich, ciao {varName}.")
        break
    else:
        continue