while True:
    import math
    import os
    os.system('cls')
    print("Welcome to the calculator!")
    print("Current version: 1.3")
    try: 
        numb1 = input("Please enter your first number or enter '#' for percentage calculator (HCF does not recognise this number, so type in a random one.): ")
        if numb1 == "#":
            os.system('cls')
            ask = input("Enter 'd' to calculate the percentage of a decimal or type 'p' to calculate the percentage of an amount. ").lower()
            if ask == 'd':
                os.system('cls')
                decimal = float(input("Enter your decimal: "))
                try: 
                    perc = decimal * 100
                    print(f'{perc}%')
                    ask = input("Do you want to try again? ").lower()
                    if ask == 'yes':
                        continue
                    else:
                        exit()
                except ValueError:
                    print("Invalid operation.")
                    ask = input("Do you want to try again? ").lower()
                    if ask == 'yes':
                        continue
                    else:
                        exit()
            elif ask == 'p':
                percentage = float(input("Percentage (don't include '%'): "))
                whole = float(input("Of what number? "))
                os.system('cls')
                try: 
                    p = (percentage * whole) / 100
                    print(f'{percentage}% of {whole} is {p}.')
                    ask = input("Do you want to try again? ").lower()
                    if ask == 'yes':
                        continue
                    else:
                        exit()
                except ValueError:
                    print("Invalid value.")
                    ask = input("Do you want to try again? ").lower()
                    if ask == 'yes':
                        continue
                    else:
                        exit()
            else:
                ask = input("Do you want to try again? ").lower()
                if ask == 'yes':
                    continue
                else:
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
            print("D = Percentage Decrease calculator")
            symbol = input("Please enter what operation you are going to do from the list above: ")
            os.system('cls')
            if symbol == 'x':
                try: 
                    numb2 = float(input(f'Please enter what number you are multiplying {numb1} by: '))
                except ValueError:
                    print("Invalid input. Please enter a numerical value.")
                    ask = input("Do you want to try again? ").lower()
                    if ask == 'yes':
                        continue
                    else:
                        exit()
                math = numb1 * numb2
                os.system('cls')
                print(f'The answer of {numb1} multiplied by {numb2} is {math}.')
                ask = input("Do you want to try again? ").lower()
                if ask == 'yes':
                    continue
                else:
                    exit()
            elif symbol.lower() == symbol == '/':
                try:
                    numb2 = float(input(f'Please enter what number you are dividing {numb1} by: '))
                except ValueError:
                    print("Invalid input. Please enter a numerical value.")
                    ask = input("Do you want to try again? ").lower()
                    if ask == 'yes':
                        continue
                    else:
                        exit()
                if numb2 == 0:
                    print("The answer is 0.")
                    input("Press enter to exit.")
                    exit()        
                else:
                    math = numb1 / numb2
                    os.system('cls')
                    print(f'The answer of {numb1} divided by {numb2} is {math}.')
                    ask = input("Do you want to try again? ").lower()
                    if ask == 'yes':
                        continue
                    else:
                        exit()
            elif symbol.lower() == symbol == '+':
                try:
                    numb2 = float(input(f'Please enter what number you are adding {numb1} to: '))
                except ValueError:
                    print("Invalid input. Please enter a numerical value.")
                    ask = input("Do you want to try again? ").lower()
                    if ask == 'yes':
                        continue
                    else:
                        exit()
                math = numb1 + numb2
                os.system('cls')
                print(f'The answer of {numb1} plus {numb2} is {math}.')
                input("Press enter to exit.")
                exit()
            elif symbol.lower() == symbol == '-':
                try:
                    numb2 = float(input(f'Please enter what number you are subtracting {numb1} by: '))
                except ValueError:
                    print("Invalid input. Please enter a numerical value.")
                    ask = input("Do you want to try again? ").lower()
                    if ask == 'yes':
                        continue
                    else:
                        exit()
                math = numb1 - numb2
                os.system('cls')
                print(f'The answer of {numb1} take away {numb2} is {math}.')
                ask = input("Do you want to try again? ").lower()
                if ask == 'yes':
                    continue
                else:
                    exit()
            elif symbol.lower() == symbol == '!':
                os.system('cls')
                a = math.sqrt(numb1)
                b = math.floor(a)
                c = math.ceil(a)
                print(f'The square root of {numb1} is {a}.')
                print(f'Because of this, we know that the square root of {numb1} is between {b} and {c}.')
                ask = input("Do you want to try again? ").lower()
                if ask == 'yes':
                    continue
                else:
                    exit()
            elif symbol.lower() == symbol == '**':
                numb2 = float(input(f'Please enter the power {numb1} is going to have: '))
                try:
                        math = numb1 ** numb2
                except OverflowError:
                        print("Power too large. Please enter a smaller power / number next time and enter a numerical value.")
                        ask = input("Do you want to try again? ").lower()
                        if ask == 'yes':
                            continue
                        else:
                            exit()
                print(f"{numb1} raised to the power of {numb2} is {math}.")
                ask = input("Do you want to try again? ").lower()
                if ask == 'yes':
                    continue
                else:
                    exit()
            elif symbol.lower() == symbol.lower() == "lcm":
                try:
                    numb1 = int(numb1)
                    numb2 = int(input("What do you want the second number to be? "))
                except ValueError:
                    print("Invalid value.")
                    ask = input("Do you want to try again? ").lower()
                    if ask == 'yes':
                        continue
                    else:
                        exit()
                try:
                    a = math.lcm(numb1,numb2)
                except ValueError:
                    input("Invalid input.")
                    ask = input("Do you want to try again? ").lower()
                    if ask == 'yes':
                        continue
                    else:
                        exit()
                print(f'The LCM of {numb1} and {numb2} is {a}')
                ask = input("Do you want to try again? ").lower()
                if ask == 'yes':
                    continue
                else:
                    exit()
            elif symbol.lower() == symbol.lower() == "hcf":
                numbers = input("Enter your numbers with a comma seperating them (no spaces): ")
                try:
                    numb = [int(num) for num in numbers.split(',')]
                except ValueError:
                    print("Invalid operation, try again.")
                    ask = input("Do you want to try again? ").lower()
                    if ask == 'yes':
                        continue
                    else:
                        exit()
                try: 
                    a = math.gcd(*numb)
                    test = numbers.replace(',',', ')
                except ValueError:
                    print("Invalid operation, try again.")
                    ask = input("Do you want to try again? ").lower()
                    if ask == 'yes':
                        continue
                    else:
                        exit()
                except OverflowError:
                    int("Invalid operation, try again.")
                    ask = input("Do you want to try again? ").lower()
                    if ask == 'yes':
                        continue
                    else:
                        exit()  
                os.system('cls')
                print(f'The HCF of {test} is {a}.')
                ask = input("Do you want to try again? ").lower()
                if ask == 'yes':
                    continue
                else:
                    exit()
            elif symbol.lower() == 'd':
                os.system('cls')
                try:
                    numb2 = float(input("Please enter your second number: "))
                except ValueError:
                    print("Invalid operation, try again.")
                    ask = input("Do you want to try again? ").lower()
                    if ask == 'yes':
                        continue
                    else:
                        exit()
                try:
                    step1 = numb1 - numb2
                    step2 = (step1/numb1)*100
                except ValueError:
                    print("Invalid operation, try again.")
                    ask = input("Do you want to try again? ").lower()
                    if ask == 'yes':
                        continue
                    else:
                        exit()
                os.system('cls')
                print(f'The decrease of {numb1} and {numb2} is by {step2}%.')
                ask = input("Do you want to try again? ").lower()
                if ask == 'yes':
                    continue
                else:
                    exit()
        print("Invalid operation, try again.")
        ask = input("Do you want to try again? ").lower()
        if ask == 'yes':
            continue
        else:
            exit()


    except ValueError:
        print("Invalid input. Please enter a numerical or correct value.")
        ask = input("Do you want to try again? ").lower()
        if ask == 'yes':
            continue
        else:
            exit()
