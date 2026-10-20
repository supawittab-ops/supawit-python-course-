class Rectangle:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def getArea(self):
        return self.__length * self.__width

    def getPerimeter(self):
        return 2 * (self.__length + self.__width)

    def isSquare(self):
        return self.__length == self.__width


rect1 = Rectangle(5, 10)
print(f"Area of {5} width and {10} length = {rect1.getArea()}")
print(f"Perimeter = {rect1.getPerimeter()}")
print(f"Is square? {rect1.isSquare()}")

rect2 = Rectangle(10, 10)
print(f"Area = {rect2.getArea()}")
print(f"Perimeter = {rect2.getPerimeter()}")
print(f"Is square? {rect2.isSquare()}")