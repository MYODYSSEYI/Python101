import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("THIS WILL BE THE LAST PASSWORD U WILL EVER NEED!")
nrLetters = int(input("Select how many letters should be in ur masterfully crafed password?\n"))
nrNumbers = int(input("How many numbers should be in that mighty password of yours?\n"))
nrSymbols = int(input("And for the finishing touch might I ask you for the number of symbols you want in your tempel of security?\n"))

passwordList = []

for char in range(1, nrLetters +1):
    passwordList.append(random.choice(letters))
for nr in range(1, nrNumbers +1):
    passwordList.append(random.choice(numbers))
for sym in range(1, nrSymbols +1): 
    passwordList.append(random.choice(symbols))
    
random.shuffle(passwordList)

password = ""

for i in passwordList:
    password += i

print(password)

