import unittest
from primitives.point import Point

class TestPoint(unittest.TestCase):

    def test_create(self):
        p0 = Point()
        self.assertEqual(p0.x, 0)
        self.assertEqual(p0.y, 0)
        self.assertEqual(p0.z, 0)
    def test_sum(self):
        p0 = Point(2, 5, 7)
        p1 = Point(3, 20, 100).sum(p0)
        self.assertEqual(p1.x, 5)
        self.assertEqual(p1.y, 25)
        self.assertEqual(p1.z, 107)

    def test_mol(self):
        p1 = Point(3, 20, 2).multiply(5)
        self.assertEqual(p1.x, 15)
        self.assertEqual(p1.y, 100)
        self.assertEqual(p1.z, 10)
        
    def test_as_numpy(self):
        p0 = Point(2, 20, 5)
        num = p0.as_numpy()
        self.assertEqual(num[0], 2)
        self.assertEqual(num[1], 20)
        self.assertEqual(num[2], 5)
        
    def test_reconv(self):
        p0 = Point(2, 20, 5)
        num = Point().from_numpy(p0.as_numpy())
        self.assertEqual(num.x, 2)
        self.assertEqual(num.y, 20)
        self.assertEqual(num.z, 5)
    

        

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