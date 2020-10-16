
import random  # importing necessary module
import mid_kmean_fernandez.libs.Point as pt  # import Point class

def random_coordinates(num_point=10, dimension=2, lower_bound=(0, 0), upper_bound=(10, 10)):
    """
    function generates random coordinate in a tuple between lower_bound and upper_bound values
    depending on number of dimensions
    """
    random.seed(1000)  # set seed
    coordinate_list = []  # empty list to hold coordinates
    try:
        if dimension == 2:
            for num in range(num_point):  # loop num_point times and append each Point randomly created in 2d
                coordinate_list.append(pt.Point(x=random.uniform(lower_bound[0], upper_bound[0]),
                                             y=random.uniform(lower_bound[1], upper_bound[1])))
            return (coordinate_list)
        elif dimension == 3:  # loop num_point times and append each Point randomly created in 3d
            for num in range(num_point):
                coordinate_list.append(pt.Point(x=random.uniform(lower_bound[0], upper_bound[0]),
                                             y=random.uniform(lower_bound[1], upper_bound[1]),
                                             z=random.uniform(lower_bound[2], upper_bound[2])))
            return (coordinate_list)
        else:  # catch dimensions greater than 3
            print("Function does not support dimensions greater than 3")
            return coordinate_list
    except TypeError:
        print("Please enter numeric values")


def check_same_coordinate(point1, point2):
    """
    Function checks if two point instances have the same positon
    """
    try:
        if (point1.x == point2.x) and (point1.y == point2.y) and (point1.z == point2.z):
            return True
        else:
            return False
    except TypeError:
        print("Incorrect argument type detected")
