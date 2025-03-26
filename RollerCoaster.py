print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
bill=0
if height >= 120:
    if age<12:
        bill+=5
        print(f"You choose Child Ticket ${bill} ")
    elif age<=18:
        bill+=7
        print(f"You choose Junior Ticket ${bill} ")
    else:
        bill+=12
        print(f"You choose Adult Ticket ${bill} ")

    photo = input("Do you want PHOTOS ?")
    if photo == "yes":
            bill += 3
            print(f"You choose photos for extra 3$, your total is {bill} ")
    else:
        print(f"Your total is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
