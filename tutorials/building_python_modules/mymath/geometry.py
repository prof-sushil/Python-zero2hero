# This is my second python module. The module name will be geometry.
# For addition and multiplication, we could use '+' and '*' operator directly
# But I will use add() and mul() functions from calculator module so that we will learn about 
# relative imports


# Relatively importing calculator module because calculator and geometry are on same parent package mymath
from .calculator import add, mul  # Here . represents the package at the same level

'''
    This is a simple geometry module.
    This module has four simple geometry functions that are defined below.
'''

def area(length, breadth):
    return mul(length, breadth)

def perimeter(length, breadth):
    return 2 * add(length, breadth) 

# Let's print the __name__ variable
print("__name__ variable of geometry module: ", __name__)
# The file which we excute from terminal will have __name__ variable as __main__.
# And remaining files will have __name__ variable as the name of the file

if __name__ == "__main__":
    # This block of code will be executed only when we run this file directly
    print("Area of rectangle with l=5 and b=2: ", area(5, 2))
    print("Perimeter of rectangle with l=5 and b=2: ", perimeter(5, 2))