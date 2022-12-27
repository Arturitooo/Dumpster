#random module and how to use it

import random

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

choice = {0:rock, 1:paper, 2:scissors}
wantToPlay = True

while wantToPlay == True:
    numberIsOkay = False
    while numberIsOkay == False:
        userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
        if -1 < userChoice < 3:
            numberIsOkay = True 
        else:
            print("You put a wrong number")
            numberIsOkay = False

    botChoice = random.randint(0,2)
    print("Your choice")
    print(choice[userChoice])
    print("Computer choice")
    print(choice[botChoice])
    print("RESULT:")

    if userChoice == 0:
        if botChoice == 0:
            print('its a draw')
        elif botChoice == 1:
            print('you lost :(')
        else:
            print('Congratulations, you won!')
    elif userChoice == 1:
        if botChoice == 0:
            print('Congratulations, you won!')
        elif botChoice == 1:
            print("it's a draw")
        else:
            print('You lost :(')
    elif userChoice == 2:
        if botChoice == 0:
            print('You lost :(')
        elif botChoice == 1:
            print('Congratulations, you won!')
        else:
            print('its a draw')
    print()

    answer = True

    while answer == True:
        stillWantToPlay = input('Do you still want to play? type "y" if yes and type "n" if no. ').lower()
        if stillWantToPlay == "n":
            print('You decided to quit the game. Bye bye!')
            wantToPlay = False
            answer = False
        elif stillWantToPlay == 'y':
            print('You decided to continue the game. Good luck! ')
            print()
            wantToPlay = True
            answer = False
        else:
            print("Put correct value! ")
    