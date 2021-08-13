import numpy as np
from primites.coord_system import CoordSystem
class Plane:
    def __init__(self, vector = Vector().unit()):
        self.vector = vector
        
    def as_numpy(self):
        return self.vector.as_numpy()
        
    def from_numpy(self, arr):
        return Plane().from_numpy(arr)
        
    def normal(self):
        return self.vector.normalize()
        
    def get_coord_system(self, vector):
        return CoordSystem(self.vector, vector)
        
    def from_coord_system(self, coordinate):
        self.vector = CoordSystem(self.vector, vector).de_project_vector(Vector().unit())
        
    def intersect(self, plane):
        normal2 = plane.normal()
        
        
        
        
        
        