import unittest
from primitives.vector import Vector
from primitives.vector import Point
import numpy as np

class TestVector(unittest.TestCase):



    def test_create_as_numpy(self):
        v = Vector(Point(1,2,3), Point(1,2,10))
        v = v.as_numpy()
        tt = np.equal(np.array([[1,2,3],[1,2,10]]), v)
        self.assertEqual( tt.all(), True )
        
    def test_math_ops(self):
        def equa(a, b):
            self.assertEqual(a.pointA.x,b.pointA.x)
            self.assertEqual(a.pointA.y,b.pointA.y)
            self.assertEqual(a.pointA.z,b.pointA.z)
        
            self.assertEqual(a.pointB.x,b.pointB.x)
            self.assertEqual(a.pointB.y,b.pointB.y)
            self.assertEqual(a.pointB.z,b.pointB.z)
        a = Vector(Point(1,2,3), Point(1,2,10))
        b = Vector(Point(10,9,8), Point(7,6,5))
        c = a.sum(b)
        d = a.sum(b).sum(b.multiply(-1))
        equa(a, d)
        equa(c, Vector(Point(11,11,11), Point(8,8,15)))
        
    def test_normalize(self):
        def equa(a, b):
            self.assertEqual(a.pointA.x,b.pointA.x)
            self.assertEqual(a.pointA.y,b.pointA.y)
            self.assertEqual(a.pointA.z,b.pointA.z)
        
            self.assertEqual(a.pointB.x,b.pointB.x)
            self.assertEqual(a.pointB.y,b.pointB.y)
            self.assertEqual(a.pointB.z,b.pointB.z)
        a = Vector(Point(1,2,3),Point(1,2,200)).normalize()
        equa(a, Vector().from_numpy_direction(np.array([0,0,1])))
        
    def test_cr(self):
        def equa(a, b):
            self.assertEqual(a.pointA.x,b.pointA.x)
            self.assertEqual(a.pointA.y,b.pointA.y)
            self.assertEqual(a.pointA.z,b.pointA.z)
        
            self.assertEqual(a.pointB.x,b.pointB.x)
            self.assertEqual(a.pointB.y,b.pointB.y)
            self.assertEqual(a.pointB.z,b.pointB.z)     
            
        origin = Point(3,4,5)
        last = Point(4,5,6)
        alfa = Vector(origin, last)
        beta = Vector().from_numpy_direction(alfa.as_numpy_direction(), origin)
        nu = alfa.as_numpy()
        teta = Vector(Point().from_numpy(nu[0]), Point().from_numpy(nu[1])  )
        equa(alfa,beta)
        equa(alfa,teta)
        
        
        

if __name__ == '__main__':
    unittest.main()
    
    
 #   def sum(self, beta):
 #       return Point(self.x + beta.x, self.y + beta.y, self.z + beta.z)
        
 #   def multiply(self, num):
 #       return Point2d(self.x * num self.y * num, self.z * num)
        
 #   def as_numpy(self):
 #       return np.array([self.x, self.y, self.z])
        
 #   def from_numpy(self, array):
  #      return Point2d(array[0], array[1], array[2])
    
  #  def to_2dpoint(self):
  #      return Point2d(self.x, self.y)