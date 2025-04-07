import art
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def calculator():
    print(art.logo)
    operation={"+": add, "-": subtract, "*": multiply, "/": divide}
    first=int(input("Enter first number: "))
    cont=True
    while cont:
        for symbol in operation:
            print(symbol)
        operation_symbol=input("\nWhich operation you wanna use ?")
        second=int(input("Enter second number: "))
        answer=operation[operation_symbol](first, second)
        print(f"{first} {operation_symbol} {second} = {answer}")
        choice=input("Do you wanna continue with the same result as first number ? yes/no : ")
        if choice=="yes":
            first=answer
        elif choice=="no":
            cont=False
            print("\n"*20)
            calculator()
        else:
            print("Invalid choice")
            cont=False
            print(f"The last result was : {answer}")
calculator()