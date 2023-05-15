# create a Circle constructor that creates a circle with a radius provided by an argument. The circles constructed must
# have two getters getArea() (PI*r^2) and getPerimeter() (2*PI*r) which give both respective areas and perimeter
# (circumference).
#
# circy = Circle(11)
# circy.getArea()
# Should return 380.132711084365

# circy = Circle(4.44)
# circy.getPerimeter()

# Should return 27.897342763877365
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = math.pi*self.radius**2
        return area

    def get_perimeter(self):
        perimeter = 2*math.pi*self.radius
        return perimeter


if __name__ == '__main__':
    circy = Circle(11)
    print(circy.get_area())

    circy1 = Circle(4.44)
    print(circy1.get_perimeter())
