import os

clear = lambda: os.system('cls')
bidders_available = True
bidders = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")

while bidders_available:
    bidder = input("What is your name?\n")
    bid_price = int(input("Your bid price? $"))
    bidders[bidder] = bid_price
    should_continue = input("Is there any other bidder available? Type \'yes\' or \'no\'.\n").lower()

    if should_continue == 'yes':
        clear()
    elif should_continue == 'no':
        bidders_available = False
        find_highest_bidder(bidding_record=bidders)
        
