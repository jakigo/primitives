import unittest
from primitives.point import Point
from shape.polygon import Polygon

class TestPolygon(unittest.TestCase):

    def test_create(self):
        p0 = Point(3,4,5)
        p1 = Point(33,-4,10)
        p2 = Point(12,7,8)
        poly = Polygon([p0,p1,p2])
        for ve, po in zip(poly.from_2d_vectors(poly.to_2d_vectors()).to_point_array(), [p0,p1,p2]):
            val = ve.sum(po.multiply(-1))
            val = val.x + val.y + val.z
            if val < 0.0000001:
                val = 0
            self.assertEqual(val, 0)

    def test_create_to_vector(self):
        p0 = Point(3,4,5)
        p1 = Point(33,-4,10)
        p2 = Point(12,7,8)
        poly = Polygon([p0,p1,p2])
        for pp in poly.to_vectors():
            print(pp)



        
        

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