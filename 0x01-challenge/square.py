#!/usr/bin/python3
"""
square class
"""


class Square():
    """attribute"""
    side = 0

    def __init__(self, side):
        """init"""
        self.side = side

    def area_of_my_square(self):
        """Area of the square"""
        return self.side**2

    def perimeter_of_my_square(self):
        """permiter of square"""
        return self.side * 4

    def __str__(self):
        """str"""
        return "{}".format(self.side)


if __name__ == "__main__":
    s = Square(side=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
