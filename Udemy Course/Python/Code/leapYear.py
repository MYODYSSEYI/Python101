
# Which year do you want to check?
#year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# MINE :(
#if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
#  print("Leap year")
#elif year % 4 != 0: 
#    print("No leap year")
#elif year 

# SENSAI

year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")

'''
NIKITA VERSION

if year % 4 == 0:
	if year % 4 + year % 100 == 0:
			print("Not leap year")
	elif year % 100:
			print ("Leap year")
else:
	print("Not leap year")
'''