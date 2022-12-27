#this is day 4 of 100 days bootcamp with Python

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print('''Welcome to Treasure Island
Your mission is to find the reasure
"''')

direction1 = input("You're at a cross road. Where do you want to go? Type "+'"left" or "right ').lower()

if direction1 == "left":
    direction2 = input('You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across ').lower()
    if direction2 == "wait":
        direction3 = input("You arrive at the island unharmed, There is a house with 3 doors. One red, one yelllow and one blue. Which colour do you choose? ").lower()
        if direction3 == "yellow":
            print("Congratulations, you won the game!")
        else:        
            print("You enter a room of a beasts. Game over")
    else:        
        print("You drowned and died, game over")
else:        
    print("You etook the wrong direction. Game over")
