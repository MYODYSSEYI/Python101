
import time
import runpy
import json


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


print("""

                                   ....
                                .'' .'''
.                             .'   :
\\\                          .:    :
 \\\                        _:    :       ..----.._
  \\\                    .:::.....:::.. .'         ''.
   \\\                 .'  #-. .-######'     #        '.
    \\\                 '.##'/ ' ################       :
     \\\                  #####################         :
      \\\               ..##.-.#### .''''###'.._        :
       \\\             :--:########:            '.    .' :
        \\\..__...--.. :--:#######.'   '.         '.     :
        :      :  : : '':'-:'':'::        .         '.  .'
        '--- '''..: :    ':    '..'''.      '.        :'
           \\\  :: : :     '      ''''''.     '.      .:
            \\\ ::  : :     '            '.      '      :
             \\\::   : :           ....' ..:       '     '.
              \\\::  : :    .....####\\ .~~.:.             :
               \\\':.:.:.:'#########.===. ~ |.'-.   . '''.. :
                \\\    .'  ########## \ \ _.' '. '-.       '''.
                :\\\  :     ########   \ \      '.  '-.        :
               :  \\\'    '   #### :    \ \      :.    '-.      :
              :  .'\\\   :'  :     :     \ \       :      '-.    :
             : .'  .\\\  '  :      :     :\ \       :        '.   :
             ::   :  \\\'  :.      :     : \ \      :          '. :
             ::. :    \\\  : :      :    ;  \ \     :           '.:
              : ':    '\\\ :  :     :     :  \:\     :        ..'
                 :    ' \\\ :        :     ;  \|      :   .'''
                 '.   '  \\\:                         :.''
                  .:..... \\\:       :            ..''
                 '._____|'.\\\......'''''''.:..'''
                            \\\
""")

# Character creation screen 
## class need to add ascii art 
playerClass = input("""
Pick your class 

Wizard      [W]
Knight      [K]
Thief       [T]
Assassin    [A]
Range       [R]
>""")

## Startequipment 
if playerClass == 'W':
    choice = input('choose your starting weapon [s] for staff [b] for book\n>')
    if choice == 's':
        playerEquiptment = 'staff'
    elif choice == 'b':
        playerEquiptment = 'book'
elif playerClass == 'K':
    choice = input('choose your starting weapon [s] for sword [m] for morningstar\n>')
    if choice == 's':
        playerEquiptment = 'sword'
    elif choice == 'm':
        playerEquiptment = 'morningstar'
elif playerClass == 'T':
    choice = input('choose your starting weapon [f] for falchion [d] for dagger\n>')
    if choice == 'f':
        playerEquiptment = 'falchion'
    elif choice == 'd':
        playerEquiptment = 'dagger'
elif playerClass == 'A':
    choice = input('choose your starting weapon [r] for rapier [c] for crossbow\n>')
    if choice == 'r':
        playerEquiptment = 'rapier'
    elif choice == 'c':
        playerEquiptment = 'crossbow'
elif playerClass == 'R':
    choice = input('choose your starting weapon [r] for recursive bow [l] for longbow\n>')
    if choice == 'r':
        playerEquiptment = 'recursiveBow'
    elif choice == 'l':
        playerEquiptment = 'longbow'



## Gravegift
choice = input("""
What have your long gone relatives left you for your afterlife?

mystery potion      [?]
bag of gold         [$]
good luck charm     [*]
>""")

if choice == '?':
    gravegift = 'mysteryPotion'
elif choice == '$':
    gravegift = 'bagOfGold'
elif choice == '*':
    gravegift = 'goodLuckCharm'

print()
## Name
playerName = input("Please enter your name if you wish to start this Adventure.\n> ")

print() # Move to next line

text = f"""
This is the story of a Warrior named {playerName} not much is known about him, since he was not born into this world by usual means.
He who died long before our mysterious adventure unfolds was sent back into this cruel world by the protective spirits of this world.
"""

for char in text:
    print(char, end='', flush=True)
    time.sleep(0.03)  # Adjust the sleep duration (in seconds) for your preferred speed

print()  # Move to the next line after printing

## Safe player data 
playerData={}
playerData['playerName'] = playerName
playerData['playerClass'] = playerClass
playerData['playerEquiptment'] = [playerEquiptment, gravegift]

with open("playerData.txt", "w") as file:
    json.dump(playerData, file)

print(playerData)

## Go to next part of story 
if playerClass == 'W':
    runpy.run_path('Wizard.py')
# elif playerClass == 'K':
#     runpy.run_path('Knight.py')
# elif playerClass == 'T':
#     runpy.run_path('Thief.py')
# elif playerClass == 'A'
#     runpy.run_path('Assassin.py')
