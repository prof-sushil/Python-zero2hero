# This is my first python module. The module name will be calculator.

'''
    This is a simple calculator.
    This module has four simple arithmetic functions that are defined below.
'''

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

# Let's print the __name__ variable
print("__name__ variable of calculator module: ", __name__)
# The file which we excute from terminal will have __name__ variable as __main__.
# And remaining files will have __name__ variable as the name of the file

if __name__ == "__main__":
    # This block of code will be executed only when we run this file directly
    print("Adding 2 and 3 using calculator: ", add(2, 3))
    print("Multiplying 2 and 3 using calculator: ", mul(2, 3))