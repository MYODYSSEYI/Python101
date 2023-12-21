
import time
import runpy

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

""")

## Startequipment 
if playerClass == 'W':
    choice = input('choose your starting weapon [s] staff [b] for book')
    if choice == 's':
        playerEquiptment = 'staff'
    elif choice == 'b':
        playerEquiptment = 'book'
# elif playerClass == 'K':
#
# elif playerClass == 'T':
#
# elif playerClass == 'A':
#


## Gravegift
gravegift = 'potion'

## Name
playerName = input("Please enter your name if you wish to start this Adventure.\n> ")

print() # Move to next line

text = f"""
This is the story of a Warrior named {playerName} not much is known about him, since he was not born into this world by usual means.
He who died long before our mysterious adventure unfolds was sent back into this cruel world by the protective spirits of this world.
"""

# for char in text:
#     print(char, end='', flush=True)
#     time.sleep(0.05)  # Adjust the sleep duration (in seconds) for your preferred speed

print()  # Move to the next line after printing

## Safe player data 
playerData={}
playerData['playerClass'] = playerClass
playerData['playerEquiptment'] = [playerEquiptment, gravegift]

print(playerData)

## Go to next part of story 
# if playerClass == 'W':
#     runpy.run_path('Wizard.py')
# elif playerClass == 'K':
#     runpy.run_path('Knight.py')
# elif playerClass == 'T':
#     runpy.run_path('Thief.py')
# elif playerClass == 'A'
#     runpy.run_path('Assassin.py')