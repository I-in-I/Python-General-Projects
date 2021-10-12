from math import hypot

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__x1 = vertice1._Point__x
        self.__y1 = vertice1._Point__y
        
        self.__x2 = vertice2._Point__x
        self.__y2 = vertice2._Point__y
        
        self.__x3 = vertice3._Point__x
        self.__y3 = vertice3._Point__y

    def perimeter(self):
        x1, x2, x3 = self.__x1, self.__x2, self.__x3
        y1, y2, y3 = self.__y1, self.__y2, self.__y3

        distance1 = hypot(x1 - x2, y1 - y2)
        distance2 = hypot(x1 - x3, y1 - y3)
        distance3 = hypot(x2 - x3, y2 - y3)
        perimeter = distance1 + distance2 + distance3
        return perimeter


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
