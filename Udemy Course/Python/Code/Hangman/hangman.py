import os
import random
import time
from hangmanAssets import logo, stages
import hangman_words
word_list = hangman_words.word_list

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
word_len=len(chosen_word)


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
while display.count('_') != 0 and rounds != 7:
  guess=input('\nchoose a letter: ').lower()
  os.system("cls" if os.name == "nt" else "clear")
  for i in range(word_len):
    letter = chosen_word[i]
    if guess == letter:
      display[i] = letter
  answer = ''
  for letter in display:
    answer += letter + " "
#
  if'_'not in display:
    print(stages[len(stages)-rounds])
    print(f'\nThe word was: {answer}\nYou win!')

# Adds one to rounds if guess is wrong
  elif display.count(guess) == 0:
    rounds += 1
    print(stages[len(stages)-rounds])
    print(f"\n{answer}")

# Displays stage of hangman and the letters u got so far
  else:
    print(stages[len(stages)-rounds])
    print(f"\n{answer}")