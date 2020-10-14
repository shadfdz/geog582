#######################################
# Name: Shad Fernandez
# RedID: 810466716
# Date: 09-OCT-2020
#######################################

# #######################################
# # Name: Shad Fernandez
# # RedID: 810466716
# # Date: 14-OCT-2020
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


import random  # importing necessary module

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
                coordinate_list.append(Point(x=random.uniform(lower_bound[0], upper_bound[0]),
                                             y=random.uniform(lower_bound[1], upper_bound[1])))
            return (coordinate_list)
        elif dimension == 3:  # loop num_point times and append each Point randomly created in 3d
            for num in range(num_point):
                coordinate_list.append(Point(x=random.uniform(lower_bound[0], upper_bound[0]),
                                             y=random.uniform(lower_bound[1], upper_bound[1]),
                                             z=random.uniform(lower_bound[2], upper_bound[2])))
            return (coordinate_list)
        else:  # catch dimensions greater than 3
            print("Function does not support dimensions greater than 3")
            return coordinate_list
    except TypeError:
        print("Please enter numeric values")




# Q1

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


# Q2

import sys  # import necessary package

class MyKmeans:
    """
    MyKmeans class

    Attributes:
        k (numeric): defines k clusters
        num_point (numeric): points to generate
        dimesnsion (numeric): defines number of dimensions
        lower_bound (numeric): tuple defines lower bound of points
        upper_bound (numeric): tuple defines upper bound of points
        points (list of Points): hold Point objects
        centroids: dictionary holding centroids

    Methods:
        set_parameters: method sets attribute values using user input

    """
    def __init__(self, k=4, num_points=10, dimension=2, lower_bound=(0, 0),
                 upper_bound=(10, 10)):
        """
        Constructor sets attribute values inlcuding list of points and centroids

        Arguments:
            k (numeric): number of clusters
            num_points (numeric): number of points. default at 10
            dimension (numeric): number of dimensions, default at 2
            lower_bound (numeric): tuple for lower bound coordinates
            upper_bound (numeric): tuple for upper bound coordinates
        """
        self.k = k
        self.num_points = num_points
        self.dimension = dimension
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.points = []
        self.centroids = {}

    def set_parameters(self):
        """
        Method sets k, num_points, dimension, lower bound and upper bound values
        Exceptions raised when ValueError is encountered
        """
        try:
            self.k = float(input("Enter the k value: "))  # get k value
            self.num_points = float(input("Enter number of points: "))  # get num_points value
            self.dimension = float(input("Enter number of dimensions: "))  # get dimensions

            # Retrieve lower bound coordinates
            if (self.dimension == 2):
                self.lower_bound = tuple(float(input("Enter first lower bound number")),
                float(input("Enter second lower bound number")))
            else:
                 self.lower_bound = tuple(float(input("Enter first lower bound number")),
                float(input("Enter second lower bound number")), float(input("Enter third lower bound number")))

                        # Retrieve lower bound coordinates
            if (self.dimension == 2):
                self.upper_bound = tuple(float(input("Enter first lower bound number")),
                float(input("Enter second lower bound number")))
            else:
                 self.upper_bound = tuple(float(input("Enter first lower bound number")),
                float(input("Enter second lower bound number")), float(input("Enter third lower bound number")))


        #  throw ValueError if non numeric values are entered
        except ValueError:
            print("A valid numeric value was not detected. Please try again.")
            sys.exit(1)

    def generate_points(self):
        """
        Method generates Point objects with random coordinates and store in points
        """
        self.points = random_coordinates(self.num_points, self.dimension, self.lower_bound, self.upper_bound)

    def initialize_centroids(self):
        """
        Method stores k random Points as centroids in centroids
        """
        random_k_point = random.sample(self.points,self.k)  # list of k random numbers  between 0 and num_points
        # create dictionary of k random points withing uppd
        for val in range(1, (self.k + 1)):  # assign key value starting at 1 to k
            reference_point = random_k_point[val - 1]  # assign random point to dictionary
            self.centroids[val] = Point(reference_point.x, reference_point.y, reference_point.z, val)


    def assign_random_clust_number(self):
        """
        Method assigns random cluster id between 1 and k to points in self.points
        """
        for point in self.points:  # iterate through points list
            point.cluster_id = random.randint(1,self.k)  # assign random cluster id between 1 and k

    def assign_clust_number(self):
        """
        Method assigns cluster number (from centroid cluster id) to a point from self.points
        based on its distance from any of the centroids. Point gets assigned cluster id of
        centroid closest to it
        """
        for i in self.points:  # loop through points
            min_dist = sys.maxsize  # set min_dist as biggest int value possible
            for j in self.centroids:  # loop through centroids
                dist = i.calc_distance(self.centroids[j])  # calculate distance between point and centroid
                if(min_dist > dist):  # if dist is less than min_dist, assign j as cluster id
                    min_dist = dist
                    i.cluster_id = j

    def update_centroid(self):
        """
        Method updates centroid coordinates based on coordinates of points with matching cluster_ids
        """
        flag_all_same_coordinate = True  # set flag

        # Iterate through centroids and update centroid coordinates based on points with matching cluster ids
        for centroid in self.centroids.values():
            ref_centroid = Point(centroid.x, centroid.y, centroid.z, centroid.cluster_id)  # create reference centroid
            ref_cluster_id = centroid.cluster_id  # add cluster id

            sum_x_coordinates = 0  # to hold x coordinate values
            sum_y_coordinates = 0  # to hold y coordinate values
            sum_z_coordinates = 0  # to hold z coordinate values
            sum_num_points = 0  # to hold number of points

            # Iterate through points and get total of each coordinate of points with matching cluster id
            for point in self.points:
                if (point.cluster_id == ref_cluster_id):
                    sum_x_coordinates += float(point.x)
                    sum_y_coordinates += float(point.y)
                    if (self.dimension == 3):
                        sum_z_coordinates += float(point.z)
                    sum_num_points += 1

            # Get average of each coordinate and update centroid coordinates
            if (sum_num_points != 0):
                centroid.x = sum_x_coordinates / sum_num_points
                centroid.y = sum_y_coordinates / sum_num_points
                centroid.z = sum_z_coordinates / sum_num_points

            # Check if the centroid
            same_point = check_same_coordinate(centroid, ref_centroid)

            # If centroids are not the same return false
            if (same_point == False):
                flag_all_same_coordinate = False

        # return flag
        return  flag_all_same_coordinate


# Q3

# Import necessary libraries
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# main
def main():

    kmeans = MyKmeans(5, 200, 2, (0,0), (200,200))  # create instance of k means
    kmeans.generate_points()   # generate points
    kmeans.assign_random_clust_number()  # assign cluster numbers to points
    kmeans.initialize_centroids()  # create centroids

    flag_terminate = False  # set flag

    #  update centroids while flag is false
    while (flag_terminate == False):
        kmeans.assign_clust_number()
        flag_terminate = kmeans.update_centroid()
        print(flag_terminate)

    #  plot k means cluster
    def plot_clust_points(mykmean, pt_size = 100, centroid_size=200, pt_marker="o", centroid_marker="X"):
        # create a color map object based on a rainbow colormap
        cmap = cm.get_cmap('rainbow', mykmean.k)

        # randomize the color index list
        idx_sh = list(range(mykmean.k))
        random.shuffle(idx_sh)

        # assign a color for points and a centroid for each cluster
        for i in mykmean.points:
            plt.scatter(i.x, i.y, c=[cmap(idx_sh[i.cluster_id - 1])], marker=pt_marker, s=pt_size)

        for i in mykmean.centroids:
            pt = mykmean.centroids[i]
            plt.scatter(pt.x, pt.y, c=[cmap(idx_sh[pt.cluster_id - 1])], marker=centroid_marker, s=centroid_size)

        plt.show()  # show plot

    plot_clust_points(kmeans)

if __name__ == '__main__':
        main()

