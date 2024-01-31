import random 

print('''
Welcome to the number guessing game!
Im thinking of a number between 1 and 100.''')

def game():
    def again():
        again = input('You want another go? (y/n): ')

        if again != 'n':
            game()
        else:
            quit()

    def chooseDifficulty():
        difficulty = input('Choose a difficulty easy or hard (e/h): ')
        if difficulty.lower() == 'e':
            tries = 10 
            return tries
        else:
            tries = 5
            return tries

    def chooseNumber():
        num = random.randint(1, 100)
        return num

    tries = chooseDifficulty() - 1
    num = chooseNumber()

    guess = int(input('Make a guess: '))
    
    while tries != 1:
        if guess == num:
            print(f'You where right the number was {num}')
            again()
        elif guess < 1 or guess > 100:
            print('Between 1 and 100 my friend')
        elif guess > num:
            print('Too high')
        elif guess < num:
            print('Too low')
            
        guess = int(input(f'Try again you got {tries} more tries'))
        
        tries -= 1

    if guess != num:
        print(f'The answer was {num}, better luck next time.')
    else:
        print(f'You where right the number was {num}')

    again()
game()
