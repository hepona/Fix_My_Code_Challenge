#!/usr/bin/python3
"""module"""


class Square:
    """class square"""

    width = 0
    height = 0

    def __init__(self, height, width):
        """init"""
        self.height = height
        self.width = width

    def area_of_my_square(self):
        """Area of the square"""
        return self.width * self.height

    def perimeter_of_my_square(self):
        """perimeter of square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """printe width and height"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
