import random
import os
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def blackjack():
    start=input("Are you ready to play ? yes/no\n").lower()
    if start=="yes":
        user_cards=random.choices(deck,k=2)
        computer_cards = random.choices(deck,k=2)
        user_sum=user_cards[0]+user_cards[1]
        print(f"Your cards are: {user_cards} = {user_sum}\n")
        print(f"Computer's first card is : {computer_cards[0]}\n")
        situation=True
        while situation:
            choice = input("Do you want another card? yes/no\n").lower()
            if choice=="yes":
                i=random.choice(deck)
                user_sum+=i
                user_cards.append(i)
                print(f"Your cards are: {user_cards} = {user_sum}\n")
                if user_sum>21:
                    print("You Lose!")
                    situation=False
                elif user_sum<21:
                    situation=True
            elif choice=="no":
                computer_sum=computer_cards[0]+computer_cards[1]
                i = random.choice(deck)
                computer_sum += i
                computer_cards.append(i)
                print(f"Computer's final hand is: {computer_cards} = {computer_sum}")
                if computer_sum>=21 and computer_sum>user_sum:
                    print("You Lose!")
                    situation=False
                elif computer_sum==user_sum:
                    print("DRAW! No Lose No Gain")
                else:
                    print("You Win!")
                    situation=False
    play_again=input("Thank you for playing!"
          "Do you want to play again? yes/no\n")
    if play_again=="yes":
        os.system('cls')
        blackjack()


blackjack()