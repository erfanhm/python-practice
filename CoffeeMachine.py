MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit_earned=0
def resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True
def process_coins():
    print("Please insert coins")
    total = int(input("How many quarters ? "))*0.25
    total += int(input("How many dimes ? ")) * 0.10
    total += int(input("How many nickles ? ")) * 0.05
    total += int(input("How many pennies ? ")) * 0.01
    return total
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-= order_ingredients[item]
    print(f"Here is your coffee {drink_name}")
def transaction_successful(money_received,drink_cost):
    if money_received >= drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"Here is ${change} in change")
        global profit_earned
        profit_earned +=drink_cost
        return True
    else:
        print("That's not enough money")
        return False
def ingredient():
    ingredients=MENU[user_choice]["ingredients"]
    cost=MENU[user_choice]["cost"]
    water=ingredients.get("water",0)
    milk=ingredients.get("milk",0)
    coffee=ingredients.get("coffee",0)
    print(f"Water : {water}ml , Milk : {milk}ml , Coffee : {coffee}ml")
    print(f"Cost : {cost}$")
def report():
    container=resources
    water=container.get("water",0)
    milk=container.get("milk",0)
    coffee=container.get("coffee",0)
    money=profit_earned
    print(f"Water : {water}ml , Milk : {milk}ml , Coffee : {coffee}g")
    print(f"Money : {money}$")
def user_drink():
    drink = MENU[user_choice]
    if resource_sufficient(drink["ingredients"]):
        payment = process_coins()
        transaction_successful(payment, drink["cost"])
        make_coffee(user_choice, drink["ingredients"])
is_on = True
while is_on:
    user_choice=input("What would you like? ( espresso / latte / cappuccino ): ").lower()

    if user_choice=="espresso":
        user_drink()
    elif user_choice=="latte":
        user_drink()
    elif user_choice=="cappuccino":
        user_drink()
    elif user_choice=="report":
        report()
    elif user_choice=="off":
        is_on = False
    else:
        print("That is an invalid input")



