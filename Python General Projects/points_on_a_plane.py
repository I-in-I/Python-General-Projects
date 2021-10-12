from math import hypot
# hypot() takes the delta of x and y

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        x1 = self.__x
        y1 = self.__y
        x2 = x
        y2 = y
        distance = hypot(x2 - x1, y2 - y1)
        return distance
    
    def distance_from_point(self, point):
        x1 = self.__x
        y1 = self.__y
        x2 = point.getx()
        y2 = point.gety()
        distance = hypot(x2 - x1, y2 - y1)
        return distance

point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
