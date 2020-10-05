# #######################################
# # Name: Shad Fernandez
# # RedID: 810466716
# # Date: 16-SEP-2020
# #######################################


# Q1

import math
import random
import statistics

# Q2

class Triangle:
    def __init__(self, p1 = (0,0), p2 = (3,0), p3 = (3,4)):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.area = self.get_area()
        self.perimeter = self.get_perimeter()
        self.is_right = 0


    def get_area(self):
        self.area = math.fabs((self.p1[0]*(self.p2[1]-self.p3[1])) - (self.p2[0]*(self.p3[1]-self.p1[1]))
                              - (self.p3[0]*(self.p1[1]-self.p2[1])))/2
        return self.area

    def __get_distance(self, p1, p2):
        length = math.sqrt(((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2))
        return length
    def get_perimeter(self):
        self.perimeter = self.__get_distance(self.p1,self.p2) + self.__get_distance(self.p2,self.p3) \
                         + self.__get_distance(self.p3,self.p1)
        return self.perimeter

    # def is_right(self):
    #     sides = (self.__get_distance(self.p1,self.p2),self.__get_distance(self.p2,self.p3),
    #              self.__get_distance(self.p3,self.p1))
    #
    #     longest_side = sides[0]
    #     longest_index = 0
    #     for index in range(len(sides), 1):
    #         if sides[index] > longest_side:
    #             longest_side = sides[index]
    #             longest_index = index

random.seed(500)

triangle_list = []
triangle_distances = []

for num in range(10):
    triangle_list.append(Triangle((random.randint(1,500),random.randint(1,500)),(random.randint(1,500),random.randint(1,500))
                                  ,(random.randint(1,500),random.randint(1,500))))

for items in triangle_list:
    triangle_distances.append(items.get_area())

print(statistics.mean(triangle_distances))
print(statistics.median(triangle_distances))
print(statistics.stdev(triangle_distances))

# Q3



