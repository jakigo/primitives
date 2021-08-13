import numpy as np

class Point2d:
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


    def unit(self):
        return Point2d(1,0)
                
    def sum(self, beta):
        return Point2d(self.x + beta.x, self.y + beta.y)
        
    def multiply(self, num):
        return Point2d(self.x * num, self.y * num)
        
    def as_numpy(self):
        return np.array([self.x, self.y])
        
    def from_numpy(self, array):
        return Point2d(array[0], array[1])

    def to_point(self, z = 0):
        from primitives.point import Point
        return Point(self.x, self.y, z)
        
    def rot90(self):
        return Point2d(self.y, - self.x)

    def __str__(self):
        return f"<{self.x} {self.y}>"
        
        