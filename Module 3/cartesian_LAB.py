# define class Point, with two arguments x and y defaulting to zero
# all properties private
# getx() and gety() to return the respective coordinate
# method distance_from_xy(x, y) which calculates and returns the distance between the point in the object and the point given by the arguments
# method distance_from_point(point) which calculates and returns the distance between the points

from math import sqrt 

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y
    
    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return sqrt((self.__x - x)**2 + (self.__y - y)**2)
    
    def distance_from_point(self, point):
        return sqrt((self.__x - point.getx())**2 + (self.__y - point.gety())**2)

class Triangle:
    def __init__(self, vertex1, vertex2, vertex3):
        self.__v1 = vertex1
        self.__v2 = vertex2
        self.__v3 = vertex3
    
    def perimeter(self):
        return self.__v1.distance_from_point(self.__v2) + self.__v2.distance_from_point(self.__v3) + self.__v3.distance_from_point(self.__v1)


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))

triangle = Triangle(Point(0,0), Point(1,0), Point(0,1))
print(triangle.perimeter())
