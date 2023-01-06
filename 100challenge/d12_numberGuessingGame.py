#d12_numberGuessingGame

from random import randint
from os import system

theNumber = randint(1,100)

def numberOfAttempts():
    #Functions asks for difficulty and using it - provides number of attempts    
    nrOfAttempts =0
    while nrOfAttempts == 0:
        diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        system('cls')
        if diff == 'easy':
            nrOfAttempts = 10
        elif diff == 'hard':
            nrOfAttempts = 5
        else:
            print("You provided wrong value, please type the good one!\n")
    return nrOfAttempts

def guess_number(lives):
    #The function asks user to input number and response if it's good or not, also presents final results like You won, you lost etc.
    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if guess == theNumber:
            #compares guess to answer and reponse to the user if the answer is good (won the game) or bad (decreasing number of attempts)
            print(f"Congratulations, {guess} is the number! You won the game!")
            break
        else:
            lives -= 1
            if guess > theNumber:
                print(f"{guess} it too high \nGuess again!")
            elif guess < theNumber:
                print(f"{guess} it too low \nGuess again!")
        if lives == 0:
            #1 way of loosing

            print("Sorry, you're out of attempts so the game is done. You lost!")
    return


print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100""")

guess_number(numberOfAttempts())