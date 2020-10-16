import mid_kmean_fernandez.libs.MyKmean as mk

def main():

    kmeans = mk.MyKmeans(4, 150, 2, (0 ,0), (150 ,200))  # create instance of k means
    # kmeans.set_parameters()
    kmeans.generate_points()   # generate points
    kmeans.assign_random_clust_number()  # assign cluster numbers to points
    kmeans.initialize_centroids()  # create centroids

    flag_terminate = False  # set flag

    #  update centroids while flag is false
    while (flag_terminate == False):
        kmeans.assign_clust_number()
        flag_terminate = kmeans.update_centroid()
        print(flag_terminate)

    mk.plot_clust_points(kmeans)


if __name__ == '__main__':
    main()

