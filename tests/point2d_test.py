import unittest
from primitives.point import Point2d

class TestPoint2d(unittest.TestCase):

    def test_create(self):
        p0 = Point2d()
        self.assertEqual(p0.x, 0)
        self.assertEqual(p0.y, 0)
    def test_sum(self):
        p0 = Point2d(2, 5)
        p1 = Point2d(3, 20).sum(p0)
        self.assertEqual(p1.x, 5)
        self.assertEqual(p1.y, 25)

    def test_mol(self):
        p1 = Point2d(3, 20).multiply(5)
        self.assertEqual(p1.x, 15)
        self.assertEqual(p1.y, 100)
        
    def test_as_numpy(self):
        p0 = Point2d(2, 20)
        num = p0.as_numpy()
        self.assertEqual(num[0], 2)
        self.assertEqual(num[1], 20)
        
    def test_reconv(self):
        p0 = Point2d(2, 20)
        num = Point2d().from_numpy(p0.as_numpy())
        self.assertEqual(num.x, 2)
        self.assertEqual(num.y, 20)
        
    def test_rot90(self):
        p0 = Point2d(5, 7)
        p1 = p0.rot90()
        p2 = p1.rot90()
        p3 = p2.rot90()
        
        p4 = p3.rot90()
        
        
        def assertZero(ve):
            self.assertEqual(ve.x, 0)
            self.assertEqual(ve.y, 0)
            
        assertZero(p0.sum(p2))
        assertZero(p1.sum(p3))
        
        self.assertEqual(p4.x, p0.x)
        self.assertEqual(p4.y, p0.y)
        
        
        

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