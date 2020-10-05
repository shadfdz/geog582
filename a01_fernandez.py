# #######################################
# # Name: Shad Fernandez
# # RedID: 810466716
# # Date: 31-AUG-2020
# #######################################

#Q1
a = 4
b = 3.14
c = ['apple', 'pies', 'hi', 1]
print(a, " ", b, " ", c[2])

#Q2
i = 582
print("GEOG" + str(i))

#Q3
base = 10
height = 12
area = 0.5 * base * height
print(area)

#Q4
for n in range(1,50,2):
    print(n)

#Q5
a = 100
while (a >= 0):
    print(a)
    a -= 1

#Q6
list1 = []
for n in range(100, 201, 2):
    list1.append(n)
print(list1)


#Q7
loc1 = [[32.715736, -117.161087], [34.052235, -118.243683], [34.41383, -119.69296]]

#Q8
loc2 = [[3619785.60, 484903.85], [3768645.35, 385215.53], [3811331, 252490]]
distance = (((loc2[0][0]-loc2[2][0])**2) + ((loc2[0][1]-loc2[2][1])**2))**0.5
print(distance/1000)

#Q9
for n in range(1,101):
    if n % 3 == 0 and n % 7 == 0:
        print("fizz buzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 7 == 0:
        print("buzz")
    else:
        print(n)

#Q10
list2 = [1,2,2,3,5,7,21,21,46,65,67]
print(list2[3:6])

#Q11
list2.insert(6,'a')
print(list2)

#Q12
list2.append('1001')
list2.extend('z')
print(list2)

#Q13
firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")
print("Hello" + " " + firstName + " " + lastName)

#Q14
integer = int(input("Please enter an integer and I'll print the divisors: "))
divisors = []
for n in range(1, integer + 1):
    if integer % n == 0:
        divisors.append(n)
print(divisors)

#Q15
primes = []                 #list to hold prime numbers
for n in range(2,10000):    #loop between between range
    isPrime = True              #set flag
    for m in range(2,n):        #loop to check if number is divisible
        if n % m == 0:
            isPrime = False    #set flag to false if divisible
            break;
    if isPrime:                 #append number if not divisible
        primes.append(n)
print(primes)
print(len(primes))
