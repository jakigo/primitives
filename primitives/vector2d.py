import numpy as np
from primitives.point2d import Point2d


class Vector2d:
    def __init__(self, pointA = Point2d(), pointB = Point2d().unit()):
        self.pointA = pointA
        self.pointB = pointB
        
    def set(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB
        
    def unit(self):
        return Vector2d(Point2d(), Point2d(1,0))
                
    def sum(self, beta):
        return Vector2d(self.pointA.sum(beta.pointA), self.pointB.sum(beta.pointB))
        
    def multiply(self, num):
        return Vector2d(self.pointA.multiply(num), self.pointB.multiply(num))
        
    def sum_start(self, beta):
        return Vector2d(self.pointA.sum(beta.pointA), self.pointB.sum(beta.pointB))
        
    def multiply_start(self, num):
        return Vector2d(self.pointA.multiply(num), self.pointB )
        
    def sum_end(self, beta):
        return Vector2d(self.pointA.sum(beta.pointA), self.pointB )
        
    def multiply_end(self, num):
        return Vector2d(self.pointA , self.pointB.multiply(num))
        
    def as_numpy(self):
        return np.array([ self.pointA.as_numpy(), self.pointB.as_numpy() ])
        
    def from_numpy(self, array):
        return Vector2d(Point2d().from_numpy(array[0]), Point2d().from_numpy(array[1]))
        
    def as_numpy_direction(self):
        return self.pointB.as_numpy() - self.pointA.as_numpy()
        
    def from_numpy_direction(self, array, origin= Point2d()):
        po = Point2d().from_numpy(array)
        po = origin.sum(po)
        return Vector2d(origin, po)
    
    def normalize(self):
        p = self.as_numpy_direction()
        p = p / np.sqrt(np.dot(p, p))
        return Vector2d().from_numpy_direction(p)

    def as_vector(self, z = 0):
        from primitives.vector import Vector
        return Vector(self.pointA.to_point(z), self.pointB.to_point(z) )

    def point_from_interpolation(self, t):
        return self.pointA.multiply(1-t).sum(self.pointB.multiply(t))

    def rot90(self):
        p0 = self.pointA.as_numpy()
        p1 = self.pointB.as_numpy()
        p1 = p1 - p0
        p1 = np.array([p1[1], - p1[0]])

        return Vector2d().from_numpy(np.array([p0,p1]))

    
        
    def __str__(self):
        return f"<{self.pointA} {self.pointB}>"
        
        
    
        
    
        