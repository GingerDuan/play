"""CLI application for a prefix-notation calculator."""

from arithmetic import *

#loop to make calculator continuous
while True:
    input_string = input("What do you want to calculate today?: ")
    tokens = input_string.split(" ") #tokenization

    # q to quit
    if "q" in tokens or "quit" in tokens:
        break

    #needs minimum of 2 inputs (operator and number)
    if len(tokens) < 2:
        print("Not enough inputs.")
        continue

    #make sure num2 is a number otherwise set to 0
    if len(tokens) < 3:
        num2 = 0
    else:
        num2 = tokens[2] 

    operator = tokens[0] 
    num1 = tokens[1] 
    result = 0
    
    if not num1.isdigit() or not num2.isdigit():
        print("Last two are not numbers")
        continue
    else:
        num1 = float(num1) 
        num2 = float(num2)

        if operator == "pow":
            result = power(num1, num2)
        
        elif operator == "+":
            result = add(num1, num2)

        elif operator == "-":
            result = subtract(num1, num2)
        
        elif operator == "*":
            result = multiply(num1, num2)

        elif operator == "/":
            result = divide(num1, num2)
            
        elif operator == "^2":
            result = square(num1)

        elif operator == "^3":
            result = cube(num1)
            
        elif operator == "%":
            print(mod(num1, num2))

        else:
            print("This is not calculable")
            continue
    
        print(result)


