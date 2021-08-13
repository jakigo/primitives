import numpy as np
from primitives.point import Point
from primitives.vector2d import Vector2d

class Vector:
    def __init__(self, pointA = Point(), pointB = Point().unit()):
        self.pointA = pointA
        self.pointB = pointB
        
    def set(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB
        
    def unit(self):
        return Vector(Point(), Point(1,0,0))
                
    def sum(self, beta):
        return Vector(self.pointA.sum(beta.pointA), self.pointB.sum(beta.pointB))
        
    def multiply(self, num):
        return Vector(self.pointA.multiply(num), self.pointB.multiply(num))
        
    def sum_start(self, beta):
        return Vector(self.pointA.sum(beta.pointA), self.pointB.sum(beta.pointB))
        
    def multiply_start(self, num):
        return Vector(self.pointA.multiply(num), self.pointB )
        
    def sum_end(self, beta):
        return Vector(self.pointA.sum(beta.pointA), self.pointB )
        
    def multiply_end(self, num):
        return Vector(self.pointA , self.pointB.multiply(num))
        
    def as_numpy(self):
        return np.array([ self.pointA.as_numpy(), self.pointB.as_numpy() ])
        
    def from_numpy(self, array):
        return Vector(Point().from_numpy(array[0]), Point().from_numpy(array[1]))
        
    def as_numpy_direction(self):
        return self.pointB.as_numpy() - self.pointA.as_numpy()
        
    def from_numpy_direction(self, array, origin= Point()):
        po = Point().from_numpy(array)
        po = origin.sum(po)
        return Vector(origin, po)
    
    def normalize(self):
        p = self.as_numpy_direction()
        p = p / np.sqrt(np.dot(p, p))
        return Vector().from_numpy_direction(p)

    def as_2dvector(self):
        return Vector2d(self.pointA.to_2dpoint(), self.pointB.to_2dpoint()) 
        
    def __str__(self):
        return f"<{self.pointA} {self.pointB}>"
        
        
    
        
    
        