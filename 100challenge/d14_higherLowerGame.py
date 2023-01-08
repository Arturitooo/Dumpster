#d14_higherLowerGame

from d14_databaseForHLG import data, logo, vs
import random
from os import system
 
#counting score
#comparison
perfect = True

def higherLowerGame(noMistake):
    score = 0
    while noMistake == True:
        if score > 0:
            system('cls')
            print(logo)
            print(f"You're' right! Current score: {score}")
            if correctAnswer == 'b':
                celeb1 = celeb2
        elif score == 0:
            celeb1 = random.choice(data)
        print(f"Compare A: {celeb1['name']}, a {celeb1['description']}, from {celeb1['country']}.")
        print(vs)
        celeb2 = random.choice(data)
        while celeb1 == celeb2:
            celeb2 = random.choice(data)
        print(f"Against B: {celeb2['name']}, a {celeb2['description']}, from {celeb2['country']}.")
        print()
        answer = input("Who has more followers? Type 'a' or 'b': ").lower()

        if celeb1['follower_count'] > celeb2['follower_count']:
            correctAnswer = 'a'
        elif celeb1['follower_count'] < celeb2['follower_count']:
            correctAnswer = 'b'
        

        if answer == correctAnswer:
            score += 1
        else:
            system('cls')
            print(logo)
            print(f"Sorry, that's not the correct answer. Final score: {score}")
            noMistake = False
    return

print(logo)
higherLowerGame(perfect)