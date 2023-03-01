import math
import os

print("Welcome to the calculator!")
print("Current version: 1.3")
try: 
    numb1 = input("Please enter your first number or enter '#' for percentage calculator: ")
    if numb1 == "#":
        os.system('cls')
        ask = input("Enter 'd' to calculate the percentage of a decimal or type 'p' to calculate the percentage of an amount. ").lower()
        if ask == 'd':
            os.system('cls')
            decimal = float(input("Enter your decimal: "))
            try: 
                perc = decimal * 100
                print(f'{perc}%')
                input("Press enter to exit.")
                exit()
            except ValueError:
                print("Invalid operation.")
                input("Press enter to exit.")
                exit()
        elif ask == 'p':
            percentage = float(input("Percentage (don't include '%'): "))
            whole = float(input("Of what number? "))
            os.system('cls')
            try: 
                p = (percentage * whole) / 100
                print(f'{percentage}% of {whole} is {p}.')
                input("Press enter to exit.")
                exit()
            except ValueError:
                print("Invalid value.")
                input("Press enter to exit.")
                exit()
        else:
            input("Invalid value. Press enter to exit.")
            exit()
    else: 
        numb1 = float(numb1)
        os.system('cls')
        print("Operations below:")
        print("x = multiply")
        print("/ = divide")
        print("+ = add")
        print("- = subtract")
        print("! = square root")
        print("** = indicies / powers")
        print("LCM = LCM")
        print("HCF = HCF/GCD")
        symbol = input("Please enter what operation you are going to do from the list above: ")
        os.system('cls')
        if symbol == 'x':
            try: 
                numb2 = float(input(f'Please enter what number you are multiplying {numb1} by: '))
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
                input("Press enter to exit.")
                exit()
            math = numb1 * numb2
            os.system('cls')
            print(f'The answer of {numb1} multiplied by {numb2} is {math}.')
            input("Press enter to exit.")
            exit()
        elif symbol == '/':
            try:
                numb2 = float(input(f'Please enter what number you are dividing {numb1} by: '))
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
                input("Press enter to exit.")
                exit()
            if numb2 == 0:
                print("The answer is 0.")
                input("Press enter to exit.")
                exit()        
            else:
                math = numb1 / numb2
                os.system('cls')
                print(f'The answer of {numb1} divided by {numb2} is {math}.')
                input("Press enter to exit.")
                exit()
        elif symbol == '+':
            try:
                numb2 = float(input(f'Please enter what number you are adding {numb1} to: '))
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
                input("Press enter to exit.")
                exit()
            math = numb1 + numb2
            os.system('cls')
            print(f'The answer of {numb1} plus {numb2} is {math}.')
            input("Press enter to exit.")
            exit()
        elif symbol == '-':
            try:
                numb2 = float(input(f'Please enter what number you are subtracting {numb1} by: '))
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
                input("Press enter to exit.")
                exit()
            math = numb1 - numb2
            os.system('cls')
            print(f'The answer of {numb1} take away {numb2} is {math}.')
            input("Press enter to exit.")
            exit()
        elif symbol == '!':
            os.system('cls')
            a = math.sqrt(numb1)
            b = math.floor(a)
            c = math.ceil(a)
            print(f'The square root of {numb1} is {a}.')
            print(f'Because of this, we know that the square root of {numb1} is between {b} and {c}.')
            input("Press enter to exit.")
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
            input("Press enter to exit.")
            exit()
        elif symbol.lower() == "lcm":
            try:
                numb1 = int(numb1)
                numb2 = int(input("What do you want the second number to be? "))
            except ValueError:
                input("Value error, press enter to exit.")
                exit()
            try:
                a = math.lcm(numb1,numb2)
            except ValueError:
                input("Invalid input.")
                exit()
            print(f'The LCM of {numb1} and {numb2} is {a}')
            input("Press enter to exit.")
            exit()
        elif symbol.lower() == "hcf":
            try:
                numb2 = int(input("What do you want the second number to be? "))
                numb1 = int(numb1)
            except ValueError:
                input("Invalid value, press enter to exit.")
                exit()
            try:
                a = math.gcd(numb1,numb2)
            except ValueError:
                input("Invalid value, press enter to exit.")
                exit()
            os.system('cls')
            print(f'The highest common factor of {numb1} and {numb2} is {a}.')
            input("Press enter to exit.")
            exit()
        print("Invalid operation, try again.")
        input('Press enter to exit.')


except ValueError:
    print("Invalid input. Please enter a numerical or correct value.")
    input("Press enter to exit.")
    exit()
