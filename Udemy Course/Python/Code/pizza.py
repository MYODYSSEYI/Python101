print("Thank you for choosing Python Pizza Deliveries!\nSizes: S, M, L\nIf you want extras type Y for yes and N for no.\n")
size = input('What size?\n') # What size pizza do you want? S, M, or L
add_pepperoni = input('You want pepperoni?\n') # Do you want pepperoni? Y or N
extra_cheese = input('Some extra cheese?\n') # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
if size == 'S':
  size = 15
  if add_pepperoni == 'Y':
    add_pepperoni = 2
  else:
    add_pepperoni = 0
if size == 'M':
  size = 20
  if add_pepperoni == 'Y':
    add_pepperoni = 3
  else:
    add_pepperoni = 0
if size == 'L':
  size = 25
  if add_pepperoni == 'Y':
    add_pepperoni = 3
  else:
    add_pepperoni = 0
if extra_cheese == 'Y':
  extra_cheese = 1
else:
  extra_cheese = 0

pizza = size + add_pepperoni + extra_cheese

print(f"Your final bill is: ${pizza}")