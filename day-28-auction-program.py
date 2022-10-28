# 95. The Secret Auction Program Instructions and Flow Chart
# Coded on 25.10.2022

from day28AuctionProgramArt import logo
from os import system

# print out the logo art at the start of the code
print(logo)

#HINT: You can clear the output in the console using below:
# system('cls')

# define a variable to store a dictionary that consist of the key: value pairs below:
# bidders = {
# "name": name,
# "bid": bid,
# }

# bidders = {
# "name": "James",
# "bid": "$123",
# },

# first create an empty dictionary in list
# bidding_data = []
bids = {}
bidding_finish = False

# def add_new_bidder(bidder_name, bid_amount):
#     # first create an empty dictionary
#     new_bidder = {}
#     # secondly, assign the key with the function parameters
#     new_bidder["name"] = bidder_name
#     new_bidder["bid"] = bid_amount
#     # finally, to add an item to an existing list, we can use append()
#     bidding_data.append(new_bidder)

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finish:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    # add_new_bidder(bidder_name=name, bid_amount=amount)
    bid_continue = input("Are there any other bidders? Type 'yes' or 'no':\n")
    # if no, exit the loop and determine the winner
    if bid_continue == "no": 
        bidding_finish = True
        find_highest_bidder(bids)
    # if yes, clear the screen and repeat
    elif bid_continue == "yes":
        system('cls')  