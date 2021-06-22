from art import logo

# Clear method to clear the screen
from replit import clear


# Add
def add(number1, number2):
    return number1 + number2


# Subtract
def subtract(number1, number2):
    return number1 - number2


# Multiply
def multiply(number1, number2):
    return number1 * number2


# Divide
def divide(number1, number2):
    return number1 / number2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    # Taking user input
    number1 = float(input("What is the first number?\nFirst number: "))

    # Printing the operants
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
      operator = input("Pick an operation from the above line.\nOperator: ")

      number2 = float(input("What is the next number?\nNext number: "))

      # Calculations
      calculation = operations[operator]
      answer = calculation(number1, number2)

      print(f"{number1} {operator} {number2} = {answer}")

      # Asking user for continue
      if input(f"Type 'y' to continue calculation with {answer} or type 'n' to exit.\n\nWant to continue: ") == "y":
          number1 = answer
          clear()
      else:
          should_continue = False
          clear()
          calculator()


calculator()

