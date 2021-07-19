
import art



# Add
def sum(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#  Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": sum,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(art.logo)
    num1 = float(input("What's your first number? "))



    should_continue = False
    while not should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the above line: ")
        num2 = float(input("What's your next number? "))

        calculation_function = operations[operation_symbol]
        result = calculation_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        choice = input(f"Type 'yes' to continue calculating with {result}. Type 'no' for exit: ").lower()

        if choice == 'yes':
            num1 = result
        else:
            should_continue = False
            calculator()

calculator()