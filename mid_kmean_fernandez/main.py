import mid_kmean_fernandez.libs.MyKmean as mk
import mid_kmean_fernandez.libs.Point as pt


# def read_xy_from_file(self, file_path):
#     self.points = []
#     f = open(file_path, 'r')
#     lines = f.readlines()
#     return lines

def main():

    file_path = './data/s1.txt'
    flag_terminate = False

    myKmeans = mk.MyKmeans()
    myKmeans.read_xy_from_file(file_path)
    myKmeans.assign_random_clust_number()
    myKmeans.initialize_centroids()

    while(flag_terminate == False):
        myKmeans.assign_clust_number()
        flag_terminate = myKmeans.update_centroid()

    myKmeans.save_clust_points(file_path)


    # kmeans = mk.MyKmeans(4, 150, 2, (0 ,0), (150 ,200))  # create instance of k means
    # # kmeans.set_parameters()
    # kmeans.generate_points()   # generate points
    # kmeans.assign_random_clust_number()  # assign cluster numbers to points
    # kmeans.initialize_centroids()  # create centroids
    #
    # flag_terminate = False  # set flag
    #
    # #  update centroids while flag is false
    # while (flag_terminate == False):
    #     kmeans.assign_clust_number()
    #     flag_terminate = kmeans.update_centroid()
    #     print(flag_terminate)
    #
    # mk.plot_clust_points(kmeans)




if __name__ == '__main__':
    main()

