from primitives.point import Point
from primitives.vector import Vector
from primitives.coord_system import CoordSystem
class Polygon:
    def __init__(self, point_arra = []):
        self.point_array = point_arra
    def to_point_array(self):
        return self.point_array
    def to_vectors(self):
        return [Vector(a, b) for a, b in zip(self.point_array[:-1], self.point_array[1:])] + [Vector(self.point_array[-1], self.point_array[0])]
    
    def to_2d_vectors(self, coord = None):
        if coord == None:
            coord = self.get_coord_system()
        return [ coord.project_vector(x).as_2dvector() for x in self.to_vectors() ]

    def get_coord_system(self):
        vectors = self.to_vectors()
        return CoordSystem(vectors[0], vectors[1])        

    def from_2d_vectors(self, vectors, coord=None):
        if coord == None:
            coord = self.get_coord_system()
        projected_vectors = [ coord.de_project_vector(x.as_vector())for x in vectors]
        return Polygon([x.pointA for x in projected_vectors])
        

    


