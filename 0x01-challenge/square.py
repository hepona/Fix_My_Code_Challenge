#!/usr/bin/python3
"""
square class
"""


class Square:
    """attribute"""

    def __init__(self, size=0):
        """init"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size

    def area_of_my_square(self):
        """Area of the square"""
        return self.size * self.size

    def perimeter_of_my_square(self):
        """permiter of square"""
        return self.size * 4

    def __str__(self):
        """str"""
        return "{}".format(self.size)


if __name__ == "__main__":
    s = Square(size=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
