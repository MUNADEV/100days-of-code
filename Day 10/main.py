from art import *

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print(logo)

def calculator():
    
    
    operation = input("Choose an operation (+, -, *, /): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = 0

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)

    print(f"{num1} {operation} {num2} = {result}")

    if input("Would you like to perform another calculation? (y/n): ") == 'y':
        calculator()

calculator()
