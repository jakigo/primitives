import unittest
from primitives.point import Point
from primitives.vector import Vector
from primitives.coord_system import CoordSystem

class TestCoordSystem(unittest.TestCase):

    def test_projects(self):
        origin = Point(10,30,90)
        p0 = Point(1,0,0)
        p1 = Point(0,1,0)

        p3 = Point(1,2,3)
        coord = CoordSystem(Vector(origin,p0), Vector(origin,p1))
        for ax in [0,1,2]:
            px = coord.project_point(p3, axis=ax)
            py = coord.de_project_point(px, axis=ax)
            val = py.sum(p3.multiply(-1))
            val = val.x + val.y + val.z
            if val < 0.0000001:
                val = 0
            self.assertEqual(val, 0)
            
    def test_vector(self):
        origin = Point(0,0,0)
        p0 = Point(1,0,0)
        p1 = Point(0,1,0)    
        coord = CoordSystem(Vector(origin,p0), Vector(origin,p1))

        destz = Point(0,0,1)
        desty = Point(0,1,0)
        destx = Point(1,0,0)
        for ax,po in zip([0,1,2], [destz,desty,destx]):
            vec = coord.get_plane(ax)
            self.assertEqual(vec.pointB.x , po.x )
            self.assertEqual(vec.pointB.y , po.y )        
            self.assertEqual(vec.pointB.z , po.z )    

    
        

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