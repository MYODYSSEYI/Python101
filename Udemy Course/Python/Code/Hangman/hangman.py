import os
import random
import time
from hangmanAssets import logo, stages
import hangman_words
word_list = hangman_words.word_list

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
while True:
    chosen_word = random.choice(word_list)
    word_len=len(chosen_word)

    used_letters = []
    display=[]
    for i in range(word_len):
        display += '_'

    given = ''
    for i in display:
        given += i + ' '


    print(logo)
    time.sleep(1)

    rounds = 1
    print(f"{given}\n")
    while display.count('_') != 0: #and rounds != 8:

        if rounds == 7:
            print(f'your word was... \n\n{chosen_word}\n')
            break
        guess=input('\nchoose a letter: ').lower()
        os.system("cls" if os.name == "nt" else "clear")
        for i in range(word_len):
            letter = chosen_word[i]
            if guess == letter:
                display[i] = letter
        answer = ''
        for letter in display:
            answer += letter + " "

        display_used=''
#
        if'_'not in display:
            print(stages[len(stages)-rounds])
            for letter in used_letters:
                display_used += letter
            print(f'Used letter: {display_used}')
            print(f'\nThe word was: {answer}\nYou win!')
            if guess not in used_letters:
                used_letters.append(guess)
# Adds one to rounds if guess is wrong
        elif used_letters.count(guess) == 0:
            if display.count(guess) == 0:
                rounds += 1
                if guess not in used_letters:
                    used_letters.append(guess)

            print(stages[len(stages)-rounds])
            for letter in used_letters:
                display_used += letter
            print(f'Used letter: {display_used}')
            print(f"\n{answer}")
# Displays stage of hangman and the letters u got so far
        else:
            print(stages[len(stages)-rounds])
            for letter in used_letters:
                display_used += letter
            print(f'Used letter: {display_used}')
            print(f"\n{answer}")
            if guess not in used_letters:
                used_letters.append(guess)


    play_again = input('Do you want to try another word?\n[Y]|[N]\n').upper()
    if play_again == 'Y':

        continue
    else:
        break


