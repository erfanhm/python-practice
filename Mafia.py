import os
from time import sleep
import random
mainroles={
    'Godfather':"The one who is the Mafia's Boss",
    'Dr.Lecter':"The one who could save the Mafia members from sniper's shot",
    'Regular Mafia':"The one who is just in Mafia side and he/she doesn't have any ability",
    'Doctor':"The one who could save the citizens from Mafia's shot",
    'Sniper':"The one who could shot Mafias at night",
    'Detector':"The one who could figured out who is Mafia or who is Citizen during night by God's Like or Dislike",
    'Regular Citizen':"The one who doesn't have any ability",
    'Mayor':"The one who could cancel the election in day",
    'Psychiatrist':"The one who could silent any of the players in the morning"
}
print("Welcome to the Mafia :)\n")
population=int(input("How many people are you playing now ? "))
assign={}
available_roles=list(mainroles.keys())
assigned_roles = {}
for _ in range(population):
    user_name = input("Enter your name: ")
    role = random.choice(list(mainroles.keys()))
    description = mainroles[role]

    print(f"\n{role}: {description}")
    sleep(3)

    os.system('cls' if os.name == 'nt' else 'clear')

    assigned_roles[user_name] = role
    del mainroles[role]

print("Pass the phone to the GOD, BITCH!.\n")
sleep(5)
god=input("Are you the GOD ?").lower()
if god=="yes":
    print("🎭 Final Role Assignments:")
    for name, role in assigned_roles.items():
        print(f"{name}     :      {role}")
        print("------------------------------")
else:
    print("FUCK YOU!\nI said pass the phone to the GOD")
