import unittest
from maker.component import Component, parameters


@parameters(param = {"alfa":0.1, "beta":0.2,"vals" : {"teta":0, "gamma":2}})
class Example(Component):
    def __init__(self, name):
        self.name = name

    def create(self):





class TestCoordSystem(unittest.TestCase):

    def test_component(self):
        Example("jacopo")
        

    
        

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