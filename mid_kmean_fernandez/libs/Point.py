# #######################################
# # Name: Shad Fernandez
# # RedID: 810466716
# # Date: 16-OCT-2020
# #######################################

class Point():
    """
    Class has attributes to store a 2d or 3d coordinate

    Args:
        x (numeric): x coordinate
        y (numeric): y coordinate
        z (numeric): z coordinate
        cluster_id (numeric): cluster id

    Parameters:
        x (numeric): x coordinate
        y (numeric): y coordinate
        z (numeric) z coordinate equal to zero by default

    Methods:
        print_coordinates: print x, y, z coordinates
        calc_distance: calculates distance between self and another point

    """
    def __init__(self, x=None, y=None, z=None, cluster_id = -1):
        """
        Constructor initializes point coordinates

        Arguments:
            x (numeric): x coordinate
            y (numeric): y coordinate
            z (numeric): z coordinate. z = 0 by default
            cluster_id (numeric): cluster id number
        """
        try:
            self.x = x
            self.y = y
            self.z = z
            self.cluster_id = cluster_id
            if self.z == None:
                self.__dimensions = 2
            else:
                self.__dimensions = 3
        except TypeError:
            print("Please enter a numeric value")


    def print_coordinates(self):
        """
        prints coordinates x y z as string
        """
        print("x = {}, y = {}, z = {} cluster ID: {}".format(self.x, self.y, self.z, self.cluster_id))

    def calc_distance(self, obj):
        """
        function calculates distance between self and another Point object
        """
        try:
            if (isinstance(obj, Point)) and (self.__dimensions == 2) and (obj.__dimensions == 2):
                return (((obj.x - self.x) ** 2) + ((obj.y - self.y) ** 2)) ** 0.5
            elif (isinstance(obj, Point)) and (self.__dimensions == 3):
                return (((obj.x - self.x) ** 2) + ((obj.y - self.y) ** 2) + ((obj.z - self.z) ** 2)) ** 0.5
            else:
                print("Object argument is not a Point class")
        except TypeError:
            print("Please enter a numeric value")