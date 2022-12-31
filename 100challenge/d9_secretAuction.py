#d9_secret auction

from os import system

more_bidders = True
bidders_list = {}

#harder solution here
#def top_bid():
#    tb_name = ''
#    tb_value = 0
#    top_bidder = {tb_name:tb_value}
#    for bidder in bidders_list:
#        if bidders_list[bidder] > top_bidder[tb_name]:
#            tb_name = bidder
#            top_bidder[tb_name] = bidders_list[bidder]
#            
#    last_key = list(top_bidder)[-1]
#    print(last_key)
#    print("The winner is:", last_key, "who decided to bid: $",top_bidder[last_key])

#simpler solution here
def top_bid():
    tb_value = 0
    tb_name = ''
    for bidder in bidders_list:
        if bidders_list[bidder] > tb_value:
            tb_value = bidders_list[bidder]
            tb_name = bidder
    print(f"The winner is: {tb_name} who decided to bid: ${tb_value}")

#    print("The winner is:", temp_bidder[-2], "with a bid of: $",temp_bidder[-1])
            

#in that loop we're asking for details of bid, bidder name, adding to dictionary and checking which one is biggest

while more_bidders == True:
    print("Welcome to the secret auction program.")
    name = input("What is your name?: ").title()
    bid = int(input("What's your bid?: $"))
    bidders_list[name] = bid
    bidders = input("Are there any other bidders? Type 'yes' or 'no'?: ").lower()
    if bidders == "no":
        more_bidders = False
    system('cls')

top_bid()
