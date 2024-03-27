import art
import game_data
import os
import random

score = 0

while True:
    print(f'''
    {art.logo}
    Guess higher or lower follower count from celebritys!
    ''')

    celebrity_a = random.randint(0, len(game_data.data)-1)
    celebrity_b = random.randint(0, len(game_data.data)-1)

    if celebrity_a == celebrity_b:
        celebrity_b = random.randint(range(0, len(game_data.data)-1))

    print(f"Your current score is: {score}")

    guess = input(f'''
    A: {game_data.data[celebrity_a]['name']}
          {art.vs}
    B: {game_data.data[celebrity_b]['name']}
    ''').lower()
    
    if guess.lower() == 'a':
        if game_data.data[celebrity_a]['follower_count'] > game_data.data[celebrity_b]['follower_count']:
            print('You win!')
            score += 1
        else:
            print('You lose!')
            break
    elif guess.lower() == 'b':
        if game_data.data[celebrity_b]['follower_count'] > game_data.data[celebrity_a]['follower_count']:
            print('You win!')
            score += 1
        else:
            print('You lose!')
            break 
    else:
        print('Wrong input!')
        input = input('another round? (y/n)').lower()
        if input == 'y':
            os.system('clear')
        else:
            break

    

 
