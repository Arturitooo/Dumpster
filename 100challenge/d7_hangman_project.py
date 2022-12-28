#d7_hangman project

import random
import os
clear = lambda: os.system('cls')

stages = {7: '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', 6: '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', 5:'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', 4:'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 3:'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', 2: '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', 1: '''
  +---+
  |   |
      |
      |
      |
      |
=========
''', 0: '''
  +---+
      |
      |
      |
      |
      |
=========
'''}

word_list = ["jeden", "dwa", "trzy"]
chosen_word = random.choice(word_list)
display = [] 
deaths = 0

for i in range(len(chosen_word)):
    display.append("_")


print(chosen_word)

while "_" in display and deaths<7 :
    clear()
    print(stages[deaths])
    print("You have", 7-deaths ,"lives left")
    print(display)
    guess = input("Gues a letter: ").lower()
 

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = guess

    if guess not in chosen_word:
        deaths += 1   


if deaths > 6:
    clear()
    print(stages[deaths])
    print("Unfortunately, you lost :'(")

else:
    clear()
    print("Congratulations, you won")
    print("The word is:", chosen_word)