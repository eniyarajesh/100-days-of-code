def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print("Welcome to calculator!!")
    print("\n")

    calc_continue = True

    num1 = float(input("Enter the first number: "))
    while calc_continue:
        for i in operation:
            print(i)
        operation_syml = input("Enter the operation: ")
        num2 = float(input("Enter the next number: "))

        result = operation[operation_syml](num1,num2)
        print(f"{num1} {operation_syml} {num2} = {result}")
        print("\n")

        calc_choice = input(f"Type 'y' to continue calculating with {result}, or 'n' to start new calculation. \nType 'x' to exit the calculator \n").lower()
        if calc_choice == "y":
            num1 = result
            print("\n")
        elif calc_choice == "n":
            calc_continue = False
            print("\n" * 20)
            calculator()
        elif calc_choice == "x":
            print("Thank you, Have a good day!!")
            break

calculator()