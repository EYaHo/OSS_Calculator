import warnings

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

#Need to define divide function.
def divide (x,y):
    if y != 0:
        return x / y
    else:
        warnings.warn("0 divisor error")