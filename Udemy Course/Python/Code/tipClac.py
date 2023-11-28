#If the bill was $150.00, split between 5 people, with 12% tip. 
bill = input("What did u pay? \n")
persons = input("How many are you? \n")
tip = input("How much do u wanna tip? \n")
tipNew = float(tip)/100+1

THE_TIP = float(bill)/float(persons)*tipNew

print(f"%.2f"%THE_TIP)
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇