
import sys  # import necessary package

import random
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import csv


import mid_kmean_fernandez.libs.Utility as ut
import mid_kmean_fernandez.libs.Point as pt

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
            self.k = int(input("Enter the k value: "))  # get k value
            self.num_points = int(input("Enter number of points: "))  # get num_points value
            self.dimension = int(input("Enter number of dimensions: "))  # get dimensions

            # Retrieve lower bound and upper bound values
            list_values = []  # hold user input for lower bound values

            # Retrieve lower bound and upper bound for 2 dimensions
            if (self.dimension == 2):
                for num in range(self.dimension):
                    list_values.append(float(input("Enter a lower bound value: ")))
                self.lower_bound = tuple(list_values)
                list_values.clear()
                for num in range(self.dimension):
                    list_values.append(float(input("Enter an upper bound value: ")))
                self.upper_bound = tuple(list_values)
            # Retrieve for three dimensions
            else:
                for num in range(self.dimension):
                    list_values.append(float(input("Enter a lower bound value: ")))
                self.lower_bound = tuple(list_values)
                list_values.clear()
                for num in range(self.dimension):
                    list_values.append(float(input("Enter an upper bound value: ")))
                self.upper_bound = tuple(list_values)

        #  throw ValueError if non numeric values are entered
        except ValueError:
            print("A valid numeric value was not detected. Please try again.")
            sys.exit(1)

    def generate_points(self):
        """
        Method generates Point objects with random coordinates and store in points
        """
        self.points = ut.random_coordinates(self.num_points, self.dimension, self.lower_bound, self.upper_bound)

    def initialize_centroids(self):
        """
        Method stores k random Points as centroids in centroids
        """
        random_k_point = random.sample(self.points,self.k)  # list of k random numbers  between 0 and num_points
        # create dictionary of k random points withing uppd
        for val in range(1, (self.k + 1)):  # assign key value starting at 1 to k
            reference_point = random_k_point[val - 1]  # assign random point to dictionary
            self.centroids[val] = pt.Point(reference_point.x, reference_point.y, reference_point.z, val)


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
            ref_centroid = pt.Point(centroid.x, centroid.y, centroid.z, centroid.cluster_id)  # create reference centroid
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
            same_point = ut.check_same_coordinate(centroid, ref_centroid)

            # If centroids are not the same return false
            if (same_point == False):
                flag_all_same_coordinate = False

        # return flag
        return  flag_all_same_coordinate

    def read_xy_from_file(self, file_path):

        self.points = []

        f = open(file_path, 'r')
        lines = f.readlines()

        list_x = []
        list_y = []
        list_z = []

        for line in lines:
            line_list = str.split(line)
            if len(line_list) == 2:
                self.points.append(pt.Point(float(line_list[0]), float(line_list[1])))
                list_x.append(int(line_list[0]))
                list_y.append(int(line_list[1]))
            else:
                self.points.append(pt.Point(float(line_list[0]), float(line_list[1]), float(line_list[2])))
                list_x.append(int(line_list[0]))
                list_y.append(int(line_list[1]))
                list_z.append(int(line_list[2]))

        if len(list_z) == 0:
            self.lower_bound = (min(list_x),min(list_y))
            self.upper_bound = (max(list_x),max(list_y))
        else:
            self.lower_bound = (min(list_x),min(list_y),min(list_z))
            self.upper_bound = (max(list_x),max(list_y),max(list_z))

    def save_clust_points(mykmean, out_file_path, pt_size=100, centroid_size=200, pt_marker="o", centroid_marker="x"):
        cmap = plt.cm.get_cmap('rainbow', mykmean.k)

        idx_sh = list(range(mykmean.k))
        random.shuffle(idx_sh)

        for i in mykmean.points:
            plt.scatter(i.x, i.y, c=cmap(idx_sh[i.cluster_id-1]), marker=pt_marker, s=pt_size)
        for i in mykmean.centroids:
            pt = mykmean.centroids[i]
            plt.scatter(pt.x, pt.y, c=cmap(idx_sh[pt.cluster_id-1]), marker=centroid_marker, s=centroid_size)
        plt.savefig(out_file_path)

    def save_clust_point_csv(self):

        file_1 = open('./output/data_points.csv', 'w')
        file_2 = open('./output/cluster_centroids.csv', 'w')

        with file_1:
            writer = csv.writer(file_1)

            for point in self.points:
                writer.writerow([point.x,point.y,point.z,point.cluster_id])

        with file_2:
            writer = csv.writer(file_2)

            for i in self.centroids:
                centroids = self.centroids[i]
                writer.writerow([centroids.x, centroids.y, centroids.z, centroids.cluster_id])






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


