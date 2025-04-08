import random
import os
from art import logo
def dealcards_deck():
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(deck)
    return card

def calculate_score(deck):
    if sum(deck) == 21 and len(deck) == 2:
        return 0
    if 11 in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)
    return sum(deck)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "DRAW :)"
    elif user_score == 0:
        return "You got BLACKJACK dude ;)"
    elif computer_score == 0:
        return "Computer got BLACKJACK :("
    elif user_score > 21:
        return "You went over :("
    elif computer_score > 21:
        return "Computer went over :)"
    elif user_score > computer_score:
        return "You Win :)"
    else:
        return "You Lose :("

def gamerules():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game = False
    for _ in range(2):
        user_cards.append(dealcards_deck())
        computer_cards.append(dealcards_deck())
    while not game:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"{user_cards} = {user_score}")
        print(f"Computer first card is : {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game = True
        else:
            new_card = input("Do you wanna get another card? yes/no\n").lower()
            if new_card == "yes":
                user_cards.append(dealcards_deck())
            elif new_card == "no":
                game = True
            else:
                print("Invalid input")
                game = False
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(dealcards_deck())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand is : {user_cards}, Total score : {user_score}")
    print(f"Computer's final hand is :{computer_cards}, Total score : {computer_score}")
    print(compare(user_score, computer_score))

gamerules()

while input("Do you wanna play again ? yes/no\n").lower() == "yes":
    os.system("cls")
    gamerules()