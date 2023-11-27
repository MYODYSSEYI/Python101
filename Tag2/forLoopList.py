listTeilnehmer = ["Oliver", "Kevin", "Chipi", "Kusai", "Bianca", "QiQi", "Harun", "Stefan", "Luca", "Dominik"]

for z in listTeilnehmer:
    print(z)
print("\n")

listTeilnehmer.append("Gerald")
for z in listTeilnehmer:
    print(z)
print("\n")

listTeilnehmer.remove(listTeilnehmer[2])
for z in listTeilnehmer:
    print(z)
print("\n")

listTeilnehmer.insert(0, "Simon")
for z in listTeilnehmer:
    print(z)
print("\n")

listTeilnehmer.sort()
for z in listTeilnehmer:
    print(z)
print("\n")

listTeilnehmer.sort(reverse=True)
for z in listTeilnehmer:
    print(z)
print("\n")