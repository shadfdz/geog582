# #######################################
# # Name: Shad Fernandez
# # RedID: 810466716
# # Date: 16-SEP-2020
# #######################################
# Q1

class Greeting:
    """Class returns a greeting"""

    def say_hello(self):
        """method prints a greeting"""
        print("Hello from GEOG582")

greet = Greeting()  # create a greeting object

greet.say_hello()  # call say hello method


# Q2
class Person:
    """Class represents a person"""

    def __init__(self, name=None, age=None):
        """Constructor to initialize name and age attribute"""
        self.name=name
        self.age=age

    def print_name(self):
        """method returns name"""
        print(self.name)

    def print_age(self):
        """method returns age"""
        print(self.age)

shad = Person("Shad",20)  # create a person object
shad.print_age();  # print age (i'm not 20 btw)
shad.print_name();  # print name

# Q3
class Counter():
    """Class keeps a counter attribute that can be incremented"""
    def __init__(self, counter=1):
        """Constructor initializes counter default value 1"""
        self.count = counter

    def get_value(self):
        """method returns count attribute"""
        print(self.count)

    def count_up(self):
        """increments count by 1"""
        self.count += 1

    def clear_counter(self):
        """restart count value to 1"""
        count = 1

class DistanceCalculator():
    """Class calculates distance in km between two coordinates tuples

    Args:
        coordinate_1 (numeric tuple): coordinate pair in minutes
        coordinate_2 (numeric tuple): coordinate pair in minutes

    Attributes:
        coordinate_1 (numeric tuple): coordinate pair in minutes
        coordinate_2 (numeric tuple): coordinate pair in minutes
        distance (numeric): distance between coordinate_1 and coordinate_2

    """
    def __init__(self, coordinate_1=(0, 0), coordinate_2=(10, 10)):
        """
        Constructor initializes coordinates. Default values provided for no argument

        Args:
            coordinate_1 (numeric tuple): coordinate pair in minutes
            coordinate_2 (numeric tuple): coordinate pair in minutes
        """
        self.coordinate_1 = coordinate_1
        self.coordinate_2 = coordinate_2
        self.distance = None

    def get_distance(self):
        """
        method calculates and returns distance in km between coordinates
        """
        try:
            self.distance = (((self.coordinate_1[0] - self.coordinate_2[0]) ** 2) + (
                        (self.coordinate_1[1] - self.coordinate_2[1]) ** 2)) ** 0.5
            self.distance = self.distance / 1000
            return (self.distance)  # Return distance
        except TypeError:
            print("Please enter a numeric value or tuple for coordinates")

class TravelTime(DistanceCalculator):
    """Class calculates distance in km and time in hr between two coordinates tuples

    Args:
        coordinate_1 (numeric tuple): coordinate pair in minutes
        coordinate_2 (numeric tuple): coordinate pair in minutes
        speed (numeric): in km per hour

    Attributes:
        coordinate_1 (float tuple): coordinate pair in minutes
        coordinate_2 (float tuple): coordinate pair in minutes
        distance (float): distance between coordinate_1 and coordinate_2
        speed (numeric): in km per hour
        time (numeric): in hours
    """
    def __init__(self, coordinate_1=(0, 0), coordinate_2=(10, 10), speed=60):
        """
        Constructor initializes coordinates and speed.

        Args:
            coordinate_1 (numeric tuple): coordinate pair in minutes
            coordinate_2 (numeric tuple): coordinate pair in minutes
            speed (numeric): determines travel time
        """
        try:
            super().__init__(coordinate_1, coordinate_2)
            self.coordinate_1 = coordinate_1
            self.coordinate_2 = coordinate_2
            self.speed = speed
            self.distance = None
            self.time = None

        except TypeError:
            print("Please enter a numeric value or tuple for coordinates")

    def get_time(self):
        """
        function returns the travel time using distance and speed
        """
        try:
            super().get_distance()
            self.time = self.distance/self.speed
            return self.time
        except TypeError:
            print("Please enter a numeric value or tuple for coordinates")
        except ZeroDivisionError:
            print("Cannot divide by zero")


sandiego_coord = (3619785.60, 484903.85)
losangeles_coord = (3768645.35, 385215.53)
santabarbara_coord = (3811331, 252490)


la_sb_distance = DistanceCalculator(losangeles_coord,santabarbara_coord)
print(la_sb_distance.get_distance())

la_sd_travel_time = TravelTime(losangeles_coord, santabarbara_coord, 60)

print(la_sd_travel_time.get_time())


# Midterm

class Point():
    """
    Class has attributes to store a 2d or 3d coordinate

    Args:
        x (numeric): x coordinate
        y (numeric): y coordinate
        z (numeric) z coordinate

    Parameters:
        x (numeric): x coordinate
        y (numeric): y coordinate
        z (numeric) z coordinate equal to zero by default
    """
    def __init__(self, x=None, y=None, z=0):
        """
        constructor initializes x,y,z. z default value 0. if z is 0 dimension is 2
        else 3
        """
        try:
            self.x = x
            self.y = y
            self.z = z
            if self.z == 0:
                self.__dimensions = 2
            else:
                self.__dimensions = 3
        except TypeError:
            print("Please enter a numeric value")

    def print_coordinates(self):
        """
        prints coordinates x y z as string
        """
        print("x = {}, y = {}, z = {}".format(self.x,self.y,self.z))

    def calc_dist(self, obj):
        """
        function calculates distance between self and another Point object
        """
        try:
            if (isinstance(obj, Point)) and (self.__dimensions == 2) and (obj.__dimensions == 2):
                return (((obj.x - self.x)**2) + ((obj.y - self.y)**2))**0.5
            elif (isinstance(obj,Point)) and (self.__dimensions == 3):
                return (((obj.x - self.x)**2) + ((obj.y - self.y)**2) + ((obj.z - self.z)**2))**0.5
            else:
                print("Object argument is not a Point class")
        except TypeError:
            print("Please enter a numeric value")

# Q2
import random  # importing necessary module

def random_coordinates(num_point=10, dimension=2, lower_bound=(0,0), upper_bound=(10,10)):
    """
    function generates random coordinate in a tuple between lower_bound and upper_bound values
    depending on number of dimensions
    """
    coordinate_list = []  # empty list to hold coordinates
    try:
        if dimension == 2:
            for num in range(num_point):  # loop num_point times and append each Point randomly created in 2d
                coordinate_list.append(Point(x = random.uniform(lower_bound[0],upper_bound[0]), y = random.uniform(lower_bound[1],upper_bound[1])))
            return(coordinate_list)
        elif dimension == 3:  # loop num_point times and append each Point randomly created in 3d
            for num in range(num_point):
                coordinate_list.append(Point(x = random.uniform(lower_bound[0],upper_bound[0]), y = random.uniform(lower_bound[1],upper_bound[1]),z= random.uniform(lower_bound[2],upper_bound[2])))
            return (coordinate_list)
        else:  # catch dimensions greater than 3
            print("Function does not support dimensions greater than 3")
            return coordinate_list
    except TypeError:
        print("Please enter numeric values")


# list1 = random_coordinates()  # create random_coordinates object
# for num in range(len(list1)):  # print coordinates
#     list1[num].print_coordinates()


# Q3

coordinate_list = random_coordinates(num_point=100, lower_bound=(0,0),upper_bound=(100,100))  # create list of random coordinates

# Q4
point = Point(x=50,y=50)  # create a point
point_distances = []  # create an empty list

for item in coordinate_list:  # create a list of distances between point and coordinates_list points
    point_distances.append(point.calc_dist(item))

shortest_distance = point_distances[0] # find the shortest distance from the list
for num in range(len(point_distances) - 1):
    if (point_distances[num] < shortest_distance):
        shortest_distance = point_distances[num]

print(shortest_distance)  # print shortest distance
print(point_distances.index(shortest_distance))  # find index of shortest distance
coordinate_list[point_distances.index(shortest_distance)].print_coordinates()  # print coordinates of closest point

