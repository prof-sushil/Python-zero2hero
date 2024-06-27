# From this file I will use my custom package called mymath

# Importing mymath module
from mymath.calculator import * # This will import all the functions from the calculator module(* means import all)

# Similarly we can import geometry module as well
# But I will show you slightly different way to do it for learning purpose
from mymath import geometry # This will import only geometry module


# Let's print the __name__ variable
print("__name__ variable of run.py: ", __name__)
# The file which we excute from terminal will have __name__ variable as __main__.
# And remaining files will have __name__ variable as the name of the file

if __name__ == "__main__":
    print("Adding 2 and 3 using calculator: ", add(2, 3))
    print("Multiplying 2 and 3 using calculator: ", mul(2, 3))
    # We have imported only geometry module not its functions. So we need to use geometry.<function_name> to access its functions
    print("Area of rectangle with l=5 and b=2: ", geometry.area(5, 2)) 
    print("Perimeter of rectangle with l=5 and b=2: ", geometry.perimeter(5, 2))