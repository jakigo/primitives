import unittest
from maker.mesh import Mesh
from maker.parameter_basket import save_parameters, load_parameters

class TestPoint(unittest.TestCase):


    
    def test_create(self):
        all_meshes = Mesh()
        def recreate(mesh_int = None):
            print(".")
            if load_parameters():
                print("+")
                mesh = all_meshes.eval()
                #save_parameters()
                if mesh_int != None:
                    #import ipdb;ipdb.set_trace()
                    for geo in mesh_int.geometry.keys():
                        mesh_int.delete_geometry(geo)
                    mesh_int.add_geometry(mesh)

                return mesh


        mesh = recreate()
        mesh.show(callback=recreate)

    

        

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