# Reuben McGuire
# UWYO COSC 1010
# 11/6/2024
# Lab 08
# Lab Section: 15
# Sources, people worked with, help given to:
# 


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def convert(string):
    if "." in string:
        try:
            num = float(string)
        except:
            converted = "Cannot be converted."
        else:
            converted = int(num)
    else:
        try:
            num = int(string)
        except:
            converted = "Cannot be converted."
        else:
            converted = float(num)
    return converted

while True:
    number = input("Enter an integer or a float:\nEnter 'q' to exit. ")
    if number == "q":
        break
    else:
        print(convert(number))

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def evaluate(m, b, l, h):
    y_vals = []
    if l > h:
        y_vals = False
    try:
        for x in range(l,h+1):
            y_vals.append(m*x+b)
    except:
        y_vals = False
    return y_vals

while True:
    
    slope_string = input("Slope: ")
    intercept_string = input("y-intercept: ")
    lower_string = input("Lower x-bound: ")
    upper_string = input("Upper x-bound: ")
    
    if slope_string == 'exit' or intercept_string == 'exit' or lower_string == 'exit' or upper_string == 'exit':
        break

    try:
        slope = float(slope_string)
        intercept = float(intercept_string)
        lower = int(lower_string)
        upper = int(upper_string)
    except:
        print("Invalid equation entry.")
        pass
    else:
        if evaluate(slope, intercept, lower, upper) == False:
            print("Invalid equation entry.")
        else:
            try:
                print(evaluate(slope, intercept, lower, upper))
            except:
                print("Invalid equation entry.")

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def square_root(num):
    if num < 0:
        root = False
    else:
        root = num**(1/2)
    return root

def quad(a, b, c):
    x_1 = ((-b + square_root(b**2 - 4*a*c)) / (2*a))
    x_2 = ((-b - square_root(b**2 - 4*a*c)) / (2*a))

    return [x_1, x_2]


while True:
    
    first = input("a: ")
    second = input("b: ")
    third = input("c: ")

    if first == 'exit' or second == 'exit' or third == 'exit':
        break
    else:

        try:
            a_1 = float(first)
            b_2 = float(second)
            c_3 = float(third)
        except:
            print("Invalid entry.")
            pass
        else:
            try:
                print(quad(a_1, b_2, c_3))
            except:
                print("Invalid entry.")