import numpy as np
from primitives.point2d import Point2d

class Point:
    
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

        
    def set(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
              
    def unit(self):
        self.x = 0
        self.y = 0
        self.z = 1
        
    def sum(self, beta):
        return Point(self.x + beta.x, self.y + beta.y, self.z + beta.z)
        
    def multiply(self, num):
        return Point(self.x * num, self.y * num, self.z * num)
        
    def as_numpy(self):
        return np.array([self.x, self.y, self.z])
        
    def from_numpy(self, array):
        return Point(array[0], array[1], array[2])
    
    def to_2dpoint(self):
        return Point2d(self.x, self.y)
        
    def __str__(self):
        return f"<{self.x} {self.y} {self.z}>"
        