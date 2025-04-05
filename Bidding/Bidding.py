import art
import os
print(art.logo)
database={}
bidding=True
def find_highest(bidding_dictionary):
    highest=0
    winner=""
    for bidder in bidding_dictionary:
        bid_amount=bidding_dictionary[bidder]
        if bid_amount>=highest:
            highest=bid_amount
            winner=bidder
    print(f"The WINNER is {winner} with a bid of {highest}\n")
while bidding:
    user_name = input("Enter your name: ").lower()
    user_price= int(input("Enter the price you wanna bid: $"))
    people=input("Is anyone else wanna join ? : 'yes' or 'no' ").lower()
    database[user_name]=user_price
    if people == "yes":
        bidding=True
    else:
        bidding=False
        os.system('cls')
        print(art.logo)
        find_highest(database)