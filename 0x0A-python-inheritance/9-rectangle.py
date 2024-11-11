#!/usr/bin/python3
"""Rectangle class Module"""

BaseGeometry =__import__.(8-rectangle.py).BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class"""
    super().__init__(self, width, height)
    super().area()
    def __str__(self):
        return '[Rectangle] {width}/{height}'.format(self.width ,self.height)
