#!/usr/bin/python3
"""Rectangle class Module"""

BaseGeometry =__import__.(8-rectangle.py).BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        super().__init__(self, width, height)
    def area(self):
    """Override area() to calculate the rectangle's area"""
        return self.width * self.height
    def __str__(self):
        return '[Rectangle] {width}/{height}'.format(self.width ,self.height)
