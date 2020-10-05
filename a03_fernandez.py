#######################################
# Name: Shad Fernandez
# RedID: 810466716
# Date: 15-SEP-2020
#######################################

# Q1
def compare(x,y):
    """  compare returns a numeric value depending if x greater than, less than, or equal to y

    Parameters:
        x, y (int or float): numeric values to be compared
    Return:
        int: -1, 0, or 1 if x > 1, x < 1, or x == y respectively
    """
    if (x > y):
        return 1
    elif (x < y):
        return -1
    else:
        return 0


# Q2
def is_between(x, y, z):
    """  is_between compares if numeric y is between numeric values x and z

    Parameters:
        x, y, z (int): numeric values
    Return:
        boolean: true if y is between else false
    """
    if (x <= y) and (y <= z):
        return True
    else:
        return False

# Q3
def favorite_movie(movie):
    """ favorite_movie prompts user to enter favorite movie and prints out input as favorite move

    Parameter:
        movie (string): favorite movie input
    Return:
        string: string input as favorite move
    """
    print("My favorite movie is " + str(movie) + ".")

# Testing function favorite movie
# favorite_movie(str(input("What is your favorite movie? ")))

# Q4
def fiz_buzz(max_iteration=100, fizz_divider=3, buzz_divider=5):
    """  fix_buzz prints fizz buzz if iteration is divisible by fizz_divider and buzz_divider,
    prints fizz_divider if divisible by fizz_divider, prints buzz_divider if divisible by buzz_divider

    Parameter:
        max_iteration (int): numeric int value that will set number of iterations
        fizz_divider (int): numeric int value
        buzz_divider (int): numeric int value
    Return:
        string: fizz buzz if divisible by fizz_divider and buzz_divider
        string: fizz if divisible by fizz_divider
        string: buzz if divisible by buzz_divider

    """
    for num in range(1,max_iteration):
        if (num % fizz_divider == 0) and (num % buzz_divider == 0):
            print("fizz buzz")
        elif (num % fizz_divider == 0):
            print("fizz")
        elif (num % buzz_divider == 0):
            print("buzz")
        else:
            print(num)

# Testing fizz_buzz
#fiz_buzz(50,5,7)

# Q5

# Declaring coordinates of SD, LA, and SB as tuples
sandiego_coord = (3619785.60, 484903.85)
losangeles_coord = (3768645.35, 385215.53)
santabarbara_coord = (3811331, 252490)

def distance_calculator(*args):
    """ distance_calculator calculates the distance between two UTM coordinates and returns the distance.

    Parameters:
        *arg1 (float): tuple containing UTM coordinates

    Returns:
        float: distance between two coordinates in kilometers
    """
    myList = []  # Create an empty list

    for x_coord, y_coord in args:  # Iterate contents of the tuples and append values to list
        myList.append(x_coord)
        myList.append(y_coord)

    distance = (((myList[0] - myList[2]) ** 2) + ((myList[1] - myList[3]) ** 2)) ** 0.5  # Calculate distance
    return(distance/1000)  # Return distance

# printing function docstring
print(distance_calculator.__doc__)


#  Testing function with declared coordinates
print(distance_calculator(sandiego_coord, losangeles_coord))
print(distance_calculator(sandiego_coord, santabarbara_coord))
print(distance_calculator(losangeles_coord, santabarbara_coord))

# Q6

# import necessary libraries

import string
import random

def random_letter(length=16,seed=500):
    """ random_letter generates a string of random character of the alphabet

    Parameters:
        length (int): sets length of string.
        seed (int): sets seed for random

    Return:
        string: a string of random characters

    """
    s_base = string.ascii_letters  # create a string of english alphabet (upper and lowercase)
    random.seed(seed)  # set seed
    for i in range(length):  # append random letters to string and return string
        s_base += s_base[random.randint(0,25)]
    return(s_base)

def letter_counter(text):
    """ letter_counter counts the number of times a character appears in a string

    Parameters:
        text (string): count of each character in text will be counted
    Return:
        dictionary: letter and character count pair
    """
    letter_dict = {}
    # Loop through each letters in testString. Ignore spaces.
    # If letter exist in string_dict, append else add to string_dict
    for letter in text:
        if letter == ' ':
            pass
        elif letter in text:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return(letter_dict)


# Q7
# The echo function can take most data types (if not all covered in class) as an argument randing from int,
# float and strings as well collections such as lists, tuples, sets, and dictionaries. The echo
# function can take multiple arguments in one function call. The * and ** symbols can unpack
# collection types.

def echo(*args, **kwargs):
    print(args, kwargs)

# create different types of collections
list1 = [1,2,3,'stringr']
tuple1 = (1,2,1.0,3,5)
set1 = {'la','la2',3.0}
dict1 = {1:"test",2:"love"}

# test echo function
echo(tuple1,dict1)
echo(tuple1,tuple1,dict1,dict1)
echo('string',2,6,list1,tuple1,set1,dict1)

# Q8
def addif(threshold=0, *args):
    """ function returns the sum of the values above the threshold

    Parameters:
        threshold (numeric value): threshold default at 0

    Return:
        total (numeric value): total of values abover threshold
    """
    total = 0  # will hold sum of values above threshold
    for val in args:  # iterate through args and add values above threshold
        if val > threshold:
            total+=val
    return(total)

#  Testing addif
print(addif(6.0,1,2,3.0,4,5,3,5,6,7.0,9.0))

print(addif(9.0,21,13,-21,3,2,2.34,3.14,-10,10))












