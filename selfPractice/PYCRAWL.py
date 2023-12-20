print('''

 ██▓███ ▓██   ██▓ ▄████▄   ██▀███   ▄▄▄       █     █░ ██▓
▓██░  ██▒▒██  ██▒▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▓█░ █ ░█░▓██▒
▓██░ ██▓▒ ▒██ ██░▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒█░ █ ░█ ▒██░
▒██▄█▓▒ ▒ ░ ▐██▓░▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ░█░ █ ░█ ▒██░
▒██▒ ░  ░ ░ ██▒▓░▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒░░██▒██▓ ░██████▒
▒▓▒░ ░  ░  ██▒▒▒ ░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▓░▒ ▒  ░ ▒░▓  ░
░▒ ░     ▓██ ░▒░   ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ▒ ░ ░  ░ ░ ▒  ░
░░       ▒ ▒ ░░  ░          ░░   ░   ░   ▒     ░   ░    ░ ░
         ░ ░     ░ ░         ░           ░  ░    ░        ░  ░
         ░ ░     ░

''')

import time

Name = input("Please enter your name if you wish to start this Adventure.\n> ")

print() # Move to next line

text = f"""
This is the story of a Warrior named {Name} not much is known about him, since he was not born into this world by usual means.
He who died long before our mysterious adventure unfolds was reborn into this world 
"""

for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)  # Adjust the sleep duration (in seconds) for your preferred speed

print()  # Move to the next line after printing
