"""
AUTHOR: Anselm Munango

Purpose:The purpose of this calculator program is to perform four basic arithmetic operations.
It allows users to input two numbers and an operator, and then it calculates and displays the result. 
The program also includes error handling for invalid inputs and division by zero,
 making it a simple yet functional calculator for basic mathematical operations. 

"""

# Define functions for each operation.
import re


def add(a, b):
    return a + b

# Subtraction, multiplication, and division functions are defined similarly.
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

# Division by zero is handled to prevent errors.
def divide(a, b):
    if b == 0:
        return None
    return a / b

# The calculate function takes two numbers and an operator, and calls the appropriate function based on the operator.
def calculate(num1, operation, num2):
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        return divide(num1, num2)
    else:
        return "Error: Invalid operation."

# The parse_input function uses regular expressions to validate and extract numbers and the operator from the user's input.

def parse_input(user_input):
    try:
        match = re.match(r'^\s*([-+]?\d*\.?\d+)\s*([+\-*/])\s*([-+]?\d*\.?\d+)\s*$', user_input)
        if not match:
            return None, None, None
        
        num1, operation, num2 = match.groups()
        return float(num1), operation, float(num2)
    except ValueError:
        return None, None, None

# The show_menu function displays the welcome message and instructions to the user.
def show_menu():
    print("\nWelcome to the Simple Calculator!")
    print("Select operation: (e.g., 2 + 3)")
    print("Type 'clear' to reset.")
    print("Type 'exit' to quit.")

# The main function runs the calculator program, showing the menu and processing user input until the user decides to exit.
def main():
    show_menu()
    while True:
        user_input = input(">>> ").strip()
        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'clear':
            print("Calculator reset.")
            continue

        num1, operation, num2 = parse_input(user_input)
        if num1 is not None and operation is not None and num2 is not None:
            result = calculate(num1, operation, num2)
            if result is None:
                print("Error: Division by zero.")
            else:
                print(f"{num1} {operation} {num2} = {result}")
        else:
            print("Invalid input. Please enter in the format: number operator number (e.g., 2 + 3)")

if __name__ == "__main__":
    main()