# Program make a simple calculator

import logger
import calculator as calc

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

log = logger.getLogger("log")

roop = True

while roop:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")
    log.info("Enter choice: " + choice)

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        log.info("first number: " + str(num1))
        num2 = float(input("Enter second number: "))
        log.info("second number: " + str(num2))

        if choice == '1':
            result = calc.add(num1, num2)
            print(num1, "+", num2, "=", result)
            log.info("1: function [add] has been excuted: " + str(num1) + " + " + str(num2) + " = " + str(result))

        elif choice == '2':
            result = calc.subtract(num1, num2)
            print(num1, "-", num2, "=", result)
            log.info("2: function [subtract] has been excuted: " + str(num1) + " - " + str(num2) + " = " + str(result))

        elif choice == '3':
            result = calc.multiply(num1, num2)
            print(num1, "*", num2, "=", result)
            log.info("3: function [subtract] has been excuted: " + str(num1) + " * " + str(num2) + " = " + str(result))
        
        elif choice == '4':
            result = calc.divide(num1, num2)
            if(result != None):
                print(num1, "*", num2, "=", result)
                log.info("4: function [divide] has been excuted: " + str(num1) + " / " + str(num2) + " = " + str(result))
            else:
                log.warning("Warning: 0 cannot be a divisor")

        # check if user wants another calculation
        # break the while loop if answer is no
        while True:
            next_calculation = input("Let's do next calculation? (yes/no): ")
            log.info("next_calculation: " + next_calculation)
            if next_calculation.lower() == "no":
                while True:
                    confirm_exit = input("Are you sure? (yes/no): ")
                    log.info("confirm_exit: " + confirm_exit)
                    if confirm_exit.lower() == "yes":
                        roop = False
                        break
                    elif confirm_exit.lower() == "no":
                        break
                break
            elif next_calculation.lower() == "yes":
                break
            
    else:
        log.warning("Warning: Invalid Input. please select 1/2/3/4")