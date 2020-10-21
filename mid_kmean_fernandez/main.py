# #######################################
# # Name: Shad Fernandez
# # RedID: 810466716
# # Date: 16-OCT-2020
# #######################################

import mid_kmean_fernandez.libs.MyKmean as mk
import os

def main():

    # check if output directory exists, otherwise create one
    if not os.path.isdir('./output'):
       os.mkdir('./output')

    file_path_1 = './data/s1.txt'  # data set file path
    file_path_2 = './data/Aggregation.txt' # data set file path
    save_file_path = './output/kmeans_'  # file path to Save

    kmeans_1 = mk.MyKmeans()
    kmeans_1.read_xy_from_file(file_path_1)

    # kmeans_2 = mk.MyKmeans()
    # kmeans_2.read_xy_from_file(file_path_2)

    flag_terminate = False  # flag

    k_list_1 = [10,15,20]  # list of k values
    k_list_2 = [5,7,9,]  # list of k values

    for num in range(len(k_list_1)):
        kmeans_1.k = k_list_1[num]
        kmeans_1.assign_random_clust_number()
        kmeans_1.initialize_centroids()

        while(flag_terminate == False):
            kmeans_1.assign_clust_number()
            flag_terminate = kmeans_1.update_centroid()

        kmeans_1.save_clust_points(save_file_path + str(num) + '_2d.png')

    # for num in range(k_list_2):
    #     kmeans_2.k = k_list_2[num]
    #     kmeans_2.assign_random_clust_number()
    #     kmeans_2.initialize_centroids()
    #
    #     while(flag_terminate == False):
    #         kmeans_2.assign_clust_number()
    #         flag_terminate = kmeans_2.update_centroid()
    #
    #     kmeans_2.save_clust_points(save_file_path + str(num) + '_2d.png')


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

