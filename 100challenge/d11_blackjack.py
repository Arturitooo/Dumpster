#d11_blackjack_capstone_project

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from os import system
import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

finished = False
still_playing = 'y'


def resulter(score1, score2):        
    difference1 = 21 - score1
    difference2 = 21 - score2
    print("Your final hand:",player_cards,'final score:',player_score)
    print("Dealer final hand:",dealer_cards,'and his final score:',dealer_score)
    
    if score2 > 21:
        return("Congratulations, you won. The dealer exceed 21.\n")  
    elif score1 > 21 or difference1 > difference2:
        return("You lose ;(\n")
    elif difference1 == difference2:
        return("it's a draw\n")
    else:
        return("Congratulations, you won!\n")
        
def ace(card):
    if card == 11:
        ace_card = int(input("You got the ace! Do you want to count it as 1 or 11? "))
        player_cards[-1] = ace_card
    return player_cards


while finished == False:
    pick_card = 'y'
    player_cards = []
    dealer_cards = []
    still_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if still_playing == 'n':
        finished = True
        print("bye bye")
    else:
        system('cls')
        print(logo)
        player_cards.append(random.choice(cards))
        player_cards.append(random.choice(cards))
        ace(player_cards[-1])
        player_score = sum(player_cards)
        print("Your cards:",player_cards,'current score:',player_score)
        dealer_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
        dealer_score = sum(dealer_cards)     
        print("Dealer's first card:",dealer_cards[0])

        if player_score < 22:

            while player_score <22 and pick_card == "y":
                pick_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if pick_card == 'y':
                    system('cls')
                    print(logo)
                    player_cards.append(random.choice(cards))
                    if player_cards[-1] == 11:
                        ace(player_cards[-1])
                    player_score = sum(player_cards)
                    print("Your cards:",player_cards,'current score:',player_score)
                    print("Dealer's first card:",dealer_cards[0])
                    
        else:
            print("You exceed 21 points, you lost - dealer won the game!")

        while player_score < 22 and dealer_score < 17:
            dealer_cards.append(random.choice(cards))
            dealer_score = sum(dealer_cards)
        
        system('cls')
        print(resulter(player_score, dealer_score))