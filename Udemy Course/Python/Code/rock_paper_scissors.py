import random 
import time

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
outcome = 'Ongoing'

listRPS=[rock,paper,scissors]
computerChoice = random.randint(0,2)
playerChoice = int(input("Let's play a game of Rock, Paper, Scissors\nChoose wisely \n0 for Rock \n1 for Paper \n2 for Scissors \nYour battel beginns now!"))

print(f'The maschine chose...\n{listRPS[computerChoice]}')

if playerChoice == 0:
    print(f'Your chose...\n{rock}')
    if computerChoice == 0:
        outcome = 'Tie'
        print('Come again!')
    elif computerChoice == 1:
        outcome = 'Lose'
        print('The mighty maschine has won!')
    else:
        outcome = 'Win'
        print('Your Fate is sealed the maschines will never forgive YOU!!!')
elif playerChoice == 1:
    print(f'Your chose...\n{paper}')
    if computerChoice == 1:
        outcome = 'Tie'
        print('Come again!')
    elif computerChoice == 2:
        outcome = 'Lose'
        print('The mighty maschine has won!')
    else:
        outcome = 'Win'
        print('Your Fate is sealed the maschines will never forgive YOU!!!')
elif playerChoice == 2:
    print(f'Your chose...\n{scissors}')
    if computerChoice == 2:
        outcome = 'Tie'
        print('Come again!')
    elif computerChoice == 0:
        outcome = 'Lose'
        print('The mighty maschine has won!')
    else:
        outcome = 'Win'
        print('Your Fate is sealed the maschines will never forgive YOU!!!')

