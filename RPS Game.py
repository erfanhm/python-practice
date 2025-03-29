import random
print("Welcome to the Rock,Paper,Scissors game")
user_choice=int(input("Are you ready to play? choose 0for ROCK, 1for PAPER, 2for SCISSORS : "))
Game=['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''','''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''','''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
computer_choice=random.randint(0,2)
print(f"Computer choice is: {Game[computer_choice]}")
print("Your choice is: ")
if user_choice==computer_choice:
    print(Game[user_choice])
    print("It's Draw")
elif (user_choice==0 and computer_choice==2 or
      user_choice==1 and computer_choice==0 or
      user_choice==2 and computer_choice==1):
    print(Game[user_choice])
    print("You WIN")
elif (user_choice == 2 and computer_choice == 0 or
      user_choice == 0 and computer_choice == 1 or
      user_choice == 1 and computer_choice == 2):
    print(Game[user_choice])
    print("Computer WINS")
else:
    print("You did not choose the right option")
