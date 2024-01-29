import random 

print('''
 ███╗   ██╗ ██╗   ██╗ ███╗   ███╗ ██████╗  ███████╗ ██████╗       ██████╗  ██╗   ██╗ ███████╗ ███████╗ ███████╗ ███████╗ ██████╗ 
 ████╗  ██║ ██║   ██║ ████╗ ████║ ██╔══██╗ ██╔════╝ ██╔══██╗     ██╔════╝  ██║   ██║ ██╔════╝ ██╔════╝ ██╔════╝ ██╔════╝ ██╔══██╗
 ██╔██╗ ██║ ██║   ██║ ██╔████╔██║ ██████╔╝ █████╗   ██████╔╝     ██║  ███╗ ██║   ██║ █████╗   ███████╗ ███████╗ █████╗   ██████╔╝
 ██║╚██╗██║ ██║   ██║ ██║╚██╔╝██║ ██╔══██╗ ██╔══╝   ██╔══██╗     ██║   ██║ ██║   ██║ ██╔══╝   ╚════██║ ╚════██║ ██╔══╝   ██╔══██╗
 ██║ ╚████║ ╚██████╔╝ ██║ ╚═╝ ██║ ██████╔╝ ███████╗ ██║  ██║     ╚██████╔╝ ╚██████╔╝ ███████╗ ███████║ ███████║ ███████╗ ██║  ██║
 ╚═╝  ╚═══╝  ╚═════╝  ╚═╝     ╚═╝ ╚═════╝  ╚══════╝ ╚═╝  ╚═╝      ╚═════╝   ╚═════╝  ╚══════╝ ╚══════╝ ╚══════╝ ╚══════╝ ╚═╝  ╚═╝

'''
)

# pre game config
start = int(input("Pick a number to start from: "))
to = int(input("Pick a number to end at: "))
tries = 1
number = random.randint(start, to)

# game
guess = int(input(f"Pick a number between {start} and {to}: "))
while guess != number:
    tries += 1
    if guess < start or guess > to:
        print(f"I said between {start} and {to}!")
    elif guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    guess = int(input("Try again: "))
    
print(f"\nYou got it! \nYou needed {tries} tries and the number was {number}.")
