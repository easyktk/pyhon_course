import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y


    def getx(self):
        return self.__x

    def gety(self):
        return self.__y


    def distance_from_xy(self, x, y):
        return math.sqrt(((self.__x - x)**2 + (self.__y - y)**2))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


#
# Write code here
#
if __name__ == "__main__":

    point1 = Point(0, 0)
    point2 = Point(1, 1)
    print(point1.distance_from_point(point2))
    print(point2.distance_from_xy(2, 0))
