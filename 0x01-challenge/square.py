#!/usr/bin/python3
"""
square class
"""


class Square:
    """attribute"""

    width = 0
    height = width

    def __init__(self, width, height):
        """init"""
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """Area of the square"""
        return self.width * self.height

    def perimeter_of_my_square(self):
        """permiter of square"""
        return (self.width * 4)

    def __str__(self):
        """str"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
