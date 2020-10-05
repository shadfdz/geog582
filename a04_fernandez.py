#######################################
# Name: Shad Fernandez
# RedID: 810466716
# Date: 16-SEP-2020
#######################################

# Q1

exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: "))  # added int keyword to cast input to int
exam_three = int(input("Input exam grade three: "))  # change variable name from exam_3

grades = [exam_one, exam_two, exam_three]
sum = 0

for grade in grades:
    sum+=grade

avg = sum / len(grades)  # misspelled grade. changed to grades

letter_grade = ''  # added variable scope to global

if avg >= 90:
    letter_grade = 'A'
elif (avg >= 80) and (avg < 90):
    letter_grade = 'B'
elif (avg >= 70) and (avg < 80):  # changed c range to >= 70
    letter_grade = 'C'  # mismatch quotes
elif (avg >= 60) and (avg < 70):  # changed ranged since overlapped
    letter_grade = 'D'
else:
    letter_grade = 'F'

for grade in grades:
    print("Exam: " + str(grade))

print("Average: " + str(avg))
print("Grade: " + letter_grade)

if letter_grade == 'F':  # changed is to equal comparator
    print("Student is failing.")
else:
    print("Student is passing")

# Q2
patients = [[175.8, 73.4], [180.2, 59.5], [165.4, 70.2], [193.5, 120]]

def calculate_bmi(height,weight):
    return (weight / ((height/100)**2)) # added parenthesis

def get_bmi_category(bmi):
    if bmi < 18.5:
        return ("underweight") # added parenthesis
    elif bmi < 25.0:
        return ("normal weight") # added parenthesis
    elif bmi < 30.0: # changed to float
        return  ("overweight") # added parenthesis
    else:
        return ("obesity") # added parenthesis

for patient in patients:
    height = patient[0] #instantiated height and weight separately
    weight = patient[1]
    bmi = calculate_bmi(height, weight)
    bmi_category = get_bmi_category(bmi)

    print("Patient's BMI is: {} ({})".format(bmi, bmi_category))

# Q3

try:
    val = int(input("Please enter a numeric value: "))
except ValueError:
    print("Type error. A non numeric value {} was entered.".format(1))
else:
    print("done!")

# Q4

def divide(dividend, divisor):
    """
    divides dividend with the divisor to return the quotient

    Parameters:
        dividend, divisor: numeric values
    Return:
        numeric quotient
    """
    try:
        return (dividend/divisor)  # divide dividend with divisor
    except ZeroDivisionError:
        print("Divided by zero: {}".format(divisor)) # return error if division by zero

divide(5,0)

# Q5
def sum_two_number(val):
    """
    sum_two_number loops until the sum of two user inputs equal the parameter set

    Parameters:
        val: numeric value
    Return:
        none
    """
    num1 = ''
    num2 = ''
    while(num1 + num2 != val):
        try:
            num1 = float(input("Enter the first numeric value: "))
            num2 = float(input("Enter the second numeric value: "))
        except ValueError:
            print("Non numeric value")

sum_two_number(19.0) # testing sum_two_number function

# Q7
# a)
# command: conda update conda #updated conda before creating a virtual environment
# command: conda create --prefix py27 python=2.7 #created a python 2.7 virtual environment in py27
# command: conda create --prefix py35 python-3.5 #created a python 3.5 virtual environment in py35
#
# b)
# /Users/shad/py27
# /Users/shad/py27












