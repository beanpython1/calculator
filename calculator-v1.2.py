import math
import os

print("Welcome to the calculator!")
print("Current version: 1.2")
try: 
    numb1 = float(input("Please enter your first number: "))
except ValueError:
    print("Invalid input. Please enter a numerical value.")
    input("Press {enter} to exit.")
    exit()
os.system('cls')
print("Operations below:")
print("x = multiply")
print("/ = divide")
print("+ = add")
print("- = subtract")
print("! = square root")
print("** = indicies / powers")

symbol = input("Please enter what operation you are going to do from the list above: ")
os.system('cls')
if symbol == 'x':
    try: 
        numb2 = float(input(f'Please enter what number you are multiplying {numb1} by: '))
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
        input("Press {enter} to exit.")
        exit()
    math = numb1 * numb2
    os.system('cls')
    print(f'The answer of {numb1} multiplied by {numb2} is {math}.')
    input("Press {enter} to exit.")
    exit()
elif symbol == '/':
    try:
        numb2 = float(input(f'Please enter what number you are dividing {numb1} by: '))
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
        input("Press {enter} to exit.")
        exit()
    if numb2 == 0:
        print("The answer is 0.")
        input("Press {enter} to exit.")
        exit()        
    else:
        math = numb1 / numb2
        os.system('cls')
        print(f'The answer of {numb1} divided by {numb2} is {math}.')
        input("Press {enter} to exit.")
        exit()
elif symbol == '+':
    try:
        numb2 = float(input(f'Please enter what number you are adding {numb1} to: '))
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
        input("Press {enter} to exit.")
        exit()
    math = numb1 + numb2
    os.system('cls')
    print(f'The answer of {numb1} plus {numb2} is {math}.')
    input("Press {enter} to exit.")
    exit()
elif symbol == '-':
    try:
        numb2 = float(input(f'Please enter what number you are subtracting {numb1} by: '))
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
        input("Press {enter} to exit.")
        exit()
    math = numb1 - numb2
    os.system('cls')
    print(f'The answer of {numb1} take away {numb2} is {math}.')
    input("Press {enter} to exit.")
    exit()
elif symbol == '!':
    os.system('cls')
    a = math.sqrt(numb1)
    b = math.floor(a)
    c = math.ceil(a)
    print(f'The square root of {numb1} is {a}.')
    print(f'Because of this, we know that the square root of {numb1} is between {b} and {c}.')
    input("Press {enter} to exit.")
    exit()
elif symbol == '**':
    numb2 = float(input(f'Please enter the power {numb1} is going to have: '))
    try:
            math = numb1 ** numb2
    except OverflowError:
            print("Power too large. Please enter a smaller power / number next time and enter a numerical value.")
            input("Press {enter} to exit.")
            exit()
    print(f"{numb1} raised to the power of {numb2} is {math}.")
    input("Press {enter} to exit.")
    exit()
print("Invalid operation, try again.")
input('Press {enter} to exit.')
