#######################################
# Name: Shad Fernandez
# RedID: 810466716
# Date: 09-SEP-2020
#######################################

# Q1
# Declare and initialize tuple. Slice tuple and print from 4th index to last
myList = (20, 'apple', 3.14, [3,1,4], 100, 'oranges', 'coconut', 100001, 12.23435)
i = slice(4,9)
print(myList[i])

# Q2
# Declare and initialize sets
setA = set(['cyan','magenta','yellow','black'])
setB = set(['red','orange','green','blue','magenta','black'])

# Test set methods using intersection, difference, superset and union
print(setA.intersection(setB))
print(setA.difference(setB))
print(setA.issuperset(setB))
print(setB.union(setA))

# Q3
# Create a dictionary.
my_dictionary = {'monkey': 20, 'eagle': 30, 'tiger': 27, 'shark': 23,
                'lion': 34, 'gorilla': 21, 'alligator': 30}
# Find max value then usa a loop to find the corresponding key.
maxVal = max(my_dictionary.values())
for key, value in my_dictionary.items():
    if value == maxVal:
        print(key, value)

# Q4
# In lines 39 and 40, the string and random modules are already been imported
import string
import random

# Create a string variable to hold ascii letter (alphabet upper and lowercase)
s_base = string.ascii_letters

# The seed generator is initialized
random.seed(582)

# Declare a string variable hold random characters
s = ""
# Loop to 200. A random number between 0 and 25 is generated using the
# randint method. Random characters in s_base is accessed
# and appended to the variable s.
for i in range(200):
    s += s_base[random.randint(0,25)]
print(s)

# Q5
# Create a variable to hold a string
testString = 'This is a test. Turtle tames tesla tanking stocks.' \
             ' Temperature today is totally hot hotter than Tacoma.'
# Create an empty dictionary
string_dict_one = {}
# Loop through each letters in testString. Ignore spaces.
# If letter exist in string_dict, append else add to string_dict
for letter in testString:
    if letter == ' ':
        pass
    elif letter in string_dict_one:
        string_dict_one[letter] += 1
    else:
        string_dict_one[letter] = 1
#print string_dict_one
print(string_dict_one)

# Q6
# Loop through string_dict. If character count is greater than
# or equal to ten, then print key value pair
for key, value in string_dict_one.items():
    if value >= 10:
        print(key, value)

# Q7
# Create a string variable and assign letters of the alphabet (lowercase then uppercase) as value
ascii_letters = string.ascii_letters

# Seed generator is initialized to 902
random.seed(902)

# Declare and initialize a empty string variable
charCount = ""

# Loop to 50. A random number between 0 and 25 is generated using the
# randint method. Random characters in ascii_letters is accessed
# and appended to the variable s.
for i in range(50):
    charCount += ascii_letters[random.randint(0,25)]
print(charCount)

# Q8
# Create an empty dictionary to hold letter count pair
string_dict_two = {}

# Loop through characters in charCount from Q7. Ignore spaces.
# If letter exist, add 1 to count else add letter to dictionary
# and add 1.
for letter in charCount:
    if letter == ' ':
        pass
    elif letter in string_dict_two:
        string_dict_two[letter] += 1
    else:
        string_dict_two[letter] = 1
print(string_dict_two)

# Q9
# Create two empty sets
setC = set()
setD = set()

# Create two sets using the keys from two dictionaries
# from the previous questions.
for key in string_dict_one:
    setC.add(key)
for key in string_dict_two:
    setD.add(key)
# Print unique character that are in setC but not in SetD
print(setC.symmetric_difference(setD))

#Q 10
# Declare and initialize a None object
nada = None
test1 = ""
test2 = 0

# Check if logic applies
print(nada == None)

# Checking type
print(type(nada))

# Check if equal to empty string
print(nada == test1)

# Check if equal to zero
print(nada == test2)





