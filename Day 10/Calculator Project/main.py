
from art import logo

print(logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

add_operator = add
subtract_operator = subtract
multiply_operator = multiply
divide_operator = divide

math_operations_dictionary = {
    '+' : add_operator,
    '-' : subtract_operator,
    '*': multiply_operator,
    '/': divide_operator
}

# print(add_operator(4, 8))
def calculator():
    should_continue = True
    first_number = float(input('What is the first number? '))
    while True:
        for symbol in math_operations_dictionary:
            print(symbol)
        operator = input('Pick an operator of +,-,*,/: ')
        second_number = float(input('What is the second number? '))
        result = math_operations_dictionary[operator](first_number, second_number)
        print(f'{first_number} {operator} {second_number} = {result}')

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation ").lower()
        if choice == 'y':
            first_number = result
        else:
            should_continue = False
            print('\n' * 10)
            calculator()


calculator()

