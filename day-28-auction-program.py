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
bidding_data = []

def add_new_bidder(bidder_name, bid_amount):
    # first create an empty dictionary
    new_bidder = {}
    # secondly, assign the key with the function parameters
    new_bidder["name"] = bidder_name
    new_bidder["bid"] = bid_amount
    # finally, to add an item to an existing list, we can use append()
    bidding_data.append(new_bidder)

name = input("What is your name?: ")
amount = int(input("What's your bid?: $"))

add_new_bidder(bidder_name=name, bid_amount=amount)

print(bidding_data)
# print(bidding_data["bid"])