import random 
import os

while True:
    os.system("cls" if os.name == "nt" else "clear")
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
    if start > to:
        replace = start
        start = to
        to = replace

    tries = 1
    number = random.randint(start, to)

# game
    guess = int(input(f"Pick a number between {start} and {to}: "))
    while guess != number:
        os.system("cls" if os.name == "nt" else "clear")
        tries += 1
        if guess < start or guess > to:
            print(f"I said between {start} and {to}!")
        elif guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        guess = int(input("Try again: "))
        
    print(f"\nYou got it! \nYou needed {tries} tries and the number was {number}.")

    again = input("Would you like to play again? (y/n): ")

    if again.lower() != "y":
        break
    else:
        os.system("cls" if os.name == "nt" else "clear")
